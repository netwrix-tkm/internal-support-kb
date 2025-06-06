## Ticket Metadata
- **Ticket ID:** 500Qk00000OiMbhIAF
- **Case Number:** 443903
- **Status:** Closed - Resolved
- **Account/Company:** College Ave Student Loan
- **Contact Name:** Amir Sardarizadeh
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Windows File Systems
- **Feature:** Access Auditing
- **Version:** 11.5

## Problem Description
The customer reported that many of their reports contained outdated data from servers that had been decommissioned years ago. Specifically, the OpenAccess reports displayed folders and shares that had not existed for over two years. The customer sought assistance in purging this outdated data to ensure the accuracy of their reports.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Collector Code:** StealthAUDIT for Windows File Systems

## Troubleshooting Steps
1. Confirmed that the old decommissioned server data had been removed from the database.
2. Noted that some reports still displayed data with "!Removed" in front of it, indicating potential issues with the FSDropTables job.
3. Advised the client to run the FSDropTables job multiple times to ensure it completed successfully.
4. Requested additional details from the client regarding specific reports and servers still showing "!Removed."
5. Provided the client with knowledge base articles for dropping decommissioned server data:
   - [How to Drop Data for Decommissioned File Servers](https://helpcenter.netwrix.com/bundle/z-kb-articles-salesforce/page/kA0Qk0000001qvpKAA.html)
   - [Running the Drop Host Job](https://helpcenter.netwrix.com/bundle/z-kb-articles-salesforce/page/kA0Qk0000001qxRKAQ.html)

## Root Cause
The issue was primarily caused by residual data from old decommissioned servers still present in the Netwrix Auditor database. The FSDropTables job had not completed successfully, leading to the persistence of outdated data in the reports.

## Solution
The issue was resolved by following the provided knowledge base articles to drop the data associated with the decommissioned servers. The client was instructed to run the drop host job multiple times to ensure all outdated data was purged from the system. After executing these steps, the reports were updated, and the outdated data was successfully removed.

## Notes
- It is essential to ensure that the FSDropTables job completes successfully to avoid similar issues in the future.
- Clients should be encouraged to provide specific examples of reports with issues to facilitate quicker resolution.
- Regular checks and maintenance of the database may help prevent the accumulation of outdated data.