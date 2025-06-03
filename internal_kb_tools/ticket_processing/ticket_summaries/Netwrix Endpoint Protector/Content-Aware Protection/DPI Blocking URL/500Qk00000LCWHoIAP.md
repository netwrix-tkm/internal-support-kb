## Ticket Metadata
- **Ticket ID:** 500Qk00000LCWHoIAP
- **Case Number:** 433932
- **Status:** Closed - Resolved
- **Account/Company:** VentureDive
- **Contact Name:** Afraz Ahmed
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** DPI Blocking URL
- **Version:** NONE

## Problem Description
The customer reported receiving sensitive information notifications after updates to the Netwrix Endpoint Protector, indicating that the Deep Packet Inspection (DPI) settings were not functioning as expected.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Content-Aware Protection
- **Age of the Issue:** 5.0

## Troubleshooting Steps
1. The customer attempted to add port number **59526** to the list of port numbers in the "Content Aware Protection > Deep Packet Inspection" settings.
2. The customer unchecked the "block unsecure connection" option in the DPI settings.

## Root Cause
The issue was likely caused by the DPI settings not being properly configured to handle the specific port number and the blocking of unsecure connections, which interfered with the detection of sensitive information.

## Solution
The issue was resolved by:
- Adding port number **59526** to the DPI settings.
- Unchecking the "block unsecure connection" option, which allowed the DPI to function correctly and stop sending notifications for sensitive information.

## Notes
- Ensure that any necessary port numbers are included in the DPI settings to avoid similar issues in the future.
- Be cautious when modifying security settings such as "block unsecure connection," as this may expose the system to potential vulnerabilities.