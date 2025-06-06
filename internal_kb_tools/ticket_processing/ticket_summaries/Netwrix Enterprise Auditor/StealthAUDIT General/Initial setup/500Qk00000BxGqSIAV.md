```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000BxGqSIAV
- **Case Number:** 412145
- **Status:** Closed - Resolved
- **Account/Company:** NIC Inc
- **Contact Name:** Bobby Williams
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Initial setup
- **Version:** 11.5

## Problem Description
The customer reported errors while attempting to perform database scans on two Oracle hosts. Although the connection was established successfully, the job failed with errors related to SQL key constraints.

## Environment Details
- **Oracle Hosts:** 
  - ETS-VAPRD-ODA0.CDC.NICUSA.COM
  - ETS-VADEV-ODA0.CDC.NICUSA.COM
- **Scan Type:** 1-Oracle_PermissionsScan

## Troubleshooting Steps
1. Verified the connection to the Oracle hosts, which showed access granted.
2. Inspected error messages indicating a violation of the UNIQUE KEY constraint 'SA_Oracle_Parameters_Id'.
3. Discussed potential solutions, including deleting the SA_Oracle_Parameters table and removing associated functions.
4. Identified duplicate entries under the `sa_database_id` column in the database.
5. Removed the duplicate entries and reran the Oracle permissions scan.

## Root Cause
The issue was caused by duplicate entries in the `sa_database_id` column of the `SA_Oracle_Parameters` table, which led to violations of the UNIQUE KEY constraint during the database scan.

## Solution
The duplicates were removed from the `sa_database_id` column, and the Oracle permissions scan was successfully rerun without errors following this correction.

## Notes
- Ensure to monitor for duplicate entries in the `SA_Oracle_Parameters` table in future setups to prevent similar issues.
- Regular database maintenance and checks can help identify and resolve such issues proactively.
```