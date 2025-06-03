## Ticket Metadata
- **Ticket ID:** 500Qk00000FaeskIAB
- **Case Number:** 420614
- **Status:** Closed - Resolved
- **Account/Company:** Velocity Global
- **Contact Name:** William Kuang
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** DPI - Other
- **Version:** Not specified

## Problem Description
The customer reported issues with ConnectWise ScreenConnect when Data Loss Prevention (DPI) was enabled. Although the application could be opened, users were unable to view and remotely control the computer.

## Environment Details
- **DPI Setting:** Enabled
- **Application:** ConnectWise ScreenConnect
- **Exceptions:** Application added to Advanced Scanning Exceptions

## Troubleshooting Steps
1. Verified that ConnectWise ScreenConnect was added to the Advanced Scanning Exceptions.
2. Attempted to run the application with DPI enabled to replicate the issue.
3. Checked for any additional settings or configurations that might affect the application's functionality.

## Root Cause
The issue was caused by the DPI settings interfering with the functionality of ConnectWise ScreenConnect, preventing remote viewing and control capabilities.

## Solution
The issue was resolved by implementing a DPI Allowlist and bypassing DPI for the ConnectWise ScreenConnect application. This adjustment allowed the application to function correctly without interference from the DPI settings.

## Notes
- Ensure that any critical applications requiring remote access are added to the DPI Allowlist to prevent similar issues in the future.
- Regularly review and update the Advanced Scanning Exceptions to accommodate any new applications or updates that may be affected by DPI settings.