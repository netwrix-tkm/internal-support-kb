## Ticket Metadata
- **Ticket ID:** 500Qk00000EhpnFIAR
- **Case Number:** 418652
- **Status:** Closed - Resolved
- **Account/Company:** Chevron Phillips Chemical
- **Contact Name:** John Randolph
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device Rights
- **Version:** EPP Server Version: 5.9.4.0, Agent Version: 6.2.2.2005

## Problem Description
The customer reported that the Endpoint Protector (EPP) device control was not functioning correctly for certain users. Specifically, users were able to use USB devices even when they were not members of the designated Azure security groups that should grant such permissions.

## Environment Details
- The EPP console was hanging, preventing access to accurate server version and OS details.
- The issue involved multiple users across the organization.

## Troubleshooting Steps
1. Reviewed user group memberships and permissions related to device control.
2. Attempted to access the EPP console to gather logs and configuration details, but the console was unresponsive.
3. Enabled debug mode on the agent, but it did not reflect in the agent UI.
4. Upgraded the agent to the latest version available in the console.
5. Used the support tool to gather logs since the debug mode was not enabled during the sync with the server.
6. Cleared the device cache from the backend as per a related Jira ticket (EPPSUPPORT-3630).

## Root Cause
The issue was caused by a caching problem within the EPP system, which allowed users to bypass the intended device control restrictions. This was likely due to stale cache data that did not accurately reflect the current group memberships.

## Solution
The issue was resolved by clearing the device cache from the backend. After this action, the device control functionality returned to normal, and users were no longer able to access USB devices unless they were members of the appropriate Azure security groups.

## Notes
- It is recommended to monitor the device cache regularly and clear it if similar issues arise in the future.
- Ensure that all agents are updated to the latest version to avoid potential compatibility issues.
- If the EPP console becomes unresponsive, consider restarting the service or checking for system resource issues.