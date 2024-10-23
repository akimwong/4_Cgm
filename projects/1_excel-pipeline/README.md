### 1. Excel to MongoDB Data Pipeline

<b>Short name:</b> Excel_Pipeline </p>
<b>Role:</b> Data Engineer </p>
<b>Technologies:</b> R, MongoDB, Excel </p>
<b>Tags:</b> Data Extraction, NoSQL Database </p>
<b>Key Tools:</b> Jupyter Notebooks-R, MongoDB Compass, Microsoft Excel </p>
<b>Description:</b> R script that extracts information from a large collaborative Excel file (around 70 columns × 1500 rows, to manage approximately 350 mini projects) and loads it into a structured MongoDB database. The solution maps and transforms data input from around 12 users, maintaining the relationships between data and preserving the process flow structure across multiple stages.

This foundational script sets the groundwork for future implementations:

- Automated data extraction from Excel to MongoDB
- Historical tracking system for all data changes
- Real-time monitoring of process advancement
- Automated notifications for task dependencies
- Performance metrics for task completion times



<b>MongoDB ETL Process Flow:</b>

1. Initialization:
- Load Required Libraries (readxl, openxlsx, mongolite, jsonlite)
- Read Excel Worksheet

2. Data Type Conversion Functions:
- convert_to_date: Excel numeric to date conversion
- convert_to_number: String to numeric conversion
- detect_and_convert: Main type detection and conversion

3. DataFrame Processing:
- Apply type conversions to the entire DataFrame

4. MongoDB Connection:
- Connect to main Dataset Collection
- Connect to Historical Collection
- Fetch existing records
- Create data dictionary for efficient lookups

5. Data Processing:
- Iterate through DataFrame rows
- Process each column
- Check for data changes
- Prepare update operations
- Prepare historical records

6. Database Update:
- Execute batch updates on main collection
- Insert historical records
