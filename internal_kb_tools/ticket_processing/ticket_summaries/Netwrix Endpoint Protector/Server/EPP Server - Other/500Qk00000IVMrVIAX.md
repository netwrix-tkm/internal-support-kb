## Ticket Metadata
- **Ticket ID:** 500Qk00000IVMrVIAX
- **Case Number:** 427484
- **Status:** Closed - Resolved
- **Account/Company:** Stadtwerke Homburg GmbH
- **Contact Name:** Thorsten Weiler
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** 1.1

## Problem Description
The customer reported issues with the Netwrix Endpoint Protector following a network change due to the replacement of switches, which altered the gateway. They were unable to change the IP address or gateway settings and received an error message when attempting to do so.

## Environment Details
- The issue arose after a network reconfiguration involving the replacement of network switches.
- The specific error message encountered was not detailed in the case but indicated a failure to change network settings.

## Troubleshooting Steps
1. The customer reached out for support, requesting assistance in German.
2. The support team scheduled a session to investigate the issue further.
3. The support engineer reviewed the configuration and identified the need to modify the Grub file.

## Root Cause
The root cause of the issue was identified as a misconfiguration in the Grub file, which prevented the changes to the IP address and gateway settings from being applied correctly.

## Solution
The issue was resolved by changing the Grub file according to the established procedure (Procedure 63). This allowed the customer to successfully update the IP address and gateway settings.

## Notes
- Ensure that any network changes, such as switch replacements, are followed by a review of the Endpoint Protector configuration to prevent similar issues.
- It is advisable to document any changes made to the Grub file for future reference and troubleshooting.
- Customers should be encouraged to provide detailed error messages when reporting issues to facilitate quicker resolution.