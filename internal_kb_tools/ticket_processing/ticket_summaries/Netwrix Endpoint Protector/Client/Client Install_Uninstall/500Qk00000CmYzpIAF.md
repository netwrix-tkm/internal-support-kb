## Ticket Metadata
- **Ticket ID:** 500Qk00000CmYzpIAF
- **Case Number:** 414308
- **Status:** Closed - Resolved
- **Account/Company:** InformedDNA
- **Contact Name:** Julian Molina-Goni
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Install/Uninstall
- **Version:** Not specified

## Problem Description
The customer, InformedDNA, needed to uninstall the Endpoint Protector client software from several Windows endpoints due to an expired license and was seeking a script or commands to facilitate this process.

## Environment Details
- The customer was using Netwrix Endpoint Protector software on Windows endpoints.

## Troubleshooting Steps
1. The customer reached out to support requesting an uninstall script or MSI file for the Endpoint Protector software.
2. The support engineer confirmed the availability of a tool for Windows and requested written confirmation from the customer regarding the tool's usage.
3. The customer provided the necessary confirmation and inquired about the need for an uninstall password.
4. The support engineer clarified that the tool does not require a password and provided a download link for the uninstall tool.
5. The customer tested the tool on a test computer and confirmed successful uninstallation.
6. The support engineer addressed the customer's concerns about device blocking during the uninstallation process.

## Root Cause
The issue stemmed from the customer's need to uninstall the Endpoint Protector client software due to an expired license, which required a specific uninstall tool to be executed on the Windows endpoints.

## Solution
The support engineer provided the customer with a download link to the uninstall tool (`EppServicesZap.zip`) and confirmed that it could be run as an administrator without requiring a password. The customer successfully used the tool to uninstall the software from a test computer.

## Notes
- The customer was advised to ensure that the uninstall tool is used only on company devices and to remove it once the uninstallation task was completed.
- If USB and other device blocking were enabled by Endpoint Protector, the uninstallation would allow the devices to be used again. However, if blocking was enforced by other software, the status of those devices post-uninstallation could not be guaranteed.