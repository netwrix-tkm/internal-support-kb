## Ticket Metadata
- **Ticket ID:** 500Qk00000DBgAxIAL
- **Case Number:** 415263
- **Status:** Closed - Resolved
- **Account/Company:** Evertec
- **Contact Name:** Duvan Roa
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Upgrade
- **Version:** 23.1

## Problem Description
The customer reported an issue during the update of the Endpoint Protector server, where the update process stalled at 62.5% with the error message "An error occurred. Hash does not match." The server in question was restricted from accessing the internet, and the customer sought guidance on necessary browsing permissions or potential server configuration issues.

## Environment Details
- The server was configured to restrict internet access.
- Specific URLs were requested for access:
  - `https://www.endpointprotector.com`
  - `https://endpointprotector.com`
  - IP Address: `178.63.3.86`

## Troubleshooting Steps
1. Verified the error message and the update process status.
2. Confirmed the server's internet access restrictions.
3. Discussed potential browsing permissions required for the update.
4. Explored server configuration settings that might affect the update process.
5. Attempted to identify if the issue was related to a specific patch.

## Root Cause
The root cause of the issue was identified as a corrupted or incompatible patch that was being applied during the server update process, which resulted in the hash mismatch error.

## Solution
The resolution involved removing the errored patch that caused the hash mismatch. After the patch was removed, the upgrade process was able to continue successfully without further issues.

## Notes
- Ensure that any patches applied to the Endpoint Protector server are verified for compatibility before installation, especially in environments with restricted internet access.
- For future updates, consider temporarily allowing access to necessary URLs to facilitate the update process, or ensure that all required files are available locally on the server prior to the update.