## Ticket Metadata
- **Ticket ID:** 500Qk00000KaLTpIAN
- **Case Number:** 431976
- **Status:** Closed - Resolved
- **Account/Company:** Sodexo
- **Contact Name:** Vignesh Haldankar
- **Product:** Netwrix Endpoint Protector
- **Component:** System & Log Backups
- **Feature:** Audit Log Backup
- **Version:** Not specified

## Problem Description
The customer reported an issue where they were unable to download logs, receiving the error message: "File not found. File shadow upload is in progress. Please retry later." This indicated a problem with the shadow files not being generated on the server or visible in the user interface.

## Environment Details
- The issue was encountered in the Netwrix Endpoint Protector environment.
- The customer was using a system that required log backups and shadow file management.

## Troubleshooting Steps
1. Investigated the status of shadow files on the server.
2. Verified the file hash for a test file transfer in the database.
3. Scheduled remote sessions to gather more information and assist the customer.
4. Collected client logs and checked the shadow file directory permissions.
5. Suggested changing the ownership of the shadow file directory to ensure proper file uploads.

## Root Cause
The root cause of the issue was identified as improper ownership of the shadow file directory. The directory was owned by `root` instead of `www-data`, which prevented the shadow files from being uploaded to the server. Additionally, the shadow file upload process has a waiting period, during which the error message is displayed.

## Solution
The issue was resolved by changing the ownership of the shadow file directory using the following command:
```bash
chown www-data:www-data /var/eppfiles/shadows/
```
After this change, the customer was advised to wait for the shadow file upload process to complete before attempting to download the logs again. Once the ownership was corrected and the appropriate waiting period was observed, the logs became downloadable without errors.

## Notes
- It is important to ensure that the ownership of the shadow file directory is set correctly to avoid similar issues in the future.
- The shadow file upload process may take longer than 30 minutes, and users should be aware of this waiting period before concluding that there is an error.
- Future troubleshooting should include checking directory permissions and ownership as a first step when encountering similar issues with log downloads.