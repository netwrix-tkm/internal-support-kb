## Ticket Metadata
- **Ticket ID:** 500Qk00000JdhWnIAJ
- **Case Number:** 430166
- **Status:** Closed - Resolved
- **Account/Company:** Halodata International Pte Ltd
- **Contact Name:** Halodata Support Tech
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Deployment
- **Version:** 5940

## Problem Description
The customer reported an issue with the Netwrix Endpoint Protector (EPP) client failing to maintain a connection with the server after initial installation. The client would communicate once and then stop, displaying the IP as NOT SET while indicating a connection status of YES.

## Environment Details
- The affected PCs do not have internal network adapters and utilize third-party network adapters (e.g., TP Link, Realtek).
- The PCs can successfully ping the server and access the dashboard via HTTPS.

## Troubleshooting Steps
1. Verified the client installation and initial communication with the server.
2. Checked network connectivity by pinging the server from the affected PCs.
3. Allowed USB modem access under Global rights before reinstalling the client.
4. Reinstalled the EPP client multiple times to attempt to restore communication.
5. Suggested a call with the customer for further troubleshooting.

## Root Cause
The issue was identified as being related to the operating system configuration or the network adapter settings, particularly since the affected PCs were using third-party network adapters.

## Solution
The problem was resolved by performing a reset of the Windows operating system, followed by a fresh installation of the EPP client. This action restored the communication between the client and the server.

## Notes
- Ensure that any PCs using third-party network adapters are properly configured to communicate with the EPP server.
- Consider documenting any specific configurations or settings that may be required for third-party adapters in future cases.
- Regularly check for updates or patches for the EPP client that may address connectivity issues.