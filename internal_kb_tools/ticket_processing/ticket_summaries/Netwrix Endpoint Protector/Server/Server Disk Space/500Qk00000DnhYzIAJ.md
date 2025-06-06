## Ticket Metadata
- **Ticket ID:** 500Qk00000DnhYzIAJ
- **Case Number:** 416621
- **Status:** Closed - Resolved
- **Account/Company:** Volksoft Consulting Pvt. Ltd
- **Contact Name:** Kantikirit Vuppalanchi
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Disk Space
- **Version:** 5.9.3.0

## Problem Description
The customer reported two main issues with the EPP Server:
1. A popup notification indicating "Disk Space low" upon login.
2. The server backup process appears to generate but stops at 99%.

## Environment Details
- **EPP Server Version:** 5.9.3.0

## Troubleshooting Steps
1. Verified the current disk space usage on the EPP Server.
2. Checked the backup logs for any errors or warnings.
3. Attempted to manually clear up disk space by removing unnecessary files.
4. Restarted the backup service to see if it would complete successfully.
5. Conducted a remote session to further investigate the issue.

## Root Cause
The root cause of the issue was identified as insufficient disk space on the EPP Server, which was preventing the backup process from completing successfully.

## Solution
During a remote session, the support technician:
1. Identified and removed temporary files and old backups that were no longer needed, freeing up sufficient disk space.
2. Restarted the backup process, which then completed successfully without stopping at 99%.

## Notes
- It is recommended to regularly monitor disk space on the EPP Server to prevent similar issues in the future.
- Implementing automated alerts for low disk space could help in proactively managing server resources.