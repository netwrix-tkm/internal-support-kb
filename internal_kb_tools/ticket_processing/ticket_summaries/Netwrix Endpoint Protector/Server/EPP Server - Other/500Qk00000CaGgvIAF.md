## Ticket Metadata
- **Ticket ID:** 500Qk00000CaGgvIAF
- **Case Number:** 413810
- **Status:** Closed - Resolved
- **Account/Company:** Zerodha Fund House
- **Contact Name:** Natalia Avdeenco
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** 5.6.0.0 - 5.9.3.0

## Problem Description
The customer reported critical remote code execution vulnerabilities affecting both the server and client components of the Netwrix Endpoint Protector.

## Environment Details
- **Affected Versions:** Server versions 5.6.0.0 to 5.9.3.0
- **Client Platforms:** MacOS, Windows, and various Linux distributions

## Troubleshooting Steps
1. Identified the vulnerabilities and their components (Server and Client).
2. Gathered necessary offline patches and client updates from the provided links.
3. Applied the hotfix adv-2024-002 to address the vulnerabilities.

## Root Cause
The vulnerabilities were due to security flaws in the server and client components of the Netwrix Endpoint Protector, which allowed for potential remote code execution.

## Solution
The issue was resolved by applying the hotfix adv-2024-002, which addressed the identified vulnerabilities. The following patches were provided for the affected components:
- **Server Patch:** 
  - [Offline patch for 5.6.0.0 - 5.9.3.0](https://download.endpointprotector.com/offline_patches/MP-HWA-EPP4-U8800.tar.gz)
- **Client Patches:**
  - **MacOS:** [EPPMac3.0.2.2005.Notarized.tar](https://download.endpointprotector.com/custom_agent/EppClientVulnerability/EPPMac3.0.2.2005.Notarized.tar)
  - **Windows:** [EPPClient_v6.2.2.2005.zip](https://download.endpointprotector.com/custom_agent/EppClientVulnerability/EPPClient_v6.2.2.2005.zip)
  - **Linux:** Multiple links for various distributions:
    - [Ubuntu 22.04](https://download.endpointprotector.com/linux_agent/EppClientVulnerability/EPPClient_ubuntu_22.04_v2.4.2.1007_x86_64.tar.gz)
    - [Ubuntu 20.04](https://download.endpointprotector.com/linux_agent/EppClientVulnerability/EPPClient_ubuntu_20.04_v2.4.2.1007_x86_64.tar.gz)
    - [Ubuntu 18.04](https://download.endpointprotector.com/linux_agent/EppClientVulnerability/EPPClient_ubuntu_18.04_v2.4.2.1007_x86_64.tar.gz)
    - [RHEL 9.4](https://download.endpointprotector.com/linux_agent/EppClientVulnerability/EPPClient_rhel_9.4_v2.4.2.1007_x86_64.tar.gz)
    - [RHEL 8.10](https://download.endpointprotector.com/linux_agent/EppClientVulnerability/EPPClient_rhel_8.10_v2.4.2.1007_x86_64.tar.gz)

## Notes
- Ensure to link all support tickets related to these vulnerabilities to the incident for tracking purposes.
- Mark support tickets as solved once the hotfix has been applied.
- Future cases should reference the hotfix adv-2024-002 for similar vulnerabilities.