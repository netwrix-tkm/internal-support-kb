## Ticket Metadata
- **Ticket ID:** 500Qk00000CaHbKIAV
- **Case Number:** 413811
- **Status:** Closed - Resolved
- **Account/Company:** Cognizant Technology Solutions
- **Contact Name:** Andrew Siemasko
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** 5.6.0.0 - 5.9.3.0

## Problem Description
The customer reported critical remote code execution vulnerabilities in the CoSoSys Endpoint Protector, affecting both server and client components. The support ticket was created to address these vulnerabilities and ensure proper remediation.

## Environment Details
- **Affected Components:**
  - Server: Netwrix Endpoint Protector (versions 5.6.0.0 - 5.9.3.0)
  - Client: Various platforms including MacOS, Windows, and Linux.

## Troubleshooting Steps
1. Linked all support tickets related to the vulnerabilities to the incident.
2. Identified and documented the necessary offline patches for the server and client components.
3. Provided download links for the patches:
   - **Server Patch:** [Offline patch for 5.6.0.0 - 5.9.3.0](https://download.endpointprotector.com/offline_patches/MP-HWA-EPP4-U8800.tar.gz)
   - **Client Patches:**
     - MacOS: [EPPMac3.0.2.2005.Notarized.tar](https://download.endpointprotector.com/custom_agent/EppClientVulnerability/EPPMac3.0.2.2005.Notarized.tar)
     - Windows: [EPPClient_v6.2.2.2005.zip](https://download.endpointprotector.com/custom_agent/EppClientVulnerability/EPPClient_v6.2.2.2005.zip)
     - Linux: Multiple links for different distributions (Ubuntu and RHEL).
4. Deployed hotfix adv-2024-002 to remediate the vulnerabilities.
5. Confirmed remediation completion on 7/10/2024.

## Root Cause
The vulnerabilities were identified in the CoSoSys Endpoint Protector software, specifically in the server and client components, which allowed for potential remote code execution.

## Solution
The issue was resolved by deploying the hotfix adv-2024-002 and applying the necessary offline patches for both the server and client components. This action mitigated the identified vulnerabilities effectively.

## Notes
- Ensure to monitor for any future vulnerabilities and apply patches promptly.
- Maintain a record of all support tickets related to vulnerabilities for tracking and compliance purposes.
- For any questions regarding the patches or deployment, contact Paul, Adrian, or Cristian.