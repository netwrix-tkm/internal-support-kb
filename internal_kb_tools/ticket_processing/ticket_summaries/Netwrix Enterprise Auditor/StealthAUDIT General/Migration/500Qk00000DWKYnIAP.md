## Ticket Metadata
- **Ticket ID:** 500Qk00000DWKYnIAP
- **Case Number:** 416032
- **Status:** Closed - Resolved
- **Account/Company:** Westpac Banking Corporation
- **Contact Name:** Mark Chambers
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Migration
- **Version:** 11.5

## Problem Description
The customer, Mark Chambers from Westpac Banking Corporation, requested guidance on migrating their database from a SQL Server 2012 to a SQL Server 2022 while using StealthAudit version 11.5.

## Environment Details
- Current SQL Server: 2012
- Target SQL Server: 2022
- StealthAudit Version: 11.5

## Troubleshooting Steps
1. Reviewed the migration requirements for StealthAudit.
2. Confirmed the compatibility of StealthAudit with SQL Server 2022.
3. Provided guidance on the necessary steps for database migration.
4. Explained the importance of log file retention settings in SAM output.

## Root Cause
The issue stemmed from a lack of clarity on the migration process and the specific steps required to ensure a smooth transition from SQL Server 2012 to SQL Server 2022 while maintaining data integrity and functionality within StealthAudit.

## Solution
The resolution involved providing the customer with detailed steps for the migration process, including:
- Ensuring that the SAM output is configured to retain log files longer than the data from previous backups.
- Utilizing StealthAUDIT to scan the TSV files provided by SAM to restore activity information for any missed days due to rollback.

## Notes
- It is crucial to configure log file retention settings appropriately to avoid data loss during migration.
- Future migrations should always verify compatibility with the current version of StealthAudit and the target SQL Server version to prevent similar issues.