## Ticket Metadata
- **Ticket ID:** 500Qk00000DDVsvIAH
- **Case Number:** 415327
- **Status:** Closed - Resolved
- **Account/Company:** Nixon Peabody LLP
- **Contact Name:** Danielle Rochford
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Upgrade
- **Version:** 6.2.2.2005

## Problem Description
The customer, Paul Goyette, was attempting to install the latest client version 6.2.2.2005 using specific command-line switches but encountered issues when trying to specify the EPP server, default policy, and add-ons during the installation process.

## Environment Details
- Client version: 6.2.2.2005
- Installation files: 
  - `EPPClientSetup.6.2.2.2005_x86_64_[a=10.10.3.248,d=FIRMDefault,o=0,n=0].msi`
  - `EPPClientSetup_SSB.6.2.2.2005_x86_64_[a=10.10.3.248,d=FIRMDefault,n=0].msi`
- Installation method: MSI file installation

## Troubleshooting Steps
1. Downloaded and unzipped the `EPPClient_v6.2.2.2005.zip` file.
2. Attempted to install the `EPPClientSetup_x86_64.msi` file without the specified switches.
3. Tried renaming the MSI file to `EPPClientSetup.6.2.2.2005_x86_64` to see if it would allow the use of the switches.
4. Sought assistance from technical support regarding the installation process.

## Root Cause
The issue stemmed from the absence of an Offline Client patch that was necessary for the installation of the EPP client version 6.2.2.2005 with the specified command-line switches.

## Solution
The resolution involved the following steps:
1. Download the Offline Client patch from the provided link: 
   ```
   http://download.endpointprotector.com/offline_agent_patches/MP-HWA-EPP4-U0088-M0002.tar.gz
   ```
2. Navigate to the Dashboard -> Live Update -> Offline Patch Uploader.
3. Upload the downloaded Offline Client patch.
4. Wait for a confirmation message indicating successful upload.
5. Verify the installation completion in the Dashboard -> Live Update section.
6. Check the System Configuration -> Client Software Upgrade to confirm the presence of the updated EPP clients.

## Notes
- Ensure that the Offline Client patch is downloaded and uploaded before attempting to install the client software with specific switches.
- Future installations should verify the availability of necessary patches to avoid similar issues.