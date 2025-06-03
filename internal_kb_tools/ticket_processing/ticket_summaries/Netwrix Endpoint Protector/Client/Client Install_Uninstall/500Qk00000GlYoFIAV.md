## Ticket Metadata
- **Ticket ID:** 500Qk00000GlYoFIAV
- **Case Number:** 423219
- **Status:** Closed - Resolved
- **Account/Company:** EMSLAND-STÄRKE GMBH
- **Contact Name:** Eike Arends
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Install/Uninstall
- **Version:** NONE

## Problem Description
The customer reported an error while attempting to install the latest Endpoint Protector software on several client machines, which had the Windows firewall turned off. An error message was displayed during the installation process.

## Environment Details
- The client machines were running Windows with the firewall disabled.

## Troubleshooting Steps
1. Verified that the Windows firewall was indeed turned off on the client machines.
2. Reviewed the error message displayed during the installation (specific details not provided in the case).
3. Engaged with the customer to confirm if they were willing to temporarily enable the firewall during installation.
4. Confirmed with the customer that they were okay with enabling the firewall for the installation process.

## Root Cause
The installation error was likely caused by the Windows firewall being turned off, which may have prevented necessary network communications or access to required resources during the installation of the Endpoint Protector software.

## Solution
The issue was resolved by advising the customer to temporarily enable the Windows firewall while installing the Endpoint Protector client software. Once the installation was completed, the firewall could be configured as needed.

## Notes
- It is important to ensure that the firewall settings are appropriately configured during software installations, especially for security-related applications.
- Future installations may require similar temporary adjustments to firewall settings to avoid installation errors.