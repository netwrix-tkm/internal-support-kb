## Ticket Metadata
- **Ticket ID:** 500Qk00000JMADtIAP
- **Case Number:** 429490
- **Status:** Closed - Resolved
- **Account/Company:** Catchpoint India
- **Contact Name:** Ronak Bhanushali
- **Product:** Netwrix Endpoint Protector
- **Component:** System & Log Backups
- **Feature:** External Storage - FTP/Samba
- **Version:** Not specified

## Problem Description
The customer reported an inability to configure external storage via SFTP, receiving an "incorrect credentials" error despite confirming that the SFTP settings were correct and functional through other clients.

## Environment Details
- The issue occurred within the Netwrix Endpoint Protector (EPP) platform.
- The SFTP connection was tested successfully using various SFTP clients to a remote public server.

## Troubleshooting Steps
1. Verified SFTP settings and credentials.
2. Confirmed SFTP functionality using external clients.
3. Checked user permissions on the SFTP server.
4. Attempted to create a new file in the designated SFTP path, which succeeded.
5. Collected logs during the connection attempts for further analysis.
6. Investigated potential issues with outdated ciphers required by the EPP server.

## Root Cause
The EPP server was configured to request outdated ciphers that are disabled by default in OpenSSL, leading to the "incorrect credentials" error when attempting to connect via SFTP.

## Solution
The issue was resolved by enabling the outdated ciphers on the EPP server. After this change, the SFTP functionality began working as expected, allowing the Data Loss Prevention (DLP) system to successfully send files to the external storage.

## Notes
- Ensure that any future configurations involving SFTP connections consider the cipher requirements of the server.
- It may be beneficial to document any specific cipher settings or TLS version requirements for the servers being connected to, as this can prevent similar issues from arising in the future.