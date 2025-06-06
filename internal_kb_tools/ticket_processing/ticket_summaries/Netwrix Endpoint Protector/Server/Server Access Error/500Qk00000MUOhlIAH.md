## Ticket Metadata
- **Ticket ID:** 500Qk00000MUOhlIAH
- **Case Number:** 437472
- **Status:** Closed - Resolved
- **Account/Company:** Satcom Infotech
- **Contact Name:** Sai Nachiappan
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Access Error
- **Version:** Not specified

## Problem Description
The customer reported an inability to log in via the GUI of the Netwrix Endpoint Protector, despite the server's IP address responding to ping requests. This issue was preventing the onboarding of the server.

## Environment Details
- The issue occurred on a server running Netwrix Endpoint Protector.
- The server was configured with a static IP.

## Troubleshooting Steps
1. Investigated the server's configuration and logs.
2. Checked the network connectivity by pinging the server's IP address, which was successful.
3. Analyzed the nginx configuration for potential issues related to certificate loading.
4. Attempted to access the GUI, which failed due to certificate issues.

## Root Cause
The root cause of the issue was identified as the inability of the nginx configuration to load the necessary certificates, which prevented the GUI from being accessible.

## Solution
The issue was resolved by reimporting the Certificate Authorities (CAs) and applying them to the server. After this action, the GUI became accessible, allowing the customer to log in successfully.

## Notes
- Ensure that all certificates are correctly configured and loaded in the nginx configuration to avoid similar issues in the future.
- Regularly verify the status of certificates and their paths in the configuration to prevent access issues.