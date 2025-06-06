## Ticket Metadata
- **Ticket ID:** 500Qk00000OICZbIAP
- **Case Number:** 442661
- **Status:** Closed - Resolved
- **Account/Company:** Technology & IT Data Analyst
- **Contact Name:** Philip Wang
- **Product:** Netwrix Endpoint Protector
- **Component:** System & Log Backups
- **Feature:** External Storage - Other
- **Version:** 22.04

## Problem Description
The customer reported issues setting up external storage using a container in an Azure Storage Account via SFTP. They encountered an "incorrect credentials" error despite entering the correct credentials.

## Environment Details
- Azure Storage Account configured for SFTP access.
- Customer located in the US.

## Troubleshooting Steps
1. Initial contact with the customer to gather details and schedule a remote session.
2. Conducted a remote session to access the SFTP storage via backend commands and checked TLS values in the Nginx configuration file.
3. Engaged the engineering team to verify compatibility with Azure Blobs.
4. Informed the customer that Azure Blobs are not officially supported and recommended using Azure SMB instead.
5. Conducted a follow-up remote session to test Azure external storage and address licensing questions.
6. Identified communication issues with some computers not connecting to the EPP server; customer planned to attempt a reinstall.

## Root Cause
The root cause of the issue was the attempt to use Azure Blobs for external storage, which is not officially supported by the Netwrix Endpoint Protector. The system was unable to authenticate correctly due to this incompatibility.

## Solution
The issue was resolved by switching from Azure Blobs to Azure SMB for external storage configuration. The customer successfully configured the external storage using Azure SMB after receiving guidance from the support team.

## Notes
- Azure Blobs are not supported for external storage in Netwrix Endpoint Protector; always recommend Azure SMB for such configurations.
- Ensure to verify compatibility with the engineering team when customers report issues related to specific storage solutions.
- Follow up with customers regarding any additional issues they may encounter after implementing the recommended solutions.