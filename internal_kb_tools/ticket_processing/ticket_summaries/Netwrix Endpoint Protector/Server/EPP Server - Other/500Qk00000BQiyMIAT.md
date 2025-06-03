## Ticket Metadata
- **Ticket ID:** 500Qk00000BQiyMIAT
- **Case Number:** 410948
- **Status:** Closed - Resolved
- **Account/Company:** ITANCIA SAS
- **Contact Name:** Massimiliano Donna
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** Not specified

## Problem Description
The customer reported an inability to access the web GUI after installing the Netwrix Endpoint Protector (EEP) demo solution on their lab environment. They encountered a connection error when attempting to access the assigned IP address.

## Environment Details
- Virtualization Tool: Hyper-V 2012 with Windows Server 2012 R2 Datacenter
- Network Configuration: Initially set to static, later changed to DHCP mode.

## Troubleshooting Steps
1. The customer removed the existing Ethernet interface and created two new ones.
2. The IP address configuration was changed from static to DHCP mode.
3. After rebooting, the device received an IP address from the DHCP server.
4. The customer attempted to access the web GUI using the assigned IP address but received a connection error.

## Root Cause
The issue stemmed from the use of an unsupported version of Hyper-V (2012) for hosting the EEP server image. The EEP solution requires Hyper-V 2016 or a supported virtualization environment.

## Solution
The support technician provided the customer with a list of supported virtualization tools and versions, confirming that Hyper-V 2012 is not compatible with the EEP solution. The technician suggested using Oracle VirtualBox as an alternative virtualization platform that is compatible with the EEP server image.

## Notes
- The customer confirmed that they would seek alternative methods to install the demo, as no workaround was available for running the EEP solution on Hyper-V 2012.
- Future users should ensure they are using a supported version of Hyper-V or consider alternative virtualization solutions to avoid similar issues.