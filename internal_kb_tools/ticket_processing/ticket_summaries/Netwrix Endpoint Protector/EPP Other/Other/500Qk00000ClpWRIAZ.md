## Ticket Metadata
- **Ticket ID:** 500Qk00000ClpWRIAZ
- **Case Number:** 414272
- **Status:** Closed - Resolved
- **Account/Company:** LayaTech
- **Contact Name:** Dinakaran
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Other
- **Version:** Not specified

## Problem Description
The customer reported that their EEP web console displayed a pop-up message indicating that the appliance was running low on disk space, with only 5.82 GB free from a total of 40.69 GB (14%). The message warned that the EPP server's functionality and performance could be severely affected.

## Environment Details
- The EPP server is hosted on AWS cloud.
- The server has a total disk space of 40.69 GB.

## Troubleshooting Steps
1. Customer was advised to use the Audit Log Backup feature to reduce the logs stored in the database.
2. Suggested deleting older system and audit log backups.
3. Recommended tuning policies to reduce the incoming log count.
4. Requested a screenshot from the server UI > Appliance - System Information to assess disk usage.
5. Discussed increasing the disk space due to the presence of large shadow files.
6. Conducted a remote session to review the server's disk space and logs.

## Root Cause
The root cause of the issue was identified as insufficient disk space on the EPP server, primarily due to the accumulation of shadow files and logs. The server's total disk space was inadequate for the operational needs, especially with 200 active licenses.

## Solution
1. The customer was instructed to clear up shadow files, which resulted in freeing approximately 4 GB of space.
2. It was recommended that the customer set up an Audit Log Backup to manage log retention effectively.
3. The customer was advised to consider increasing the disk space by an additional 50-100 GB to accommodate future growth and prevent similar issues.
4. A follow-up call was scheduled to discuss further actions after the disk space increase.

## Notes
- The customer indicated that increasing disk space incurs additional charges, which may limit their options.
- It is crucial to set up an external storage server for log management to avoid space issues in the future, especially given the current low disk capacity of 41 GB.