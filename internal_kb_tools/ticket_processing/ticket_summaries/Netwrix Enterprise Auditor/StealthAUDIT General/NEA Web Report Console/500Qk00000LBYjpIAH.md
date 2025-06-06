## Ticket Metadata
- **Ticket ID:** 500Qk00000LBYjpIAH
- **Case Number:** 433902
- **Status:** Closed - Resolved
- **Account/Company:** Horizon Media
- **Contact Name:** Angelo DiPietro
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** NEA Web Report Console
- **Version:** 11.5.0.160

## Problem Description
The customer reported an issue with generating a report that displays the age of files on their file shares. They encountered a limitation on the number of rows being generated, preventing them from obtaining a complete report.

## Environment Details
- **Product Version:** Netwrix Enterprise Auditor (NEA) 11.5.0.160
- **Data Size:** The report was querying a table with over 4.2 million rows.

## Troubleshooting Steps
1. Reviewed the custom report (FileSystem_Aging) to understand the data being queried.
2. Adjusted the Export, Max Row limit, and Grid Filter options to attempt to increase the number of rows returned.
3. Consulted the Netwrix help documentation for guidance on report generation limits.
4. Noted that reports cannot exceed 1 million rows, as they will fail to load.
5. Suggested running a more restrictive SQL query using SQL Server Management Studio (SSMS) to filter the data before exporting.

## Root Cause
The issue was caused by the inherent limitation in the reporting tool, which restricts the number of rows that can be generated in a report to a maximum of 1 million. The customer's query was attempting to process a significantly larger dataset without appropriate filtering.

## Solution
The issue was resolved by:
- Adjusting the report settings to manage the row limits effectively.
- Utilizing SQL Server Management Studio (SSMS) to run a more restrictive query with appropriate WHERE clauses to filter the data before exporting it to CSV.

## Notes
- Reports with limits larger than the default may slow down the run time.
- For future reference, always ensure that queries are optimized to stay within the row limits to avoid loading issues.
- Consider using SSMS for complex queries that require extensive filtering to manage large datasets effectively.