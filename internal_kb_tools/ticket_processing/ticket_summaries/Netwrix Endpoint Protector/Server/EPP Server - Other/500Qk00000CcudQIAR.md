## Ticket Metadata
- **Ticket ID:** 500Qk00000CcudQIAR
- **Case Number:** 413947
- **Status:** Closed - Resolved
- **Account/Company:** The Stars Group Interactive Services / Flutter International
- **Contact Name:** Andy Bridson
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Server
- **Feature:** EPP Server - Other
- **Version:** Not specified

## Problem Description
The customer reported that after applying the latest hot-fixes to their tenants, they were not seeing any updated client versions and inquired if this was expected behavior.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Server

## Troubleshooting Steps
1. Confirmed that the latest hot-fix does not automatically import new agents.
2. Provided download links for the new agents for both MacOS and Windows:
   - MacOS: [Download Link](https://download.endpointprotector.com/custom_agent/EppClientVulnerability/EPPMac3.0.2.2005.Notarized.tar)
   - Windows: [Download Link](https://download.endpointprotector.com/custom_agent/EppClientVulnerability/EPPClient_v6.2.2.2005.zip)
3. Offered to schedule a remote session to assist in injecting the new EPP Clients into the EPP Server.

## Root Cause
The root cause of the issue was identified as a misunderstanding regarding the functionality of the latest hot-fix. The hot-fix does not import new agents; instead, the agents are treated separately and need to be manually downloaded and injected into the system.

## Solution
The issue was resolved by clarifying to the customer that they needed to manually download and install the new client versions from the provided links. Additionally, a remote session was offered to assist with the injection of the new clients into the EPP Server, although the customer opted to use their existing deployment methods (SCCM/Jamf) instead.

## Notes
- It is important to communicate clearly that hot-fixes may not include automatic updates for client agents and that these need to be handled separately.
- Future support interactions should ensure that customers are aware of the manual steps required for client updates after applying hot-fixes.