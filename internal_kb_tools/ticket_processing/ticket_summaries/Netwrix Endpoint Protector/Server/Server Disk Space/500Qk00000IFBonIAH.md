## Ticket Metadata
- **Ticket ID:** 500Qk00000IFBonIAH
- **Case Number:** 426863
- **Status:** Closed - Resolved
- **Account/Company:** Samsung Electronics Company
- **Contact Name:** Komal Rani
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Disk Space
- **Version:** NONE

## Problem Description
The customer reported that their appliance was running low on disk space, with only 49.68 GB free out of 257.28 GB (19%). They received a warning that the EPP Server functionality and performance may be severely affected due to this low disk space.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Server

## Troubleshooting Steps
1. **Initial Assessment:** The support team reviewed the error message indicating low disk space.
2. **Remote Session Scheduling:** A remote session was proposed to perform a disk cleanup on the EPP Server appliance.
3. **Customer Communication:** Multiple emails were exchanged to schedule the remote session, which was eventually set for November 18, 2024.
4. **Disk Cleanup Execution:** During the remote session, the support engineer performed a disk cleanup to free up space.
5. **Follow-Up:** After the cleanup, the customer was contacted to confirm if the issue was resolved.

## Root Cause
The root cause of the issue was the accumulation of logs and backups that consumed significant disk space on the EPP Server appliance. The customer had not configured log retention policies effectively, leading to excessive storage usage.

## Solution
The issue was resolved by performing a disk cleanup during a scheduled remote session. The support engineer advised the customer to:
- Use the Audit Log Backup feature to manage logs stored in the database.
- Delete older system and audit log backups.
- Tune policies to reduce the incoming log count.
- Implement a log retention policy to keep only one year of logs, which would help prevent similar issues in the future.

## Notes
- It is recommended that customers regularly monitor disk space and configure log retention settings to avoid similar issues.
- Customers should be informed about the importance of managing log data and backups proactively to maintain optimal performance of the EPP Server.