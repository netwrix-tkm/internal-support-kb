```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000EzyooIAB
- **Case Number:** 419301
- **Status:** Closed - Resolved
- **Account/Company:** MAX IT Finance LTD
- **Contact Name:** Eyal Shrao
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Deployment
- **Version:** 3.0.3.1

## Problem Description
The customer reported that after installing the latest version of the Netwrix Endpoint Protector client on macOS Sonoma, the agent was unable to connect to the management server. The issue was not related to the firewall.

## Environment Details
- Operating System: macOS Sonoma
- Proxy Configuration: Enabled during installation

## Troubleshooting Steps
1. Verified that the firewall was not blocking the connection.
2. Attempted to connect the client with the proxy enabled, which failed.
3. Disabled the proxy and confirmed that the client could connect to the server.
4. Identified two workarounds:
   - Install the client without the proxy enabled, then enable the proxy after installation.
   - Remove the proxy configuration from `/etc/epp/options.ini` and the associated certificate file.
5. Provided a script to configure the proxy settings correctly.
6. Discussed the uninstallation process and password issues with the customer.

## Root Cause
The client was configured to use a proxy that was not correctly routing traffic to the management server, preventing the agent from establishing a connection. The proxy settings were causing the client to misroute requests.

## Solution
The issue was resolved by:
- Advising the customer to install the client without the proxy enabled initially.
- Providing a script to configure the proxy settings correctly after installation.
- Confirming that the client could communicate with the server once the proxy was disabled or configured correctly.

## Notes
- Ensure that the proxy settings are correctly configured for clients that need to communicate with local servers.
- If the client is installed with proxy settings enabled, it may lead to connectivity issues, especially if the server is on the same local network.
- For uninstallation issues, ensure that the correct password is used and that the password complexity does not interfere with macOS requirements.
```