## Ticket Metadata
- **Ticket ID:** 500Qk00000MHHsbIAH
- **Case Number:** 436889
- **Status:** Closed - Resolved
- **Account/Company:** Qast Systems Solutions Inc.
- **Contact Name:** Jessica Zhang
- **Product:** Netwrix Endpoint Protector
- **Component:** System & Log Backups
- **Feature:** System Backup
- **Version:** 5941

## Problem Description
The customer, Huawei, reported that entities such as users and computers could not be exported from the Netwrix Endpoint Protector. Clicking the Export button resulted in no response, and a prompt indicated that the issue might be due to low disk space.

## Environment Details
- The system was functioning correctly until February 15, 2025.
- The issue was reported on February 25, 2025.

## Troubleshooting Steps
1. Verified the disk space on the server hosting the Netwrix Endpoint Protector.
2. Checked for any recent changes or updates that might have affected the export functionality.
3. Reviewed system logs for any errors or warnings related to the export process.
4. Confirmed that the user had the necessary permissions to perform exports.
5. Attempted to replicate the issue in a controlled environment.

## Root Cause
The root cause of the issue was identified as insufficient disk space on the server, which prevented the export process from completing successfully.

## Solution
The issue was resolved by freeing up disk space on the server. This involved:
- Deleting unnecessary files and logs.
- Ensuring that there was adequate space available for the export operations to proceed.

After these actions were taken, the export functionality was restored, and the customer was able to export entities without further issues.

## Notes
- It is important to regularly monitor disk space on servers running Netwrix Endpoint Protector to prevent similar issues in the future.
- Customers should be advised to maintain a buffer of free disk space to accommodate temporary files generated during export operations.