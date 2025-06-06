## Ticket Metadata
- **Ticket ID:** 500Qk00000PhxEZIAZ
- **Case Number:** 446513
- **Status:** Closed - Resolved
- **Account/Company:** Alacriti
- **Contact Name:** ravisankar pishini
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Disk Space
- **Version:** Not specified

## Problem Description
The customer reported that the EPP server was occupying excessive disk space and requested assistance to clear some space.

## Environment Details
- The server was running Netwrix Endpoint Protector.
- The root space was reported to be occupied up to 64%, which triggered a server space warning banner.
- Most of the occupied files were located in the `/var/spool` directory.

## Troubleshooting Steps
1. Confirmed the customer's availability for a call to discuss the issue.
2. Reviewed the disk space usage on the server.
3. Identified that the majority of the space was being consumed by files in the `/var/spool` directory.

## Root Cause
The root cause of the disk space issue was not explicitly identified; however, it was noted that the `/var/spool` directory contained a significant number of files contributing to the disk space usage.

## Solution
The issue was resolved by clearing unnecessary files from the `/var/spool` directory, which freed up the required disk space on the EPP server.

## Notes
- It is advisable to regularly monitor disk space usage on the server to prevent similar issues in the future.
- Consider implementing automated cleanup scripts for directories like `/var/spool` to manage disk space more effectively.