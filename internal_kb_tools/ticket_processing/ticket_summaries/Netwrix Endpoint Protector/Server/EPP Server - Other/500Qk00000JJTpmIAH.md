## Ticket Metadata
- **Ticket ID:** 500Qk00000JJTpmIAH
- **Case Number:** 429395
- **Status:** Closed - Resolved
- **Account/Company:** CoreWin Distributor
- **Contact Name:** Danylo Didenko
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Server
- **Feature:** EPP Server - Other
- **Version:** Not specified

## Problem Description
The customer, PrivatBank, reported an issue where they were unable to download logs from a macOS computer. They encountered an error message stating "File not Found" when attempting to gather logs at 10:31 GMT+2.

## Environment Details
- **Operating System:** macOS
- **Time of Incident:** 10:31 GMT+2

## Troubleshooting Steps
1. Verified the error message "File not Found" during the log download attempt.
2. Inquired if the logs could be searched for on the EPP server backend for alternative download options.
3. Checked the EPP server status and connectivity to the macOS client.
4. Reviewed the log collection settings and permissions on the macOS device.

## Root Cause
The root cause of the issue was identified as a temporary glitch in the log collection process, which resulted in the logs not being available for download at the time of the request.

## Solution
The issue was resolved by temporarily fixing the log collection process on the EPP server. This allowed the logs to become accessible for download again. The customer was advised to retry the download after the fix was applied.

## Notes
- It is recommended to monitor the log collection process regularly to prevent similar issues in the future.
- If the "File not Found" error persists, further investigation into server connectivity and log permissions may be necessary.
- Ensure that the EPP server is updated to the latest version to minimize the occurrence of such glitches.