## Ticket Metadata
- **Ticket ID:** 500Qk00000EhNirIAF
- **Case Number:** 418623
- **Status:** Closed - Resolved
- **Account/Company:** Hub International Limited
- **Contact Name:** Ebenezer Brew
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device Settings
- **Version:** 5.9.4.0

## Problem Description
The customer reported an issue with reverting to global settings under device control for specific computers. While the global settings applied successfully to some machines, others continued to inherit settings from a different user, despite computer settings having priority.

## Environment Details
- **Server Version:** 5.9.4.0

## Troubleshooting Steps
1. Verified the global settings configuration for the affected computers.
2. Checked the priority of computer settings versus user settings.
3. Attempted to manually reset the settings for the problematic machines.
4. Reviewed logs for any errors or warnings related to settings inheritance.
5. Confirmed that the server version was correctly identified and compatible with the device control features.

## Root Cause
The issue was identified as being caused by custom user settings that were not properly reset to global settings, leading to the inheritance of settings from another user.

## Solution
The issue was resolved by resetting the custom user settings to global for the affected users on the two machines that were experiencing the inheritance problem. This action ensured that the global settings took precedence as intended.

## Notes
- Ensure that custom user settings are regularly reviewed and reset to global settings when necessary to prevent similar issues.
- It may be beneficial to document any specific user settings that could conflict with global settings for future reference.