## Ticket Metadata
- **Ticket ID:** 500Qk00000EReNtIAL
- **Case Number:** 418136
- **Status:** Closed - Resolved
- **Account/Company:** Pronto
- **Contact Name:** Jason Kidd
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Windows File Systems
- **Feature:** Custom Reports
- **Version:** 11.6

## Problem Description
The customer reported that after reinstalling Netwrix Enterprise Auditor version 11.6 on their server, they were unable to add the "Last Modified" column to the Sensitive Data ShareDetails table in their custom report.

## Environment Details
- **Product Version:** 11.6
- **Collector Code:** StealthAUDIT for Windows File Systems

## Troubleshooting Steps
1. Verified the installation of Netwrix Enterprise Auditor 11.6.
2. Checked the existing custom report configuration for the "Last Modified" column.
3. Attempted to manually add the "Last Modified" column to the Sensitive Data ShareDetails table.
4. Reviewed SQL views associated with the report to identify any discrepancies.

## Root Cause
The issue was caused by the loss of the custom "Last Modified" column in the report after the self-upgrade to version 11.6. The upgrade process did not retain the previous custom configurations.

## Solution
The issue was resolved by creating a new SQL view that joined the `SA_FS_DLPResults_ShareDetails` and `SA_FS_CleanupView` tables. This allowed the "Last Modified" column to be successfully added back to the "Share details" report. After the SQL view creation, the report was republished, which restored the functionality.

## Notes
- It is important to back up custom reports and configurations before performing upgrades to avoid loss of customizations.
- Future upgrades should be tested in a staging environment to ensure that custom configurations are preserved.