```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000DnjPWIAZ
- **Case Number:** 416625
- **Status:** Closed - Resolved
- **Account/Company:** Kepsure Solutions
- **Contact Name:** Dharmik Bhayani
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** EPP Client - Other
- **Version:** Not specified

## Problem Description
The client application shows as online on the server after installation, but the client itself indicates that the server IP is not set.

## Environment Details
- The issue was reported in a client-server setup using Netwrix Endpoint Protector.

## Troubleshooting Steps
1. Verified the client status on the server and confirmed it appeared online.
2. Checked the client application for server IP configuration.
3. Collected logs from the client for analysis.
4. Suggested reinstalling the EPP client to see if the issue persists.
5. Reviewed the logs and found them empty, indicating potential issues with client-server communication.
6. Investigated potential certificate issues in the Windows Certificate Store.
7. Consulted Jira issues related to missing certificates that could affect client communication.

## Root Cause
The issue was identified as being related to missing certificates in the Windows Certificate Store, which prevented the EPP client from properly communicating with the EPP notifier.

## Solution
The resolution involved:
- Ensuring that the necessary certificates (Global Sign and DigiCert) were installed in the Windows Certificate Store.
- After installing the required certificates, the client was able to correctly set the server IP and communicate with the server.

## Notes
- It is important to check for missing certificates in the Certificate Store when encountering similar issues with client-server communication in Netwrix Endpoint Protector.
- Future installations should verify that all necessary certificates are present to avoid similar issues.
```