## Ticket Metadata
- **Ticket ID:** 500Qk00000JIhbTIAT
- **Case Number:** 429335
- **Status:** Closed - Resolved
- **Account/Company:** Dubai Police
- **Contact Name:** Fakhra Abdulla
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Deployment
- **Version:** NONE

## Problem Description
The customer reported that the EPP client was installed on four MacBooks with the same OS version and network configuration. While two of the MacBooks connected successfully to the EPP server, the other two did not establish a connection.

## Environment Details
- Four MacBooks with the same OS version
- Same network configuration for all devices
- EPP client installation attempted with proxy settings enabled

## Troubleshooting Steps
1. Verified the installation of the EPP client on all four MacBooks.
2. Checked network traffic between the non-connecting MacBooks and the EPP server, confirming there were no blocks.
3. Attempted to install the EPP client with the proxy enabled.
4. Observed that when the proxy was enabled, the client did not communicate with the server.
5. Tested disabling the proxy, which allowed the client to communicate with the server.
6. Identified two workarounds:
   - Install the client without the proxy enabled and enable it post-installation.
   - Remove the proxy configuration line from `/etc/epp/options.ini` and the associated "cert.xxxxx..." file.

## Root Cause
The root cause of the issue was identified as the EPP client not being able to communicate with the server when the proxy was enabled during installation. The client adopted the proxy configuration, which interfered with its ability to connect to the server.

## Solution
The issue was resolved by installing the EPP client without the proxy enabled. After the installation was complete, the proxy was enabled, allowing the client to communicate with the server successfully.

## Notes
- For future installations, it is recommended to install the EPP client without the proxy enabled initially, then enable the proxy afterward to avoid connectivity issues.
- Alternatively, if the proxy must be enabled during installation, ensure to remove the proxy configuration from `/etc/epp/options.ini` and the corresponding certificate file to restore communication with the server.