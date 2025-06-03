## Ticket Metadata
- **Ticket ID:** 500Qk00000CljVpIAJ
- **Case Number:** 414254
- **Status:** Closed - Resolved
- **Account/Company:** Successive Technologies Pvt Ltd
- **Contact Name:** Abhishek Tewari
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Feature Request
- **Version:** 6.2.2.1 (dashboard), 6.2.2.2005 (forum)

## Problem Description
The customer reported an issue related to the application of a newly released security patch (ADV-2024-002) on the EPP server. After applying the hotfix, the agents were still showing an option to download the updated agents instead of automatically updating. The customer inquired if there was a way to apply the new agent update from the dashboard or through the 'Client Software Upgrade' option.

## Environment Details
- **Hotfix Deployed:** ADV-2024-002
- **Agent Version on Dashboard:** 6.2.2.1
- **Agent Version on Forum:** 6.2.2.2005

## Troubleshooting Steps
1. The support engineer requested the customer to check the EPP console and navigate to Dashboard > Live Update > "View Applied EPP Software Updates" to confirm if the hotfix was applied.
2. The customer confirmed that the latest fix (hotfix 1.1 version) was applied and provided a screenshot as evidence.
3. The support engineer acknowledged that the client updates were not included in the UI for this release and proceeded to provide download links for the updated agents.

## Root Cause
The issue was identified as a limitation in the user interface of the EPP console, where the client updates were not included in the UI for the current hotfix release. This resulted in the agents prompting for a download instead of updating automatically.

## Solution
The support engineer provided the customer with direct download links for the updated agents:
- **Windows Agent:** [Download Link](https://download.endpointprotector.com/custom_agent/EppClientVulnerability/EPPClient_v6.2.2.2005.zip)
- **MacOS Agent:** [Download Link](https://download.endpointprotector.com/custom_agent/EppClientVulnerability/EPPMac3.0.2.2005.Notarized.tar)

The case was closed after confirming with the customer that the hotfix was applied successfully and the download links were provided.

## Notes
- Future updates should ensure that client updates are included in the UI to avoid confusion for users.
- Customers should be informed about the manual download process for agent updates when such limitations exist in the UI.