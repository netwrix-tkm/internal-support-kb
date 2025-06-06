## Ticket Metadata
- **Ticket ID:** 500Qk00000CaPvVIAV
- **Case Number:** 413831
- **Status:** Closed - Resolved
- **Account/Company:** Blue Halo
- **Contact Name:** Mike Callahan
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Health
- **Version:** 5.6.0.0 - 5.9.3.0

## Problem Description
The customer reported vulnerabilities related to remote code execution in CoSoSys Endpoint Protector, specifically affecting both server and client components. The support ticket was created to address these vulnerabilities and ensure proper patching.

## Environment Details
- **Affected Components:**
  - Server
  - Client (MacOS, Windows, Linux)

## Troubleshooting Steps
1. Reviewed the reported vulnerabilities and their impact on the server and client components.
2. Provided necessary offline patches and client updates for various operating systems:
   - **Server Patch:** 
     - [Offline patch for 5.6.0.0 - 5.9.3.0](https://download.endpointprotector.com/offline_patches/MP-HWA-EPP4-U8800.tar.gz)
   - **Client Patches:**
     - MacOS: [EPPMac3.0.2.2005.Notarized.tar](https://download.endpointprotector.com/custom_agent/EppClientVulnerability/EPPMac3.0.2.2005.Notarized.tar)
     - Windows: [EPPClient_v6.2.2.2005.zip](https://download.endpointprotector.com/custom_agent/EppClientVulnerability/EPPClient_v6.2.2.2005.zip)
     - Linux:
       - [Ubuntu 22.04](https://download.endpointprotector.com/linux_agent/EppClientVulnerability/EPPClient_ubuntu_22.04_v2.4.2.1007_x86_64.tar.gz)
       - [Ubuntu 20.04](https://download.endpointprotector.com/linux_agent/EppClientVulnerability/EPPClient_ubuntu_20.04_v2.4.2.1007_x86_64.tar.gz)
       - [Ubuntu 18.04](https://download.endpointprotector.com/linux_agent/EppClientVulnerability/EPPClient_ubuntu_18.04_v2.4.2.1007_x86_64.tar.gz)
       - [RHEL 9.4](https://download.endpointprotector.com/linux_agent/EppClientVulnerability/EPPClient_rhel_9.4_v2.4.2.1007_x86_64.tar.gz)
       - [RHEL 8.10](https://download.endpointprotector.com/linux_agent/EppClientVulnerability/EPPClient_rhel_8.10_v2.4.2.1007_x86_64.tar.gz)
3. Deployed hotfix adv-2024-002 to address the vulnerabilities.

## Root Cause
The vulnerabilities were identified in the CoSoSys Endpoint Protector software, affecting both server and client components, which could potentially allow remote code execution.

## Solution
The issue was resolved by deploying the hotfix adv-2024-002 and providing the necessary patches for both server and client components. The customer was instructed to apply these patches to mitigate the vulnerabilities.

## Notes
- Ensure that all future support tickets related to these vulnerabilities are linked to this incident and marked as solved.
- It is important to regularly check for updates and patches for the Endpoint Protector to maintain security and compliance.
- For any questions or further assistance, reach out to Paul, Adrian, or Cristian.