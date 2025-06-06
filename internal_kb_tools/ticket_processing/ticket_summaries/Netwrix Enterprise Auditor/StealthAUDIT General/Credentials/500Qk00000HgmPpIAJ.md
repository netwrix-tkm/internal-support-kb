## Ticket Metadata
- **Ticket ID:** 500Qk00000HgmPpIAJ
- **Case Number:** 425584
- **Status:** Closed - Resolved
- **Account/Company:** KS StateBank
- **Contact Name:** James Stevens
- **Product:** Netwrix Enterprise Auditor
- **Component:** File System Monitoring
- **Feature:** Credentials
- **Version:** 11.5

## Problem Description
The customer reported that the file system monitoring was not functioning properly, with discrepancies in permissions when compared to the folder permissions on the server. This issue was linked to the Bulk Import functionality not operating as expected.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Collector Code:** StealthAUDIT General
- **Age of the Product:** 5.1 years

## Troubleshooting Steps
1. Reviewed the File System Scan and Bulk Import during a meeting with the customer.
2. Identified issues with the Bulk Import scan.
3. Reset the host data and rescanned the Bulk Import.
4. Instructed the customer to run the File System scan (FSAA) and then rerun the Bulk Import.
5. Suggested enabling Debug Logging and collecting logs from specified locations for further analysis.
6. Planned to delete the T2 database and rerun the Permission scan if the error "T2 database does not match the T1 database" persisted.

## Root Cause
The root cause of the issue was identified as a malfunction in the Bulk Import process, which was preventing accurate permission comparisons between the Netwrix system and the actual folder permissions on the server.

## Solution
The issue was resolved by performing the following steps:
1. Expanded the Bulk Import settings.
2. Navigated to Configure and Query Properties.
3. Under Query Selection, clicked on Maintenance.
4. Selected Repair, chose the host, and executed the Repair function.

After these steps, the Bulk Import functionality was restored, and the file system monitoring began to reflect the correct permissions.

## Notes
- It is important to monitor the Bulk Import functionality regularly to ensure it is operating correctly, as discrepancies in permissions can lead to security risks.
- If similar issues arise in the future, consider resetting host data and performing a Repair on the Bulk Import settings as initial troubleshooting steps.