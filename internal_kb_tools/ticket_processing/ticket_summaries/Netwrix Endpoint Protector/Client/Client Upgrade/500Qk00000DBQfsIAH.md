## Ticket Metadata
- **Ticket ID:** 500Qk00000DBQfsIAH
- **Case Number:** 415247
- **Status:** Closed - Resolved
- **Account/Company:** AXA Venture Partners
- **Contact Name:** Sebastien Ebbo
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Upgrade
- **Version:** 6.1.0.6 (client version reported)

## Problem Description
The customer reported confusion regarding the application of a security update following the security advisory ADV-2024-002, which addressed remote code execution vulnerabilities in CoSoSys Endpoint Protector. The customer believed updates were automatic but found that all computers were still running version 6.1.0.6 and did not see any newer versions.

## Environment Details
- All computers were running version 6.1.0.6 of the Netwrix Endpoint Protector client for Windows.

## Troubleshooting Steps
1. Confirmed the need for a manual application of the hotfix to the EPP Server.
2. Provided instructions for applying the hotfix via the "Dashboard" > "Live Update" interface.
3. Offered assistance for a remote session to guide the customer through the hotfix application.
4. Informed the customer about the necessity to upgrade EPP clients after applying the hotfix.
5. Provided a link to download the offline patch for EPP clients.
6. Detailed the steps to upload the offline patch and upgrade client software.

## Root Cause
The issue arose because the hotfix for the security vulnerability needed to be applied manually to the EPP Server, and the client software also required an upgrade to address the vulnerabilities. The customer was unaware that the updates were not automatic and that manual intervention was necessary.

## Solution
The issue was resolved by:
1. Applying the hotfix to the EPP Server manually.
2. Downloading and uploading the offline patch for EPP clients.
3. Upgrading the EPP clients to the latest version available on the server.

The customer was guided through these steps during a scheduled remote session, ensuring that the upgrade job was completed successfully.

## Notes
- Ensure that customers are aware that hotfixes and client upgrades may require manual intervention, especially after security advisories.
- It is important to verify the version of the client software and confirm that all necessary updates have been applied to mitigate security vulnerabilities effectively.