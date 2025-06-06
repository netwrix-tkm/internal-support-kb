```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000CXrbJIAT
- **Case Number:** 413678
- **Status:** Closed - Resolved
- **Account/Company:** Palo Pinto General Hospital
- **Contact Name:** Josh Yowell
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Health
- **Version:** Not specified

## Problem Description
The server was unable to obtain a default gateway via DHCP, and when a static IP was configured, it returned an error stating "ERROR - Please enter valid gateway." Although the device was reachable via ping, the web interface was not accessible.

## Environment Details
- The server is hosted in a local virtual machine (VM).
- The issue arose after an unexpected server downtime.

## Troubleshooting Steps
1. Suggested using a static IP configuration and verifying subnet settings.
2. Proposed setting up a remote session to investigate the server configuration further.
3. Scheduled a meeting to troubleshoot the issue in real-time.

## Root Cause
The issue was identified as a problem with the network interfaces on the appliance, which were not functioning correctly.

## Solution
The problem was resolved by fixing the bugged interfaces on the appliance, allowing the server to properly grab a default gateway and access the web interface.

## Notes
- Ensure that the correct configuration settings for the subnet are always applied when setting up the appliance.
- Future installations should verify network interface functionality to prevent similar issues.
- Regular checks on server health and network configurations are recommended after unexpected downtimes.
```