## Ticket Metadata
- **Ticket ID:** 500Qk00000PPYzNIAX
- **Case Number:** 445797
- **Status:** Closed - Resolved
- **Account/Company:** Techsol Infosec
- **Contact Name:** Umesh Shetty
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Access Error
- **Version:** 5.9.4.1

## Problem Description
The customer, Choice International, reported a server outage with a corrupted Ubuntu operating system, specifically indicating an issue with `/dev/sda4 recovering journal`. They requested the default root ID and password for access.

## Environment Details
- Operating System: Ubuntu
- Product: Netwrix Endpoint Protector
- Previous Server Configuration: Failed virtual machine with the same IP as the new one.

## Troubleshooting Steps
1. Attempted to access the backend of the server through the EPP VM console.
2. Restarted the machine; the issue persisted.
3. Tried to access the GRUB menu; selecting boot options returned to the initial page.
4. Shut down the old machine and created a new virtual machine.
5. Configured the new machine with the same IP address as the original server.
6. Reinstalled the SSL certificate.
7. Accessed the EPP UI using both IP and FQDN.
8. Uploaded the product license.
9. Updated the EPP server to the latest version (5.9.4.1).

## Root Cause
The root cause of the issue was identified as a corrupted Ubuntu operating system on the original server, which rendered it inaccessible and non-functional.

## Solution
The issue was resolved by provisioning a new virtual machine to replace the failed Endpoint Protector server. The new VM was configured with the same IP address as the original server, the SSL certificate was reinstalled, and the Endpoint Protector UI became accessible via both IP and FQDN. The product license was re-uploaded, and the server was updated to the latest version (5.9.4.1). After these steps, normal access and functionality were restored, allowing the customer to proceed with client updates.

## Notes
- Ensure to keep a backup of server configurations and data to prevent similar issues in the future.
- Regularly update the server to the latest version to mitigate potential vulnerabilities and issues.
- Document any changes made during troubleshooting for future reference.