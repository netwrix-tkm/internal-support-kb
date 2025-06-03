## Ticket Metadata
- **Ticket ID:** 500Qk00000IevhyIAB
- **Case Number:** 427878
- **Status:** Closed - Resolved
- **Account/Company:** ANWR GROUP eG
- **Contact Name:** Edwin Hamzagic
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Upgrade
- **Version:** Not specified

## Problem Description
The customer reported issues while attempting to roll out a new client software version. They were unable to transfer the old version and required urgent assistance.

## Environment Details
- The issue occurred during a scheduled upgrade attempt for multiple client devices.
- The upgrade process was initiated at 12:30 PM, but by 2:00 PM, no clients had been successfully upgraded.

## Troubleshooting Steps
1. **Initial Inquiry:** The support engineer requested more details about the issue, including any error messages or screenshots.
2. **Client Selection Issue:** The customer reported that they could not select any clients for the upgrade, regardless of licensing status.
3. **Check for Existing Jobs:** The support engineer advised the customer to check for any existing upgrade jobs that might be blocking the selection of clients.
4. **Deletion of Jobs:** The customer deleted existing jobs as instructed but continued to experience issues.
5. **Server Restart:** The customer restarted their on-premises server, which seemed to improve performance slightly but did not resolve the upgrade issue.
6. **Remote Session Setup:** A remote session was proposed to review the installation logs and verify communication.

## Root Cause
The root cause was identified as existing incomplete or failed upgrade jobs that were preventing the selection of clients for the new upgrade. The last upgrade job had completed with failures, which blocked further attempts.

## Solution
The issue was resolved by:
- Instructing the customer to delete all existing upgrade jobs, including those that had failed or were incomplete.
- After the deletion, the customer was able to initiate a new upgrade job successfully.

## Notes
- Ensure that all previous upgrade jobs are cleared before attempting a new upgrade to avoid similar issues.
- It is advisable to monitor the upgrade process closely and check for any failures in the logs to prevent blocking issues in future upgrades.
- Communication with the customer should include clear instructions on how to check for and delete existing jobs to facilitate smoother troubleshooting.