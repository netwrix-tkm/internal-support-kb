## Ticket Metadata
- **Ticket ID:** 500Qk00000FoIabIAF
- **Case Number:** 421087
- **Status:** Closed - Resolved
- **Account/Company:** Dew Solutions Pvt Ltd
- **Contact Name:** Bhogendra Kumar
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Other
- **Version:** NONE

## Problem Description
The customer reported a disk space issue on their appliance, indicating that the available disk space had dropped to 6.88 GB out of a total of 19.52 GB (approximately 35% free). They were warned that the functionality and performance of the EPP Server could be severely affected due to low disk space.

## Environment Details
- **Appliance Type:** Netwrix Endpoint Protector
- **Current Disk Space:** 6.88 GB free from 19.52 GB total

## Troubleshooting Steps
1. Advised the customer to use the Audit Log Backup feature to reduce the logs stored in the database.
2. Suggested deleting older system and audit log backups to free up space.
3. Recommended tuning policies to reduce the incoming log count.

## Root Cause
The root cause of the issue was identified as insufficient disk space due to the accumulation of logs and backups over time, which was not being managed effectively.

## Solution
The issue was resolved by implementing the following actions:
- The customer utilized the Audit Log Backup feature to clear out unnecessary logs.
- Older system and audit log backups were deleted to free up additional disk space.
- Policies were tuned to limit the volume of incoming logs, thereby preventing future occurrences of low disk space.

## Notes
- It is important for customers to regularly monitor disk space and manage log retention settings to avoid similar issues in the future.
- Consider setting up alerts for low disk space to proactively address potential performance impacts.