## Ticket Metadata
- **Ticket ID:** 500Qk00000CaTarIAF
- **Case Number:** 413818
- **Status:** Closed - Resolved
- **Account/Company:** Relay Network LLC
- **Contact Name:** Andrew Siemasko
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** 5.6.0.0 - 5.9.3.0

## Problem Description
The customer reported vulnerabilities related to CoSoSys Remote Code Execution affecting both the server and client components of the Netwrix Endpoint Protector. The support ticket was created to address these vulnerabilities and ensure that all related tickets are linked and marked as solved.

## Environment Details
- **Affected Components:** 
  - Server (versions 5.6.0.0 - 5.9.3.0)
  - Client (various OS versions including MacOS, Windows, and Linux)

## Troubleshooting Steps
1. Reviewed the reported vulnerabilities and confirmed their existence in the specified versions.
2. Gathered necessary offline patches and client updates for the affected versions.
3. Provided download links for the patches and updates for server and client components:
   - **Server Patch:** 
     - [Offline patch for 5.6.0.0 - 5.9.3.0](https://download.endpointprotector.com/offline_patches/MP-HWA-EPP4-U8800.tar.gz)
   - **Client Updates:**
     - MacOS: [EPPMac3.0.2.2005.Notarized.tar](https://download.endpointprotector.com/custom_agent/EppClientVulnerability/EPPMac3.0.2.2005.Notarized.tar)
     - Windows: [EPPClient_v6.2.2.2005.zip](https://download.endpointprotector.com/custom_agent/EppClientVulnerability/EPPClient_v6.2.2.2005.zip)
     - Linux: Multiple links for various distributions (Ubuntu and RHEL):
       - [Ubuntu 22.04](https://download.endpointprotector.com/linux_agent/EppClientVulnerability/EPPClient_ubuntu_22.04_v2.4.2.1007_x86_64.tar.gz)
       - [Ubuntu 20.04](https://download.endpointprotector.com/linux_agent/EppClientVulnerability/EPPClient_ubuntu_20.04_v2.4.2.1007_x86_64.tar.gz)
       - [Ubuntu 18.04](https://download.endpointprotector.com/linux_agent/EppClientVulnerability/EPPClient_ubuntu_18.04_v2.4.2.1007_x86_64.tar.gz)
       - [RHEL 9.4](https://download.endpointprotector.com/linux_agent/EppClientVulnerability/EPPClient_rhel_9.4_v2.4.2.1007_x86_64.tar.gz)
       - [RHEL 8.10](https://download.endpointprotector.com/linux_agent/EppClientVulnerability/EPPClient_rhel_8.10_v2.4.2.1007_x86_64.tar.gz)

## Root Cause
The vulnerabilities were identified in the specified versions of the Netwrix Endpoint Protector server and client components, necessitating immediate updates to mitigate security risks.

## Solution
The issue was resolved by applying the provided offline patch to the server and updating the client components with the latest versions available for MacOS, Windows, and Linux. The server version included the necessary vulnerability fixes, ensuring that the system was secure against the reported vulnerabilities.

## Notes
- Ensure that all future support tickets related to vulnerabilities are linked to the corresponding incident for tracking purposes.
- Regularly check for updates and patches for the Netwrix Endpoint Protector to maintain security compliance.
- For any questions or further assistance, contact Paul, Adrian, or Cristian.