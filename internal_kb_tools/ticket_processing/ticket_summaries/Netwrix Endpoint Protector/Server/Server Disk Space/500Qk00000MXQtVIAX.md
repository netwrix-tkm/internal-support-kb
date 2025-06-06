## Ticket Metadata
- **Ticket ID:** 500Qk00000MXQtVIAX
- **Case Number:** 437636
- **Status:** Closed - Resolved
- **Account/Company:** Aptitude Software
- **Contact Name:** Dave Young
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Disk Space
- **Version:** Not specified

## Problem Description
The customer reported that the disk space on their server was nearly full, which could potentially lead to performance issues or system failures.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Server

## Troubleshooting Steps
1. Reviewed the current disk space usage on the server.
2. Identified large files and logs that were consuming significant disk space.
3. Cleared unnecessary server logs that were no longer needed.

## Root Cause
The issue was primarily caused by the accumulation of unnecessary server logs, which consumed a substantial amount of disk space over time.

## Solution
The issue was resolved by clearing the server logs that were not needed, thereby freeing up disk space and restoring normal operation.

## Notes
- Regular monitoring of disk space is recommended to prevent similar issues in the future.
- Consider implementing a log rotation policy to manage log files more effectively and avoid excessive disk usage.