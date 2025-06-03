## Ticket Metadata
- **Ticket ID:** 500Qk00000CaIyrIAF
- **Case Number:** 413812
- **Status:** Closed - Resolved
- **Account/Company:** Tornado Bus Company
- **Contact Name:** Andrew Siemasko
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** 5.6.0.0 - 5.9.3.0

## Problem Description
The customer reported vulnerabilities related to Remote Code Execution in CoSoSys Endpoint Protector, affecting both server and client components.

## Environment Details
- **Affected Components:**
  - Server: Versions 5.6.0.0 to 5.9.3.0
  - Client: Various versions for MacOS, Windows, and Linux

## Troubleshooting Steps
1. Reviewed the reported vulnerabilities and their impact on the server and client components.
2. Gathered necessary offline patch files for the server and client components.
3. Provided download links for the patches specific to MacOS, Windows, and Linux clients.
4. Deployed the hotfix adv-2024-002 to address the vulnerabilities.

## Root Cause
The vulnerabilities were identified as Remote Code Execution risks in the CoSoSys Endpoint Protector software, specifically affecting the server and client components.

## Solution
The issue was resolved by deploying the hotfix adv-2024-002, which addressed the identified vulnerabilities. The following patches were provided for the affected components:
- **Server Patch:** 
  - [Offline patch for 5.6.0.0 - 5.9.3.0](https://download.endpointprotector.com/offline_patches/MP-HWA-EPP4-U8800.tar.gz)
- **Client Patches:**
  - **MacOS:** [EPPMac3.0.2.2005.Notarized.tar](https://download.endpointprotector.com/custom_agent/EppClientVulnerability/EPPMac3.0.2.2005.Notarized.tar)
  - **Windows:** [EPPClient_v6.2.2.2005.zip](https://download.endpointprotector.com/custom_agent/EppClientVulnerability/EPPClient_v6.2.2.2005.zip)
  - **Linux:** 
    - [Ubuntu 22.04](https://download.endpointprotector.com/linux_agent/EppClientVulnerability/EPPClient_ubuntu_22.04_v2.4.2.1007_x86_64.tar.gz)
    - [Ubuntu 20.04](https://download.endpointprotector.com/linux_agent/EppClientVulnerability/EPPClient_ubuntu_20.04_v2.4.2.1007_x86_64.tar.gz)
    - [Ubuntu 18.04](https://download.endpointprotector.com/linux_agent/EppClientVulnerability/EPPClient_ubuntu_18.04_v2.4.2.1007_x86_64.tar.gz)
    - [RHEL 9.4](https://download.endpointprotector.com/linux_agent/EppClientVulnerability/EPPClient_rhel_9.4_v2.4.2.1007_x86_64.tar.gz)
    - [RHEL 8.10](https://download.endpointprotector.com/linux_agent/EppClientVulnerability/EPPClient_rhel_8.10_v2.4.2.1007_x86_64.tar.gz)

## Notes
- Ensure that all future support tickets related to these vulnerabilities are linked to this incident and marked as solved.
- For any questions or further assistance, reach out to Paul, Adrian, or Cristian.