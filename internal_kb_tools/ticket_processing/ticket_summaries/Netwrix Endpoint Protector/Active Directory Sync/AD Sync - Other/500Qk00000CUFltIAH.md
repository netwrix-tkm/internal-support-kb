## Ticket Metadata
- **Ticket ID:** 500Qk00000CUFltIAH
- **Case Number:** 413519
- **Status:** Closed - Resolved
- **Account/Company:** Semi Conductor Devices
- **Contact Name:** Timur Bafaev
- **Product:** Netwrix Endpoint Protector
- **Component:** Active Directory Sync
- **Feature:** AD Sync - Other
- **Version:** 5.8.1.0

## Problem Description
The customer reported an issue with binding the Netwrix Endpoint Protector (EPP) server version 5.8.1.0 to Active Directory (AD). The error message indicated that the binding failed due to invalid credentials.

## Environment Details
- EPP Server Version: 5.8.1.0
- Attempted Connection Ports: 389 (LDAP) and 636 (LDAPS)
- Network Configuration: The server is in an air-gapped network, meaning it is not connected to the internet.

## Troubleshooting Steps
1. Confirmed the error message: "Bind to Active Directory failed. Check the login credentials and/or server details. AD said: invalid credentials."
2. Suggested a remote connection to investigate further.
3. Requested the customer to update the EPP server to version 5.9.3.0.
4. Inquired about the AD settings and requested screenshots of the configurations.
5. Advised the customer to try different connection types and to wait 3 minutes after saving settings before testing the connection.

## Root Cause
The root cause of the issue was identified as incorrect login credentials or misconfigured settings in the Active Directory binding process. The air-gapped nature of the network also limited troubleshooting options.

## Solution
The issue was resolved by guiding the customer to:
- Verify and correct the login credentials used for binding to Active Directory.
- Ensure that the correct server details and connection types were selected.
- After making the necessary adjustments, the binding to Active Directory was successful.

## Notes
- Ensure that the credentials used for binding to Active Directory are correct and have the necessary permissions.
- When working in air-gapped environments, be prepared to guide customers through manual troubleshooting steps, as remote access may not be possible.
- Always recommend updating to the latest version of the software to benefit from bug fixes and improvements.