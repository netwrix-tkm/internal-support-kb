## Ticket Metadata
- **Ticket ID:** 500Qk00000DnmDhIAJ
- **Case Number:** 416629
- **Status:** Closed - Resolved
- **Account/Company:** Pinsent Masons
- **Contact Name:** Rijay Parmar
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device not recognized
- **Version:** NONE

## Problem Description
The customer reported that a card printer device was showing as offline despite being connected via USB. The Endpoint Protector (EPP) client indicated that the device was blocked, but it was displayed as green in the client interface.

## Environment Details
- The card printer connects via USB.
- The issue was observed in the context of the Netwrix Endpoint Protector platform.

## Troubleshooting Steps
1. Verified the physical connection of the card printer to the USB port.
2. Checked the EPP client settings to confirm the status of the device.
3. Reviewed the device permissions and settings within the EPP client.
4. Attempted to restart the EPP client and reconnect the device.
5. Ensured that the device drivers were up to date and compatible with the system.

## Root Cause
The root cause of the issue was identified as a misconfiguration in the device settings within the EPP client, which led to the device being incorrectly recognized as blocked.

## Solution
The issue was resolved by adjusting the device settings in the EPP client to ensure that the card printer was correctly recognized and allowed. The device was then set to the appropriate permissions, allowing it to function properly.

## Notes
- Ensure that device settings are regularly reviewed to prevent similar issues in the future.
- It is advisable to check for any updates or patches for the EPP client that may address device recognition issues.
- Document any changes made to device settings for future reference and troubleshooting.