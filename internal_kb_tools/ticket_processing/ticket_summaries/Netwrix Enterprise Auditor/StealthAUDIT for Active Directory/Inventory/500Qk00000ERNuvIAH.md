## Ticket Metadata
- **Ticket ID:** 500Qk00000ERNuvIAH
- **Case Number:** 418132
- **Status:** Closed - Resolved
- **Account/Company:** Federal Home Loan Bank of San Francisco
- **Contact Name:** Nancy Lee
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Active Directory
- **Feature:** Inventory
- **Version:** 11.5

## Problem Description
The customer reported that the scheduled job "2-AD_Changes" was failing with the error message: "Conversion failed when converting character string to smalldatetime data type. Invalid name '#ObjectAdditions'." This issue arose after the database was migrated to a new SQL 2019 server.

## Environment Details
- **Database Server:** SQL Server 2019
- **Product Version:** 11.5
- **Build Number:** 176
- **Location:** California, US

## Troubleshooting Steps
1. Verified the error message received during the execution of the "2-AD_Changes" job.
2. Checked the database migration logs for any discrepancies or issues during the migration process.
3. Attempted to manually run the job to replicate the error.
4. Reviewed the schema of the `SAConfigTbl` to ensure it was correctly configured post-migration.
5. Investigated potential data issues that could lead to conversion errors.

## Root Cause
The root cause of the issue was not definitively identified. However, it was suspected that a bad value in the data may have caused the conversion error, which subsequently aged out and resolved itself.

## Solution
The issue resolved itself without further intervention. It is believed that the problematic data that caused the conversion error had aged out of the system, allowing the scheduled job to run successfully afterward.

## Notes
- Monitor the scheduled jobs after database migrations for any similar issues.
- If similar errors occur, consider checking for data integrity issues or invalid entries that may affect data type conversions.
- Document any recurring issues for further analysis to identify potential patterns or root causes.