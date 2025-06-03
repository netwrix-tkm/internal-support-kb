## Ticket Metadata
- **Ticket ID:** 500Qk00000KZNzAIAX
- **Case Number:** 431938
- **Status:** Closed - Resolved
- **Account/Company:** Walt Disney Pictures
- **Contact Name:** Bob Rinaldi
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Install/Uninstall
- **Version:** 6.2.3.1

## Problem Description
The customer reported an error during the installation of version 6.2.3.1 of the Netwrix Endpoint Protector. The error message indicated that the service 'Endpoint Protector' could not be installed due to insufficient privileges, despite the installation being attempted under an ADMINISTRATOR account.

## Environment Details
- The installation was performed on a fresh server.
- The customer had recently migrated and needed to update the agent.
- The installation was attempted over an existing installation, which may have contributed to the issue.

## Troubleshooting Steps
1. Verified the error message received during installation: "Service 'Endpoint Protector' could not be installed. Verify that you have sufficient privileges to install system services."
2. Confirmed that the installation was being performed under an ADMINISTRATOR account.
3. Investigated the installation process and noted that the IP address was populated incorrectly during the manual installation.
4. Provided the customer with the zap tool to assist in the installation process.
5. Informed the customer that a new license file would be required since it was a fresh server.
6. Scheduled follow-up monitoring and checks for the next week.

## Root Cause
The root cause of the installation failure was identified as the incorrect IP address populated during the manual installation process, which likely led to conflicts with the existing installation.

## Solution
The issue was resolved by conducting a remote session where the agents were successfully installed without further issues. The customer was able to manage the installation on all computers using the provided zap tool.

## Notes
- Ensure that the IP address is correctly populated during installation to avoid similar issues in the future.
- For fresh server installations, always verify that a new license file is obtained and applied.
- Monitor installations closely after migration to catch any potential issues early.