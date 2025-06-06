## Ticket Metadata
- **Ticket ID:** 500Qk00000EkDocIAF
- **Case Number:** 418739
- **Status:** Closed - Resolved
- **Account/Company:** Hughes Federal Credit Union
- **Contact Name:** Zach Metz
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Upgrade
- **Version:** 5.9.3.0

## Problem Description
The customer reported that a scheduled update to version 5.9.4.0 for their server did not execute as planned. Despite scheduling the update twice, the server remained on version 5.9.3.0.

## Environment Details
- **Current Server Version:** 5.9.3.0
- **Scheduled Update Version:** 5.9.4.0
- **Scheduled Times:** 
  - First attempt: Monday at 7 PM MST
  - Second attempt: Tuesday at 6 PM MST

## Troubleshooting Steps
1. Verified the scheduled update status on the server.
2. Checked for any error messages or logs related to the update process.
3. Confirmed that the "Cancel Schedule" button was still present, indicating the update was not processed.
4. Attempted to reschedule the update multiple times without success.

## Root Cause
The root cause of the issue was not explicitly identified during the troubleshooting process. However, it was determined that the scheduled update did not trigger the installation process on the server.

## Solution
The issue was resolved by manually upgrading the EPP server to version 5.9.4.0. This involved executing the update process directly rather than relying on the scheduled task.

## Notes
- Ensure to monitor the scheduled updates closely and verify their execution status after scheduling.
- If similar issues arise, consider performing a manual upgrade if the scheduled updates fail to execute.
- Document any error messages or logs that may provide insight into why scheduled updates do not complete successfully for future reference.