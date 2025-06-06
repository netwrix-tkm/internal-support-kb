```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000NVnaHIAT
- **Case Number:** 440447
- **Status:** Closed - Resolved
- **Account/Company:** Genius Consultants Limited
- **Contact Name:** Saikat Banerjee
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Disk Space
- **Version:** Not specified

## Problem Description
The customer reported a storage issue on their server, requesting assistance to clean up space.

## Environment Details
The server is hosted on AWS, and the customer was using the Netwrix Endpoint Protector platform.

## Troubleshooting Steps
1. Established remote connection with the customer, Saikat Banerjee.
2. Explained two options for resolving the storage issue:
   - Adjust the system backup to retain logs older than 1 month instead of 4 months.
   - Increase the disk space size by contacting their account manager.
3. Adjusted the system backup settings to take logs older than 1 month.
4. Scheduled a follow-up to check if the space was cleared after the backup ran.

## Root Cause
The server was retaining logs older than 4 months, which were consuming unnecessary disk space. The logs did not contain relevant data, leading to inefficient use of storage.

## Solution
The issue was resolved by adjusting the backup settings to retain only logs older than 1 month. This change allowed the server to clear up space effectively.

## Notes
- It is recommended to regularly review and adjust backup settings to prevent similar storage issues in the future.
- Customers should be informed about the importance of managing log retention policies to optimize disk space usage.
```