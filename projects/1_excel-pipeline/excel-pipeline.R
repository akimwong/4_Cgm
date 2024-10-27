library(readxl)
library(openxlsx)
library(mongolite)
library(jsonlite)

# Path to the Excel file
ruta_archivo <- "projects/1_excel-pipeline/data.xlsx"

# Read the spreadsheet into a DataFrame (DataFrame in R)
df <- read_excel(ruta_archivo, sheet = "Sheet1")

# Define a function to convert Excel numeric values to dates
# with a specific format dd/mm/yyyy
convertir_a_fecha <- function(valor) {
  tryCatch({
    num_valor <- as.numeric(valor)
    if (!is.na(num_valor)) {
      format(as.Date(num_valor, origin = "1899-12-30"), "%d/%m/%Y")
    } else {
      NA
    }
  }, error = function(e) NA)  # Return NA if an error occurs
}

# Convert commas to periods and then to numeric 
convertir_a_numero <- function(valor) {
  valor <- gsub(",", ".", valor)  # Replace comma with period
  as.numeric(valor)               # Convert to numeric
}

# Define a function to detect and convert types in each value of
# mixed columns
detect_and_convert <- function(value) {
  if (is.na(value) || value == "") {
    return("")  # Keep empty cells as NA
    # Double condition to transform numbers to dates
    # Detect numbers representing dates in Excel format
  } else if (!is.na(suppressWarnings(as.numeric(value))) &&
             grepl("^[0-9]{5}$", value)) {
    # Convert to date with specific format
    return(convertir_a_fecha(value))
    # Detect numbers (integers or decimals)
  } else if (grepl("^[0-9]+(\\.[0-9]+)?$", value)) {
    # Use the function convertir_a_numero
    return(convertir_a_numero(value))
  } else {
    # Keep the value as text if it's not a number or date
    return(value)
  }
}

# Apply the function to each cell (not each column) in the data frame
df <- as.data.frame(
  lapply(df, function(column) {
    apply(as.matrix(column), 1, detect_and_convert)
  })
)

# Set up the connection to the MongoDB database
client <- mongo(collection = "Dataset",
                db = "Table1",
                url = "mongodb://localhost:27017/")
historico <- mongo(collection = "Dataset_Historic",
                   db = "Table1",
                   url = "mongodb://localhost:27017/")

# Get the current date and time in custom format
formatted_datetime <- format(Sys.time(), "%Y-%m-%d %H:%M")

# Load existing data into a list to reduce queries to MongoDB
existing_data <- client$find(fields = '{"row_id": 1, 
                                        "col_name": 1, 
                                        "cell_value": 1, 
                                        "timestamp": 1}')
# Create a dictionary with the existing database data
existing_data_dict <- setNames(
  split(existing_data, seq_len(nrow(existing_data))),
  paste(existing_data$row_id, existing_data$col_name, sep = "_")
)
# Prepare lists for batch operations
operations <- list()
historical_operations <- list()

# Iterate over each row of the DataFrame, extracting the row's ID
for (i in seq_len(nrow(df))) {
  row <- df[i, ]
  row_id <- row$`ID.`
  
  # For each column in the row, get the cell value and generate a unique key
  for (col_name in names(df)) {
    cell_value <- row[[col_name]]
    key <- paste(row_id, col_name, sep = "_")
    existing_data_entry <- existing_data_dict[[key]]
    
    # Skip if the cell is empty and does not exist in the database
    if (is.na(cell_value) && is.null(existing_data_entry)) {
      next
    }
    
    # If it exists in the database, check for changes
    if (!is.null(existing_data_entry)) {
      existing_cell_value <- existing_data_entry$cell_value
      existing_timestamp <- existing_data_entry$timestamp
      
      # Update the value if it's different from the existing one
      if (cell_value != existing_cell_value) {
        # Create the update in the main collection
        operations <- append(operations, list(
          list(
            updateOne = list(
              filter = list(row_id = row_id, col_name = col_name),
              update = list(
                '$set' = list(
                  cell_value = cell_value,
                  timestamp = formatted_datetime
                )
              ),
              upsert = TRUE
            )
          )
        ))
        
        # Insert the previous value into the historical collection
        historical_operations <- append(historical_operations, list(
          list(
            row_id = row_id,
            col_name = col_name,
            cell_value = existing_cell_value,
            timestamp = existing_timestamp
          )
        ))
      }
    } else if (!is.na(cell_value)) {
      # If it doesn't exist in the database, insert as a new document
      operations <- append(operations, list(
        list(
          updateOne = list(
            filter = list(row_id = row_id, col_name = col_name),
            update = list(
              '$set' = list(
                cell_value = cell_value,
                timestamp = formatted_datetime
              )
            ),
            upsert = TRUE
          )
        )
      ))
    }
  }
}

# Execute the batch operations for the main collection
if (length(operations) > 0) {
  for (operation in operations) {
    client$update(
      query = toJSON(operation$updateOne$filter, auto_unbox = TRUE),
      update = toJSON(operation$updateOne$update, auto_unbox = TRUE),
      upsert = operation$updateOne$upsert
    )
  }
}

# Insert into the historical collection in a single step
if (length(historical_operations) > 0) {
  historical_df <- do.call(
    rbind,
    lapply(historical_operations, function(x) {
      as.data.frame(x, stringsAsFactors = FALSE)
    })
  )
  historico$insert(historical_df)
}