```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000KdlusIAB
- **Case Number:** 432226
- **Status:** Closed - Resolved
- **Account/Company:** ING companies
- **Contact Name:** Sudipa Bera
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** Not specified

## Problem Description
The customer requested assistance to change the EPP URL port from 443 to 8443 for both Production and DR environments in their on-premise setup.

## Environment Details
- On-premise setup of Netwrix Endpoint Protector.
- Current configuration uses port 443 for both Production and DR environments.

## Troubleshooting Steps
1. Conducted a remote session with the customer to initiate the port change.
2. Confirmed the requirement to replace port 443 with port 8443.
3. Implemented the configuration change to update the EPP URL to port 8443.

## Root Cause
The issue stemmed from the customer's requirement to change the default port (443) used by the EPP URL to a non-standard port (8443) for their specific operational needs.

## Solution
The port was successfully changed to 8443 during the remote session. The customer was advised to verify the functionality of the new configuration and confirm if everything works as expected.

## Notes
- Ensure that any firewall or network configurations are updated to allow traffic on port 8443.
- Customers should be informed that changing default ports may require additional configuration on client systems or applications that connect to the EPP server.
- Follow up with the customer after the change to confirm that the new port is functioning correctly.
```