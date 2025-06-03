## Ticket Metadata
- **Ticket ID:** 500Qk00000FJJSvIAP
- **Case Number:** 419963
- **Status:** Closed - Resolved
- **Account/Company:** CoreWin Distributor
- **Contact Name:** Danylo Didenko
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device Rights
- **Version:** Not specified

## Problem Description
The customer, PrivatBank, reported an issue where a USB disk drive that was previously allowed to connect to a specific computer was now showing a gray icon in the EPP client UI, indicating that the device was "Disconnected," despite being physically connected.

## Environment Details
- **Device Type:** USB disk drive
- **Client Software:** Netwrix Endpoint Protector (EPP)

## Troubleshooting Steps
1. Verified the device connection status in the EPP client UI.
2. Suggested the customer navigate to Device Control -> Devices -> Filter for the last computer -> locate the device -> click on the actions button -> Manage rights -> set the allow access for the device for the computer and user.
3. Offered to schedule a remote session for further investigation if the issue persisted.

## Root Cause
The root cause was not explicitly identified in the communications, but it was implied that the device rights may have been inadvertently changed or not properly configured, leading to the device being blocked.

## Solution
The issue was resolved by guiding the customer to reconfigure the device rights in the EPP client UI, allowing access for the USB disk drive to the specific computer and user. This action restored the connection and changed the icon from gray to the appropriate status.

## Notes
- Ensure that device rights are regularly reviewed and updated to prevent similar issues in the future.
- If a device that was previously allowed suddenly shows as disconnected, check the device rights settings first before escalating the issue.
- No further feedback was received from the customer after the resolution, indicating satisfaction with the solution provided.