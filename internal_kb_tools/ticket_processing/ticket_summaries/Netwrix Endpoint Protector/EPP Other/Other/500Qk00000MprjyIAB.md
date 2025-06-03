## Ticket Metadata
- **Ticket ID:** 500Qk00000MprjyIAB
- **Case Number:** 438505
- **Status:** Closed - Resolved
- **Account/Company:** BAE Systems UK
- **Contact Name:** Paul Salisbury
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Other
- **Version:** EPPClient_rhel_8.10_v2.4.3.1007

## Problem Description
The customer reported that after installing the EPPClient_rhel_8.10_v2.4.3.1007 client on their Red Hat/Alma/Rocky PCs, the appliance was unable to detect the clients despite successful pings and no firewall restrictions.

## Environment Details
- Operating Systems: Red Hat, AlmaLinux, Rocky Linux
- Client Version: EPPClient_rhel_8.10_v2.4.3.1007
- Previous Client Version: v1.9.1.1 (which was able to communicate with the appliance)

## Troubleshooting Steps
1. Confirmed that the machines could ping the appliance.
2. Verified that there were no firewall ports blocking traffic.
3. Installed the original Linux client (v1.9.1.1) to test communication, which was successful.
4. Sent the latest client version to the customer.
5. Instructed the customer to modify the `options.sh` file by uncommenting specific lines (4, 5, 7, 8, 10, 11) and ensuring the server's IP, port, and department were correctly set.
6. Advised the customer to uninstall the old client before installing the new one.

## Root Cause
The issue was caused by not all necessary lines being uncommented in the `options.sh` configuration file of the client, which prevented proper communication with the appliance.

## Solution
After the customer uncommented the required lines in the `options.sh` file and reinstalled the client, the communication issue was resolved, and the client was successfully detected by the appliance.

## Notes
- Ensure that all necessary lines in the `options.sh` file are uncommented during client installation to avoid similar issues in the future.
- Always verify that the server's IP, port, and department settings are correctly configured in the `options.sh` file.
- Confirm that there are sufficient licenses available in the System Configuration before installation.