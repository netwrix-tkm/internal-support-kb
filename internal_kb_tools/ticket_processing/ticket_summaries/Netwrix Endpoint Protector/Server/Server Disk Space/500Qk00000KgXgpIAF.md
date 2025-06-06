## Ticket Metadata
- **Ticket ID:** 500Qk00000KgXgpIAF
- **Case Number:** 432383
- **Status:** Closed - Resolved
- **Account/Company:** Asia Bank
- **Contact Name:** Danylo Didenko
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Disk Space
- **Version:** Not specified

## Problem Description
The customer, Asia Bank, reported receiving a critical low disk space notification, indicating that only 7% of available disk space remained on their server.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Server

## Troubleshooting Steps
1. A remote session was scheduled to assess the disk space issue.
2. Old shadow copies were identified as taking up significant disk space.
3. The old shadows were deleted to free up disk space.

## Root Cause
The low disk space issue was primarily caused by the accumulation of old shadow copies, which were consuming a substantial amount of disk space.

## Solution
The issue was resolved by deleting the old shadow copies, which successfully freed up sufficient disk space on the server, alleviating the critical low disk space notification.

## Notes
- It is advisable to regularly monitor disk space and manage shadow copies to prevent similar issues in the future.
- Consider implementing automated alerts for low disk space to proactively address potential problems before they escalate.