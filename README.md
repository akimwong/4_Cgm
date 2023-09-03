### Where do the revenues come from?
From circuit migration. The more circuits are migrated in a shorter time with the least amount of resources, the higher the revenues.

### What is the problem?
- In order to be migrated, each circuit must meet a series of technical and administrative requirements defined by TELEFONICA. If any of these requirements is not met, the circuit cannot be migrated.
- Many times, problems are detected on the eve of the migration date or at the moment of migration itself, leading to high levels of stress among the staff and resulting in the loss of resources when attempting to migrate the circuit for the second time.

### What tools do we have?
- Inventory tools from TELEFONICA
- An Excel sheet for each technical room containing a list of all the circuits to be migrated, which is used to track each project. These Excel sheets are shared, and around 10 technicians input and update various types of information.

### What about Excel?
- Excel is a basic tool, very intuitive and easy to CRUD (Create, Read, Update and Delete).
- Sharing an Excel file among multiple individuals carries the risk that anyone can modify each other's information (either accidentally or intentionally) without tracking changes. It is unknown how long each person takes to input their part of the project.

## STRATEGY 1 (FAILED)

1. Developed small programs to automate specific tasks one by one.
2. Shared the code and taught colleagues how to execute these programs for those specific tasks.
3. Create a database to periodically store changes made to each cell in all Excel worksheets for data analytics purposes.

#### Why it failed?:

1. The use of Jupyter Notebook as a User Interface (UI) was not user-friendly for typical employees.
2. Most importantly, many individuals did not recognize the importance of maintaining consistency in BASIC aspects of the Excel worksheet unless these changes directly affected them. These aspects include:
   - Keeping the same headers across all files
   - Maintaining consistent circuit coding from the beginning to the end of each project
   - Avoiding the creation of new columns with the same name as existing ones
   - Not incrementing new circuits with the same coding as previous circuits
