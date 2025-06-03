## Ticket Metadata
- **Ticket ID:** 500Qk00000KqFymIAF
- **Case Number:** 432860
- **Status:** Closed - Resolved
- **Account/Company:** Airpak
- **Contact Name:** Stefania Oltean
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** 8.1

## Problem Description
The customer inquired whether Netwrix Endpoint Protector (EPP) could block and identify hacking devices, specifically Flipper Zero and Raspberry Pi, as part of a tender document.

## Environment Details
- The inquiry pertains to the capabilities of the Netwrix Endpoint Protector in a data center environment.

## Troubleshooting Steps
1. Reviewed the capabilities of the EPP agent regarding device detection.
2. Confirmed that devices detected by the EPP agent would appear in the EPP Notifier application.
3. Investigated potential detection of devices on Windows, noting they may appear as "Teensee Board Device," "Keyboard Device," or "USB Modem."
4. Discussed the possibility of submitting a ticket for further detection capabilities, including logs and registry exports.

## Root Cause
The inability to block or identify Flipper Zero and Raspberry Pi devices is due to the fact that these devices are not inherently detected by the EPP agent unless they are recognized as specific device types.

## Solution
The resolution was to inform the customer that unless the Flipper Zero and Raspberry Pi devices are detected by the EPP agent, they cannot be blocked. If detection is required, the customer can submit a ticket with logs and registry exports for further assistance.

## Notes
- It is important to note that certain devices using the UART protocol may not be controllable by EPP due to operating system restrictions (e.g., macOS).
- Future inquiries regarding device detection should include specific details about the devices in question and any relevant logs to facilitate troubleshooting.