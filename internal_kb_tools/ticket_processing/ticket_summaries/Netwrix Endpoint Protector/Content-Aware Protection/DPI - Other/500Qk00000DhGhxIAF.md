## Ticket Metadata
- **Ticket ID:** 500Qk00000DhGhxIAF
- **Case Number:** 416382
- **Status:** Closed - Resolved
- **Account/Company:** Solar Atmospheres, Inc.
- **Contact Name:** Mike Zeigler
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** DPI - Other
- **Version:** Not specified

## Problem Description
The customer reported that after enabling SSL Inspection on their Fortigate device, the local certificate used was causing the Netwrix Endpoint Protector to bypass Deep Packet Inspection (DPI) on all websites. The customer needed assistance to ensure that Endpoint Protector could function correctly with the SSL inspection process.

## Environment Details
- **Device:** Fortigate firewall
- **Security Feature:** SSL Inspection
- **Endpoint Protection Software:** Netwrix Endpoint Protector

## Troubleshooting Steps
1. Verified the configuration of SSL Inspection on the Fortigate device.
2. Checked the local certificate settings to ensure they were correctly implemented.
3. Reviewed the Endpoint Protector settings to identify any misconfigurations.
4. Attempted to adjust DPI settings to see if they could be made compatible with the SSL Inspection.

## Root Cause
The issue was identified as being caused by the local certificate used for SSL Inspection, which was not properly configured to work with the Endpoint Protector, leading to DPI being bypassed.

## Solution
The issue was resolved by regenerating the local certificate used for SSL Inspection. This ensured that the certificate was compatible with the Endpoint Protector, allowing it to function correctly with the SSL inspection process.

## Notes
- Ensure that any local certificates used for SSL Inspection are properly configured and compatible with all security features in use.
- Regularly review and update certificates to prevent similar issues in the future.
- Document any changes made to SSL Inspection settings for future reference.