## Overview
Collection of data management tools developed within a project management context.  These solutions focus on automating data collection, processing, visualization, analysis and reporting to enhance project tracking and team collaboration efficiency.  Each project maintains confidentiality by using dummy datasets while highlighting core technologies and achievements.</p>
Some projects were developed in parallel in both Python and R, performing the same function. The choice of language depends on the specific working context.

## Projects

### 1. Excel to MongoDB Data Pipeline

<b>Short name:</b> Excel_Pipeline </p>
<b>Role:</b> Data Engineer </p>
<b>Technologies:</b> R, MongoDB, Excel </p>
<b>Tags:</b> Data Extraction, NoSQL Database </p>
<b>Key Tools:</b> Jupyter Notebooks-R, MongoDB Compass, Microsoft Excel </p>
<b>Description:</b> Developed a R script that extracts information from a large collaborative Excel file (around 70 columns × 2700 rows, to manage approximately 350 mini projects) and loads it into a structured MongoDB database. <b>The solution implements a tracking system that captures cell values with timestamps and monitors changes from approximately 11 concurrent users.</b> This approach maintains a complete historical record of modifications, enabling comprehensive audit trails while ensuring data integrity.

This foundational database structure sets the groundwork for future implementations of real-time tracking, historical data analysis, and automated notifications. The MongoDB architecture enables the development of features for data-driven decision making, efficient team coordination through automated task handovers, and comprehensive performance metrics.

### 2. Automated Email Generation

<b>Short name:</b> Email_Merge </p>
<b>Role:</b> Data Automation Developer </p>
<b>Technologies:</b> R, Python, Excel </p>
<b>Tags:</b> Data Processing, Email Automation, Template Generation </p>
<b>Key Tools:</b> Jupyter Notebooks-R, RStudio, VStudio Code, Microsoft Excel </p>
<b>Description:</b> Developed parallel implementations in both Python and R for <b>generating personalized templates in Outlook for corporate email based on structured data inputs.</b> 

The solution customizes content by merging template structures with individual recipient data, enabling efficient mass communication while maintaining personalization.  The system includes a manual verification step to ensure accuracy before dispatch.

### 3. Excel Data Validation

<b>Short name:</b> Data_Validation </p>
<b>Role:</b> Data Automation Developer </p>
<b>Technologies:</b> R, Python, Excel </p>
<b>Tags:</b> Data Validation, Data Extraction, Automated Reporting </p>
<b>Key Tools:</b> Jupyter Notebooks-R, RStudio, VStudio Code, Microsoft Excel </p>
<b>Description:</b> Developed parallel implementations in Python and R to validate the integrity of production data stored in Excel files. The solution compares the structure and content of the production file against a reference file, ensuring that the column names and reference keys have not changed.</b>

If the minimum requirements are met, the system proceeds to extract the production data for further processing and analysis. This automated validation step ensures that downstream data pipelines and reporting processes can reliably consume the production data, reducing the risk of errors or inconsistencies.
