## Ticket Metadata
- **Ticket ID:** 500Qk00000FoFhbIAF
- **Case Number:** 421088
- **Status:** Closed - Resolved
- **Account/Company:** PSI CRO AG
- **Contact Name:** Jovan Salsone
- **Product:** Netwrix Endpoint Protector
- **Component:** EasyLock / Enforced Encryption
- **Feature:** EasyLock - Other
- **Version:** NONE

## Problem Description
The customer reported that after deploying EasyLock to a USB device and setting up a password, they were able to log in and interact with the device without entering the required credentials.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Feature in Use:** EasyLock

## Troubleshooting Steps
1. Verified the deployment of EasyLock on the USB device.
2. Checked the configuration settings for password enforcement.
3. Attempted to replicate the issue on different USB devices.
4. Reviewed the EasyLock documentation for any known issues or misconfigurations.
5. Applied Procedure 65 as a potential fix.

## Root Cause
The issue was identified as a misconfiguration in the EasyLock settings that allowed access to the USB device without proper credential verification.

## Solution
The issue was resolved by applying Procedure 65, which involved reconfiguring the EasyLock settings to ensure that password enforcement was correctly implemented. This adjustment ensured that users must enter the correct credentials to access the USB device.

## Notes
- Ensure that all EasyLock configurations are thoroughly reviewed after deployment to prevent similar issues.
- It is recommended to test the configuration on multiple devices to confirm that the settings are enforced correctly.
- Document any changes made during troubleshooting for future reference.