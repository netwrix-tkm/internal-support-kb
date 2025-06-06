## Ticket Metadata
- **Ticket ID:** 500Qk00000IzsSYIAZ
- **Case Number:** 428562
- **Status:** Closed - Resolved
- **Account/Company:** Bremer Bank
- **Contact Name:** Leslie Lange
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for SQL
- **Feature:** Database
- **Version:** 11.6

## Problem Description
The customer reported that the SQL Solution Set reports contained stale data from SQL Servers that had either been decommissioned or migrated to AWS RDS instances. They requested assistance in removing all SQL tables with stale data and starting fresh with only the active SQL Servers.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Data Collector:** StealthAUDIT for SQL

## Troubleshooting Steps
1. Confirmed the presence of stale data in the SQL Solution Set reports.
2. Discussed the need to remove data from decommissioned or relocated SQL servers.
3. Suggested setting up a remote session for configuration.
4. Provided a step-by-step guide to create a job for removing stale data:
   - Right-click the custom or Jobs folder and select **Create Job**.
   - Navigate to the **Configure** node and select the **Queries** node.
   - Click the **Create Query** button.
   - In the **General** tab, name the query (e.g., **DropSQLHostData**).
   - In the **Data Source** tab, select **SQL** from the Data Collectors dropdown menu.
   - Click **Configure** to launch the SQL Data Collector Configuration Wizard.
   - On the **Category** page, select **Utilities > Remove Storage Tables** under the appropriate database type.
   - Run the job.

## Root Cause
The issue was caused by the presence of stale data in the SQL Solution Set reports due to the decommissioning or relocation of SQL Servers, which were not automatically removed from the reporting system.

## Solution
The issue was resolved by creating a job that utilized the SQL Data Collector Configuration Wizard to remove all collected SQL data for the decommissioned SQL Servers. The job was successfully executed, clearing the stale data and allowing the customer to start fresh with only the active SQL Servers.

## Notes
- It is important to regularly review and clean up SQL data to prevent the accumulation of stale data, especially after server decommissioning or migration.
- Ensure that any jobs created for data removal are tested in a non-production environment before execution in production to avoid unintended data loss.