## Ticket Metadata
- **Ticket ID:** 500Qk00000OQXAdIAP
- **Case Number:** 443149
- **Status:** Closed - Resolved
- **Account/Company:** Iovance BioTherapeutics
- **Contact Name:** Michael Aquinde
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device Rights
- **Version:** Not specified

## Problem Description
The customer reported that several computers were allowed USB access, which should not be the case. The computers had the Endpoint Protector (EPP) installed, but they were not visible in the USB bypass policy or the EPP console.

## Environment Details
- EPP clients were installed on the affected computers.
- The computers were not communicating with the EPP server.

## Troubleshooting Steps
1. Confirmed that the computers did not appear in the EPP UI, indicating a communication issue with the server.
2. Advised the customer to check the System Configuration for available licenses.
3. Suggested verifying if the EPP server IP was reachable from the affected machines.
4. Recommended uninstalling and reinstalling the EPP agent on one of the problematic machines.
5. Conducted a remote session to further investigate the issue.

## Root Cause
The EPP agent was deployed without the server IP and port being correctly configured, preventing the clients from communicating with the server.

## Solution
The customer was instructed to redeploy the EPP agent with the correct server IP and port settings. Documentation for the Intune deployment of EPP was provided to assist with the reconfiguration.

## Notes
- Ensure that the EPP agent is properly configured with the correct server IP and port during deployment to avoid similar issues in the future.
- The EPP server communicates with its clients over port 443; this should be verified in network configurations.
- If devices are unable to communicate with the server, they will not appear in the EPP console, and restrictions will not be enforced.