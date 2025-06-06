## Ticket Metadata
- **Ticket ID:** 500Qk00000OOwEkIAL
- **Case Number:** 443047
- **Status:** Closed - Resolved
- **Account/Company:** AGS Health Inc.
- **Contact Name:** Mahesh P
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Access Error
- **Version:** NONE

## Problem Description
The customer reported an inability to log into the web portal and server, receiving an error message indicating that the server took too long to respond.

## Environment Details
- **Server URL:** [dlp-linux.agshealth.com](https://dlp-linux.agshealth.com)
- **Error Message:** "Hmmm… can't reach this page. dlp-linux.agshealth.com took too long to respond."

## Troubleshooting Steps
1. Customer checked the connection.
2. Customer checked the proxy and firewall settings.
3. Technical support suggested a remote connection to further investigate the issue.
4. A remote session was conducted to analyze the server's status.

## Root Cause
The issue was identified as a problem with the inodes count on the Linux server, which was causing the server to be inaccessible.

## Solution
The issue was resolved by running the following command on the server:
```bash
e2fsck -f -y
```
This command checked and fixed the filesystem, restoring access to the server.

## Notes
- Ensure regular monitoring of inode usage on Linux servers to prevent similar issues in the future.
- It is advisable to perform filesystem checks periodically, especially after unexpected server behavior or downtime.