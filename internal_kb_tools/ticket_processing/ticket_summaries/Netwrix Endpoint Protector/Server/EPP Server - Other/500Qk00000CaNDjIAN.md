## Ticket Metadata
- **Ticket ID:** 500Qk00000CaNDjIAN
- **Case Number:** 413814
- **Status:** Closed - Resolved
- **Account/Company:** Seal Dynamics
- **Contact Name:** Andrew Siemasko
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** 5.6.0.0 - 5.9.3.0

## Problem Description
The customer reported vulnerabilities related to Remote Code Execution in CoSoSys Endpoint Protector, specifically affecting both server and client components. The support ticket was created to address these vulnerabilities and ensure they were resolved.

## Environment Details
- **Affected Components:**
  - Server: Versions 5.6.0.0 to 5.9.3.0
  - Client: Various versions for MacOS, Windows, and Linux

## Troubleshooting Steps
1. Reviewed the reported vulnerabilities and confirmed their existence in the specified versions.
2. Gathered necessary offline patch files for the server and client components.
3. Provided download links for the patches to the customer:
   - **Server Patch:** [Offline patch for 5.6.0.0 - 5.9.3.0](https://download.endpointprotector.com/offline_patches/MP-HWA-EPP4-U8800.tar.gz)
   - **Client Patches:**
     - MacOS: [EPPMac3.0.2.2005.Notarized.tar](https://download.endpointprotector.com/custom_agent/EppClientVulnerability/EPPMac3.0.2.2005.Notarized.tar)
     - Windows: [EPPClient_v6.2.2.2005.zip](https://download.endpointprotector.com/custom_agent/EppClientVulnerability/EPPClient_v6.2.2.2005.zip)
     - Linux: Multiple links for different distributions.
4. Deployed the hotfix `adv-2024-002` to address the vulnerabilities.

## Root Cause
The vulnerabilities were identified as Remote Code Execution risks in the CoSoSys Endpoint Protector software, affecting both server and client components across multiple operating systems.

## Solution
The issue was resolved by deploying the hotfix `adv-2024-002`, which addressed the identified vulnerabilities. The necessary patches were provided to the customer for both server and client components, ensuring that all affected systems were updated accordingly.

## Notes
- Ensure that all future support tickets related to vulnerabilities are linked to this incident for tracking purposes.
- Regularly check for updates and patches from CoSoSys to mitigate similar vulnerabilities in the future.
- Maintain communication with the customer regarding the importance of applying security patches promptly.