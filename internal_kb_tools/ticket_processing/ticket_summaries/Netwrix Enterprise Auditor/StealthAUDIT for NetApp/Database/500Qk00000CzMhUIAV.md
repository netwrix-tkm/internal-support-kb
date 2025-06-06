## Ticket Metadata
- **Ticket ID:** 500Qk00000CzMhUIAV
- **Case Number:** 414859
- **Status:** Closed - Resolved
- **Account/Company:** WellSpan Health
- **Contact Name:** John Masgalas
- **Product:** Netwrix Enterprise Auditor
- **Component:** Database
- **Feature:** Database Maintenance
- **Version:** 11.5

## Problem Description
The customer reported that a SQL job named “DBMaintenancePlan_Index.Subplan_1” failed to complete successfully on their MS SQL Server hosting the StealthAudit database. The failure occurred during its scheduled run, and the logs indicated that the job failed due to a missing index.

## Environment Details
- **Server:** sbitssql01.wellspan.org
- **Database:** StealthAudit
- **Job Failure Time:** 7:38:31 AM on 7/10/2024
- **Error Message:** "Cannot find index 'IDX_SA_ADInventory_Principals_DisplayName'."

## Troubleshooting Steps
1. Reviewed the job logs to identify the error message related to the index.
2. Investigated the SQL Server to confirm if the index “IDX_SA_ADInventory_Principals_DisplayName” existed.
3. Noted that a DROP operation had been performed on the index.
4. Communicated with the DBA team to confirm if the DROP operation was intentional.
5. Suggested monitoring the job for its next scheduled execution.

## Root Cause
The root cause of the job failure was identified as an issue with the TempDB, which prevented the necessary cleanup operations from occurring. Additionally, the missing index was a result of a DROP operation that had been executed on the index, which was not intended.

## Solution
The issue was resolved by cleaning up the TempDB, which allowed the job to complete successfully. The DBA team was also advised to review the index settings and ensure that the necessary indexes were recreated if they were dropped unintentionally.

## Notes
- It is important to monitor SQL jobs closely, especially when they involve critical indexes.
- Future changes to indexes should be documented and communicated to avoid similar issues.
- Ensure that the TempDB is regularly maintained to prevent job failures related to cleanup operations.