## Ticket Metadata
- **Ticket ID:** 500Qk00000CJGetIAH
- **Case Number:** 413042
- **Status:** Closed - Resolved
- **Account/Company:** Better World Technology Private Limited / Directi Group
- **Contact Name:** Shoeb Amin
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Client - Other
- **Feature:** Notification for blocked devices
- **Version:** NONE

## Problem Description
The customer reported that when a device is blocked for a user, the user is unable to see any logs indicating when it was blocked or under what policy it was blocked. They requested assistance in enabling this feature for clients.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Client

## Troubleshooting Steps
1. Confirmed that logs related to devices should be visible in "Reports and Analysis > Log Reports".
2. Asked the customer to check if the logs were present in the specified location.
3. Suggested updating the policies on the EPP client and checking if the notification icon was blinking.
4. Instructed the customer to enable "Notifications Pop-up" under "Device Control > Global Settings".

## Root Cause
The root cause identified was that users do not have access to view logs of blocked devices directly on their computers. The logs are only available on the EPP server.

## Solution
The issue was resolved by informing the customer that users cannot see logs of blocked devices on their local machines. Instead, they can only access logs through the EPP server. The support engineer also guided the customer to enable pop-up notifications to provide users with details about blocked devices.

## Notes
- Users will not be able to see logs of blocked devices on their local machines; all logs are stored on the EPP server.
- Enabling pop-up notifications can help users receive immediate updates regarding blocked devices and policies.