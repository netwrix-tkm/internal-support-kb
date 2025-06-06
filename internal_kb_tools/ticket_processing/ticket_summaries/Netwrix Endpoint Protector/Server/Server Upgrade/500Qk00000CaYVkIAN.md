## Ticket Metadata
- **Ticket ID:** 500Qk00000CaYVkIAN
- **Case Number:** 413837
- **Status:** Closed - Resolved
- **Account/Company:** Engineering Office
- **Contact Name:** Aakif Khan
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Upgrade
- **Version:** 5.6.0.0 - 5.9.3.0

## Problem Description
The customer reported vulnerabilities related to Remote Code Execution in the CoSoSys software, specifically affecting both the server and client components. The support ticket was created to address these vulnerabilities and ensure they were resolved.

## Environment Details
- **Affected Components:**
  - Server
  - Client (MacOS, Windows, Linux)

## Troubleshooting Steps
1. Identified the vulnerabilities affecting the server and client components.
2. Gathered necessary offline patches and updates for the affected versions:
   - Server patch: [Offline patch for 5.6.0.0 - 5.9.3.0](https://download.endpointprotector.com/offline_patches/MP-HWA-EPP4-U8800.tar.gz)
   - Client patches for various operating systems:
     - MacOS: [EPPMac3.0.2.2005.Notarized.tar](https://download.endpointprotector.com/custom_agent/EppClientVulnerability/EPPMac3.0.2.2005.Notarized.tar)
     - Windows: [EPPClient_v6.2.2.2005.zip](https://download.endpointprotector.com/custom_agent/EppClientVulnerability/EPPClient_v6.2.2.2005.zip)
     - Linux: Multiple links for different distributions.
3. Applied the Hotfix 1.1 to address the identified vulnerabilities.

## Root Cause
The vulnerabilities were due to flaws in the CoSoSys software that allowed for Remote Code Execution, affecting both server and client components.

## Solution
The issue was resolved by applying Hotfix 1.1, which addressed the vulnerabilities in the software. The necessary patches for both server and client components were provided and implemented successfully.

## Notes
- Ensure to link all support tickets related to these vulnerabilities to the main incident for tracking purposes.
- Future updates should be monitored closely to prevent similar vulnerabilities from arising.
- For any questions or further clarifications, reach out to Paul, Adrian, or Cristian.