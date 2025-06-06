## Ticket Metadata
- **Ticket ID:** 500Qk00000GHklEIAT
- **Case Number:** 422178
- **Status:** Closed - Resolved
- **Account/Company:** SACRED BYTES
- **Contact Name:** Chandeep Chandeep
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Disk Space
- **Version:** NONE

## Problem Description
The customer reported a disk space issue, receiving a warning message in the Live Update stating, "Your Appliance is running low on Disk Space." The server was operating at 81% of its 40 GB capacity.

## Environment Details
- **Server Capacity:** 32 GB (actual usage at 81% of 40 GB)
- **Product Version:** Not specified
- **Build Number:** 5940

## Troubleshooting Steps
1. Reviewed the warning message in Live Update regarding low disk space.
2. Consulted the article on upgrade prerequisites which indicated contacting customer support if disk space exceeds 70%.
3. Assessed the current disk space usage on the server.

## Root Cause
The issue was caused by the server's disk space being utilized beyond the recommended threshold of 70%, leading to the warning message.

## Solution
The issue was resolved by increasing the disk space on the server, which alleviated the low disk space warning.

## Notes
- It is advisable to monitor disk space regularly to prevent similar issues in the future.
- Consider implementing alerts for disk space usage to proactively manage server resources.