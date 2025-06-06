## Ticket Metadata
- **Ticket ID:** 500Qk00000NLFwWIAX
- **Case Number:** 439997
- **Status:** Closed - Resolved
- **Account/Company:** Porsche Cars GB Ltd
- **Contact Name:** Richard Ward
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Windows File Systems
- **Feature:** Configuration
- **Version:** 11.6.0.137

## Problem Description
The Create Schema job fails with the error message: "Column A is not the same data type as referencing column B in foreign Key X. Could not create constraint or index." This issue arose after upgrading from version 11.5.0.200 to 11.6.0.137.

## Environment Details
- The customer was using Netwrix Enterprise Auditor version 11.5.0.200 before the upgrade.
- The issue was specifically related to the Create Schema job within the File System solution.

## Troubleshooting Steps
1. **Reproduce the Issue:**
   - Confirmed the issue by running the Create Schema job after the upgrade.
   - Collected logs showing the specific errors related to data type mismatches in foreign keys.

2. **Attempted Migrate Schema:**
   - Ran the Migrate Schema instant job to update data types for relevant tables and views.
   - Encountered errors indicating conflicts with foreign key constraints.

3. **Repair Maintenance Task:**
   - Executed a repair maintenance task from the FSAA System Scan query for all active hosts.
   - The repair took approximately 7 hours and indicated changes were made.

4. **Re-ran Create Schema Job:**
   - After the repair, the Create Schema job was restarted, resulting in different error messages related to missing foreign keys.

5. **Checked Table Structures:**
   - Verified that the SA_FSAC_DailyActivity and SA_FSAC_ActivityEvents tables did not have the expected foreign keys.

6. **Executed SQL Queries:**
   - Ran SQL queries to identify any hosts in the SA_FSAA_Resources table that were not present in the Hosts table.

## Root Cause
The root cause of the issue was identified as missing foreign keys in the ActivityEvents and DailyActivity tables, which were expected to reference the Hosts table. This inconsistency arose due to data manipulation or corruption prior to the upgrade, leading to invalid states in the database.

## Solution
To resolve the issue:
1. The development team provided SQL queries to delete records referencing invalid host IDs (24, 25, 27) from the SA_FSAC_ActivityEvents and SA_FSAC_DailyActivity tables.
2. The following SQL commands were executed:
   ```sql
   DELETE FROM SA_FSAC_ActivityEvents WHERE HOST IN (24, 25, 27);
   DELETE FROM SA_FSAC_DailyActivity WHERE HOST IN (24, 25, 27);
   ```
3. After executing the delete commands, the Migrate Schema job was run again, followed by the Create Schema job, which completed successfully without errors.

## Notes
- It is crucial to ensure that all foreign key relationships are intact before performing upgrades or schema migrations.
- Future upgrades should be preceded by a thorough check of the database integrity to prevent similar issues.
- If encountering similar errors, verify the existence of foreign keys and the integrity of referenced tables before proceeding with schema operations.