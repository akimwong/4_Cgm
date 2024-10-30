## Overview
Collection of data management tools developed within a project management context.  These solutions focus on automating data collection, processing, visualization, analysis and reporting to enhance project tracking and team collaboration efficiency.  Each project maintains confidentiality by using dummy datasets while highlighting core technologies and achievements.

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
<b>Description:</b> Developed parallel implementations in both Python and R for <b>generating personalized email templates in Outlook for corporate email based on structured data inputs.</b> The solution creates customized email content by merging template structures with individual recipient data, enabling efficient mass communication while maintaining personalization. The system includes manual verification steps to ensure content accuracy and appropriateness before actual email dispatch.
