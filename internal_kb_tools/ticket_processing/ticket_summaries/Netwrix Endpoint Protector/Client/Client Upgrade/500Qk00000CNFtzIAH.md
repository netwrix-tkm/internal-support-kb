```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000CNFtzIAH
- **Case Number:** 413248
- **Status:** Closed - Resolved
- **Account/Company:** FAIR Health, Inc.
- **Contact Name:** Nicholas Micallef
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Upgrade
- **Version:** 3.0.2.2005 (MacOS Agent)

## Problem Description
The customer inquired whether the MacOS Endpoint Protector Agents were affected by the recent security disclosure ADV-2024-002, which indicated multiple vulnerabilities in the Endpoint Protector agents and server.

## Environment Details
- The customer had already addressed vulnerabilities in Windows agents and applied a hotfix to their server.

## Troubleshooting Steps
1. Confirmed that MacOS Agents were indeed affected by ADV-2024-002.
2. Scheduled a remote session to apply the necessary patch to the EPP Server.
3. Provided download links for the latest EPP Agents for both Windows and MacOS.
4. Informed the customer that the new MacOS agent version 3.0.2.2005 was available for download but not yet included in the EPP Server for remote upgrades.
5. Clarified that the new MacOS agent could be installed on top of the existing agent without needing to uninstall it first.

## Root Cause
The vulnerabilities referenced in ADV-2024-002 affected both Windows and MacOS Endpoint Protector Agents, necessitating an update to mitigate security risks.

## Solution
The issue was resolved by providing the customer with the download link for the patched MacOS agent version 3.0.2.2005:
- [Download MacOS Agent 3.0.2.2005](https://download.endpointprotector.com/custom_agent/EppClientVulnerability/EPPMac3.0.2.2005.Notarized.tar)

Additionally, it was confirmed that the new agent could be installed directly over the existing version.

## Notes
- The new EPP Agent version 3.0.2.2005 was not included in the patch for the EPP Server, meaning it could not be pushed via the System Configuration -> Client Software Upgrade feature at that time.
- Customers should be advised to use an MDM tool to push the new agents to their machines if necessary.
- Future updates regarding the inclusion of the new agent in the EPP Server for remote upgrades should be monitored.
```