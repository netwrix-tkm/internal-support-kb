## Ticket Metadata
- **Ticket ID:** 500Qk00000OLnfwIAD
- **Case Number:** 442856
- **Status:** Closed - Resolved
- **Account/Company:** Slice Fintech
- **Contact Name:** Santosh Kaddu
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Migration
- **Version:** Not specified

## Problem Description
The customer, Slice Fintech, was in the process of migrating their existing AWS account servers to a different account, which involved changing the server IP addresses. They requested documentation and configuration details to ensure proper communication between agents and the new server post-migration.

## Environment Details
- Existing EPP VM version: 5.9.4.0 (assumed based on backup requirements)
- Migration involved creating a new EPP VM in a different AWS account.

## Troubleshooting Steps
1. Provided initial guidance on creating a System Backup V2 from the existing EPP UI.
2. Advised taking a snapshot of the existing virtual machine before migration.
3. Scheduled remote sessions to assist with the migration process.
4. In the remote session on 12-05, created the System Backup V2 and backup key.
5. Updated the new server to the latest version and imported the System Backup V2.
6. Instructed the customer to redo the SSO configuration for the new EPP server, which included removing the existing configuration and creating a new one.
7. On 13-05, confirmed successful installation of the new EPP VM and the import of the System Backup V2 after SSO removal.

## Root Cause
The issue stemmed from the need to migrate the existing EPP VM to a new AWS account, which required careful handling of the backup and configuration settings to ensure continuity of service and communication with endpoints.

## Solution
The issue was resolved by:
- Successfully installing the new EPP VM.
- Importing the System Backup V2 after removing the old SSO configuration.
- Ensuring that the new server was updated to the latest version and configured correctly to communicate with the endpoints.

## Notes
- It is crucial to ensure that the new EPP VM has the same version as the old one for the backup import to work correctly.
- If the IP address of the new server is different, utilize the change IP tool to update the server's IP assigned to the endpoints.
- Always take a snapshot of the existing VM before making significant changes to avoid data loss.