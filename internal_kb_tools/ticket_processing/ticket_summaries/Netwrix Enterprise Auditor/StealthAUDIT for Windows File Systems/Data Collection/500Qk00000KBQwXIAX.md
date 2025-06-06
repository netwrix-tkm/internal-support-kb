## Ticket Metadata
- **Ticket ID:** 500Qk00000KBQwXIAX
- **Case Number:** 431108
- **Status:** Closed - Resolved
- **Account/Company:** Point32Health Services, Inc.
- **Contact Name:** Peter Sterianos
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Windows File Systems
- **Feature:** Data Collection
- **Version:** 11.6

## Problem Description
The customer reported an error during the scan portion of the filesystem Activity collection job in Netwrix Enterprise Auditor. The error message indicated an inability to read data from the transport connection, stating: "Error getting scan database from execution host: Unable to read data from the transport connection: The connection was closed."

## Environment Details
- The issue occurred after an upgrade to version 11.6 of Netwrix Enterprise Auditor on February 6, 2025.
- The filesystem activity jobs were running on hosts IS-TEST and IS-FS2, which were feeding through a proxy server.

## Troubleshooting Steps
1. Analyzed log files to identify the source of the error, which indicated an issue with the Tier 2 database.
2. Deleted old temporary files (*.tmp) and junk files with fabricated extensions from the proxy server directories for IS-TEST and IS-FS2.
3. Renamed the directories for IS-TEST and IS-FS2 to allow new directories to be created on the next run.
4. Deleted any "*Failed.zip" files in the relevant directories.
5. Confirmed that adequate disk space was available on the proxy server.
6. Scheduled follow-up tests to monitor the execution of the filesystem activity jobs.

## Root Cause
The root cause of the issue was identified as a problem with the Tier 2 database, likely exacerbated by the presence of old temporary files and junk files on the proxy server, which could have interfered with the data transport connection.

## Solution
The issue was resolved by performing the following actions:
- Cleaning up the proxy server by deleting old temporary and junk files.
- Renaming the existing directories for IS-TEST and IS-FS2 to ensure new directories would be created during the next job run.
- Deleting any failed job files to prevent conflicts during the execution of new jobs.
- After these actions, the customer was advised to retest the filesystem activity job once they were caught up with other jobs.

## Notes
- It is important to regularly clean up temporary and junk files on the proxy server to prevent similar issues in the future.
- Monitoring the Event Viewer during filesystem activity scans may provide additional insights into any underlying issues that arise.
- Ensure that the Tier 2 databases are synchronized and up-to-date to avoid discrepancies that could lead to scanning failures.