## Ticket Metadata
- **Ticket ID:** 500Qk00000EybvuIAB
- **Case Number:** 419214
- **Status:** Closed - Resolved
- **Account/Company:** Satcom Infotech
- **Contact Name:** Aakash Khantwal
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Upgrade
- **Version:** Not specified

## Problem Description
The customer requested urgent support for assigning a manual IP address to the second NIC (Network Interface Card) on a Nutanix instance, as they were engaged in an implementation activity for a major client.

## Environment Details
- **Platform:** Nutanix instance
- **NIC Configuration:** Second NIC requiring manual IP assignment

## Troubleshooting Steps
1. Reviewed the current network configuration on the Nutanix instance.
2. Attempted to assign a manual IP address to the second NIC through the backend.
3. Checked firewall settings to ensure that necessary ports were open for communication.
4. Conducted a remote session to assist with the configuration.

## Root Cause
The issue was caused by the firewall blocking port 80, which is essential for the proper communication required to assign the manual IP address to the second NIC.

## Solution
The issue was resolved by allowing port 80 in the firewall settings. This change enabled the necessary communication for the manual IP assignment to take effect on the second NIC.

## Notes
- Ensure that firewall settings are reviewed before attempting network configurations to avoid similar issues in the future.
- Document any changes made to firewall settings for future reference and troubleshooting.