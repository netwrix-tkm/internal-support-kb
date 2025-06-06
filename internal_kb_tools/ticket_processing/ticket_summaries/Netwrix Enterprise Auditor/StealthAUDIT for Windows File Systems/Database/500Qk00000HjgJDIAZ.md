```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000HjgJDIAZ
- **Case Number:** 425742
- **Status:** Closed - Resolved
- **Account/Company:** ConocoPhillips Company
- **Contact Name:** Frank McNickle
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Windows File Systems
- **Feature:** Database
- **Version:** 11.5

## Problem Description
During a health call, the customer identified multiple hosts that were no longer in use and requested assistance in purging all records and data related to these offline hosts from their database.

## Environment Details
- The customer is using Netwrix Enterprise Auditor version 11.5.
- The issue involved the management of offline hosts within the database.

## Troubleshooting Steps
1. Created a list of offline hosts that needed to be purged.
2. Developed a custom job named `DropFSHost` in the `zClone_Sandbox` folder to remove data for the offline servers from the file system database tables.
3. Scheduled the job to run when no other File System jobs were active.
4. Monitored the job execution and checked for successful completion.
5. Addressed issues where some jobs were aborted, potentially due to a server reboot.

## Root Cause
The root cause of the issue was the presence of outdated records for decommissioned servers in the database, which needed to be manually purged to maintain an accurate and efficient database.

## Solution
The issue was resolved by:
- Successfully executing the `DropFSHost` job, which removed the data for the identified offline servers.
- Advising the customer to manually remove any remaining entries from the Host Management table to ensure complete removal from all subsequent host lists.

## Notes
- If any entries appear with names like "!REMOVED_{HOSTNAME}", it indicates that the removal did not complete successfully. In such cases, the customer should add these entries back to the `DropFSHost` job host list and re-run the job.
- It is recommended to remove hosts from the master list in the Host Management section to ensure they are deleted from all related lists.
- The customer was advised to monitor the job status and confirm successful removals through the Results > FSAA_Hosts view.
```