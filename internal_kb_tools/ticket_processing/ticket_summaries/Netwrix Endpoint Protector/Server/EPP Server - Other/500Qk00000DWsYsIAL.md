## Ticket Metadata
- **Ticket ID:** 500Qk00000DWsYsIAL
- **Case Number:** 416049
- **Status:** Closed - Resolved
- **Account/Company:** CIPS MSP
- **Contact Name:** Veronica Conti
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** 5.8.1.0

## Problem Description
The customer, F.T.P. Srl, reported several issues following the installation of the Netwrix Endpoint Protector, including problems with downloading the latest appliance, SSL certificate management, Active Directory synchronization, and browsing capabilities within the Directory Services.

## Environment Details
- The customer attempted to download the 5.8.1.0 VHDX appliance from the official website.
- The server is configured to sync with Active Directory for user and group management.

## Troubleshooting Steps
1. Verified the download link for the latest appliance and checked for any reported issues with the template.
2. Discussed the possibility of changing the SSL certificate for the web console access.
3. Clarified the implications of an SSL certificate expiration on client-server communication.
4. Investigated the issue of the manually created System Administrator account not syncing with the AD group after deletion.
5. Examined the inability to browse groups and sub-OUs during AD synchronization.

## Root Cause
The root cause of the issues was identified as a combination of:
- A potential problem with the VHDX template that prevented it from starting properly.
- Misconfiguration in the SSL certificate settings.
- A known limitation in the synchronization process that affected the visibility of certain accounts and groups in Active Directory.

## Solution
The issues were resolved during a remote session via Anydesk, where the following actions were taken:
- The VHDX template was replaced with a verified working version.
- The SSL certificate was successfully updated to allow secure access to the web console.
- The synchronization settings were adjusted to ensure that all relevant accounts from Active Directory were imported correctly.

## Notes
- It is recommended to always verify the integrity of downloaded templates before installation.
- Regularly check and renew SSL certificates to avoid communication issues.
- Be aware of potential limitations in Active Directory synchronization and ensure proper configurations are in place to facilitate visibility of all necessary accounts and groups.