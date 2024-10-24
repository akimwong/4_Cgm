### 1. Excel to MongoDB Data Pipeline

<b>Short name:</b> Excel_Pipeline </p>
<b>Role:</b> Data Engineer </p>
<b>Technologies:</b> R, MongoDB, Excel </p>
<b>Tags:</b> Data Extraction, NoSQL Database </p>
<b>Key Tools:</b> Jupyter Notebooks-R, MongoDB Compass, Microsoft Excel </p>
<b>Description:</b> Developed a R script that extracts information from a large collaborative Excel file (around 70 columns × 2700 rows, to manage approximately 350 mini projects) and loads it into a structured MongoDB database. <b>The solution implements a tracking system that captures cell values with timestamps and monitors changes from approximately 11 concurrent users.</b> This approach maintains a complete historical record of modifications, enabling comprehensive audit trails while ensuring data integrity.

This foundational script sets the groundwork for future implementations:

- Automated data extraction from Excel to MongoDB
- Historical tracking system for all data changes
- Real-time monitoring of process advancement
- Automated notifications for task dependencies
- Performance metrics for task completion times


<b>SCRIPT Process Flow:</b>

1. Initialization:
- load Required Libraries (readxl, openxlsx, mongolite, jsonlite)
- read Excel Worksheet

2. Data Type Conversion Functions:
- convert_to_date: Excel numeric to date conversion
- convert_to_number: String to numeric conversion
- detect_and_convert: Main type detection and conversion

3. DataFrame Processing:
- apply type conversions to the entire DataFrame

4. MongoDB Connection:
- connect to main Dataset Collection
- connect to Historical Collection
- fetch existing records
- create data dictionary for efficient lookups

5. Data Processing:
- iterate through DataFrame rows
- process each column
- check for data changes
- prepare update operations
- prepare historical records

6. Database Update:
- execute batch updates on main collection
- insert historical records
