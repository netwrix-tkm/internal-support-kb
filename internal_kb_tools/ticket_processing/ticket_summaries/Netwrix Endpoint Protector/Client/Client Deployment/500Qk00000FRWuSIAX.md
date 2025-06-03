## Ticket Metadata
- **Ticket ID:** 500Qk00000FRWuSIAX
- **Case Number:** 420336
- **Status:** Closed - Resolved
- **Account/Company:** Nixon Peabody LLP
- **Contact Name:** Paul Goyette
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Deployment
- **Version:** Not specified

## Problem Description
The customer inquired about how to verify the installation of the Outlook add-in for Netwrix Endpoint Protector. They could not find the EPP add-in in the Outlook client under "Manage Add-ins" or "Manage COM Add-ins" and sought alternative methods to check its installation status, such as checking the Windows registry.

## Environment Details
- The issue was related to the installation of the Outlook add-in for the Netwrix Endpoint Protector client.
- The customer was using a version of the software that had undergone changes in how add-ons were installed.

## Troubleshooting Steps
1. Confirmed that the customer was unable to see the EPP add-in in Outlook.
2. Advised the customer to check the installation command used for deploying the add-in.
3. Suggested that the attributes in the `msiexec` command were missing, which could prevent the add-in from being installed.
4. Provided guidance on how to structure the installation command:
   - For installation with add-ons: `EPPClientSetup.6.2.3.1010_x86_64_[a=192.168.0.0].msi`
   - For installation without specific add-ons: `EPPClientSetup.6.2.3.1010_x86_64_[a=192.168.0.0,o=0,n=0].msi`
5. Informed the customer to remove the `outlook_ext` part from the `msiexec` command.
6. Followed up with the customer to monitor and deploy the changes.

## Root Cause
The Outlook add-in was not installing because the necessary attributes were missing from the `msiexec` command used during the installation process. This change in behavior was noted to have occurred in server version v5.9.4.0.

## Solution
The issue was resolved by modifying the installation command to ensure that the required attributes were included. The customer successfully deployed the add-in using the corrected command structure, which allowed the Outlook add-in to install properly.

## Notes
- It is important to ensure that the correct attributes are included in the `msiexec` command when deploying the Outlook add-in to avoid installation issues.
- Future deployments should be monitored to confirm that the add-in appears in the Outlook client as expected.
- There is currently no dashboard or report available to check the status of the add-in installation directly.