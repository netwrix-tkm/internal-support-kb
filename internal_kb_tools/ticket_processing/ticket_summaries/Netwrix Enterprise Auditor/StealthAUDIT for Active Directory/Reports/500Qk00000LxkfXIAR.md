## Ticket Metadata
- **Ticket ID:** 500Qk00000LxkfXIAR
- **Case Number:** 436009
- **Status:** Closed - Resolved
- **Account/Company:** Shell Information Technology International, Inc.
- **Contact Name:** Brige PG
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Active Directory
- **Feature:** Reports
- **Version:** 11.6

## Problem Description
The customer reported that a report named BT_Billing was not generating correctly, specifically failing to populate its attributes. An error occurred during the execution of the analysis for an attribute called 'Company'.

## Environment Details
- The issue was related to a custom SQL Analysis that involved multiple tables and views in a SQL database.
- The error encountered was: `Ambiguous Column Name: "Company"`.

## Troubleshooting Steps
1. Identified that the SQL task was referencing two or more tables/views that contained a column named "Company".
2. Conducted a meeting with the customer to discuss the issue and gather more information.
3. Modified the SQL query to specify the correct reference for the "Company" column in the SELECT statement.

## Root Cause
The root cause of the issue was the presence of multiple tables/views in the SQL database that had a column with the same name ("Company"). This led to ambiguity in the SQL query, causing the task to fail.

## Solution
To resolve the issue, the SQL query was modified to explicitly target the "Company" column from only one valid table/view. This adjustment eliminated the ambiguity, allowing the SQL task to run successfully.

## Notes
- It is important to ensure that SQL queries are designed to avoid ambiguous column names, especially when referencing multiple tables or views.
- Future custom SQL analyses should be reviewed for potential naming conflicts to prevent similar issues from arising.