## Ticket Metadata
- **Ticket ID:** 500Qk00000EfjfRIAR
- **Case Number:** 418555
- **Status:** Closed - Resolved
- **Account/Company:** Jeeves Group Consultants Ltd.
- **Contact Name:** Frederik Söderberg
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Upgrade
- **Version:** 5.6.0.0

## Problem Description
During a live update on the server, the user encountered the error message: "Database partitions are disabled! Please contact Support for assistance!" The update process halted at 50%.

## Environment Details
- The issue occurred while attempting to upgrade to version 5.6.0.0.
- The update included major user interface improvements and new features such as Context Detection Rules and Debug Logging.

## Troubleshooting Steps
1. Verified the error message displayed during the update process.
2. Checked the server logs for any additional error details.
3. Attempted to restart the update process multiple times, which resulted in the error: "FEHLER: 2 - Number of maximum retries for this update reached, skipping this update..."
4. Assessed the current version of the client software installed on the server.

## Root Cause
The root cause of the issue was identified as an erroneous patch that was included in the update process, which caused the database partitions to be disabled.

## Solution
The erroneous patch was removed, and the upgrade was continued to version 5.8.1.0. This version was chosen because the client had very old versions installed, and upgrading to 5.8.1.0 allowed for a smoother transition and enabled the user to upgrade from the UI.

## Notes
- Ensure that any patches included in future updates are thoroughly tested to prevent similar issues.
- It is advisable to check the compatibility of client versions before initiating an upgrade to avoid complications during the update process.