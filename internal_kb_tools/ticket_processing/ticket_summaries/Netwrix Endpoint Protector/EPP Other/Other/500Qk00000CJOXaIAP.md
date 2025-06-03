## Ticket Metadata
- **Ticket ID:** 500Qk00000CJOXaIAP
- **Case Number:** 413054
- **Status:** Closed - Resolved
- **Account/Company:** The Stars Group Interactive Services / Flutter International
- **Contact Name:** Alexandru Hojda
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Other
- **Version:** 3.0.2.1007

## Problem Description
The customer reported that the MacOS Stealth Mode, a built-in firewall feature, was not functioning as expected when the Netwrix Endpoint Protector (EPP) client was deployed on endpoints. Specifically, with Stealth Mode enabled, the machine was still responding to ping requests, indicating that it was reachable, contrary to the expected behavior.

## Environment Details
- Operating System: MacOS
- EPP Client Version: 3.0.2.1007
- DPI (Deep Packet Inspection) settings were enabled on the affected machine.

## Troubleshooting Steps
1. The customer tested the Stealth Mode functionality with the EPP agent removed and confirmed it worked as expected.
2. The support technician recommended testing with the latest EPP agent version and both DPI enabled and disabled.
3. The technician provided steps to enable debug logging and collect logs for further analysis if the issue persisted.
4. The technician analyzed the DPI settings and the "Intercept VPN traffic" option.

## Root Cause
The issue was identified as being caused by the DPI feature being enabled on the MacOS machine without the "Intercept VPN traffic" option also being enabled. This configuration prevented Stealth Mode from functioning correctly.

## Solution
To resolve the issue, the following solutions were provided:
1. Enable DPI and also enable the "Intercept VPN traffic" option.
2. Alternatively, disable DPI altogether.
3. After making the changes, the customer was advised to disable and then re-enable MacOS Stealth Mode for the changes to take effect.

The customer confirmed that turning off the "Intercept VPN traffic" option resolved the issue on their machine.

## Notes
- It is important to ensure that both DPI and "Intercept VPN traffic" settings are configured correctly to avoid similar issues in the future.
- A report can be generated to identify all users with the "Intercept VPN traffic" setting turned off by checking the 'Settings' column in the Device Control section of the EPP interface.