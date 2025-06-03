## Ticket Metadata
- **Ticket ID:** 500Qk00000KaiztIAB
- **Case Number:** 432005
- **Status:** Closed - Resolved
- **Account/Company:** BeeWaTec AG
- **Contact Name:** Alexander Mack
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device Settings
- **Version:** Not specified

## Problem Description
The customer reported that they set the system to allow USB access for an alarm system, but the USB device still did not have access.

## Environment Details
- **Platform:** Netwrix Endpoint Protector

## Troubleshooting Steps
1. Verified the configuration settings for USB access in the Netwrix Endpoint Protector.
2. Checked the Global Rights settings to ensure the USB device was listed.
3. Attempted to modify permissions for the USB device to allow access.

## Root Cause
The issue was caused by the USB device not being explicitly added under the Global Rights settings, which prevented it from being recognized as an allowed device.

## Solution
The issue was resolved by adding the USB device under Global Rights > Specific devices with the allow right. This action granted the necessary permissions for the USB device to function correctly.

## Notes
- Ensure that all USB devices are explicitly added to the Global Rights settings to avoid similar access issues in the future.
- Regularly review device permissions to maintain proper access control and functionality.