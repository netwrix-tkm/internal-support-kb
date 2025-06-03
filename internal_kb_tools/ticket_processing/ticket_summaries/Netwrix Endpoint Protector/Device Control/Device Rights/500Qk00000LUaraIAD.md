## Ticket Metadata
- **Ticket ID:** 500Qk00000LUaraIAD
- **Case Number:** 434693
- **Status:** Closed - Resolved
- **Account/Company:** Vistec Electron Beam GmbH
- **Contact Name:** Volker Neick
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device Rights
- **Version:** Not specified

## Problem Description
The customer reported that after connecting a USB stick, the server did not recognize the USB device. Additionally, some unregistered USB devices were unblocked, which should have been blocked, indicating that USB device control was not functioning correctly on some computers.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Issue Type:** Unexpected Behavior

## Troubleshooting Steps
1. The customer attempted to restart the server, but this did not resolve the issue.
2. A remote session was scheduled to gather more details and verify the cause of the problem.

## Root Cause
The root cause of the issue was not explicitly identified in the case documentation. However, it was determined that the USB device control feature was malfunctioning, leading to unregistered devices being unblocked.

## Solution
The issue was resolved during the remote session. Specific details of the resolution were not documented, but it involved troubleshooting the USB device control settings and ensuring that the appropriate policies were enforced to block unregistered USB devices.

## Notes
- It is important to regularly verify the configuration of USB device control settings to prevent unauthorized access to unregistered devices.
- Future cases involving USB device recognition issues should include a review of the device control policies and any recent changes to the server or endpoint configurations.