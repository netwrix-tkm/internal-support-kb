## Ticket Metadata
- **Ticket ID:** 500Qk00000KcYJhIAN
- **Case Number:** 432135
- **Status:** Closed - Resolved
- **Account/Company:** Warwick Investment Group
- **Contact Name:** Jordan White
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Upgrade
- **Version:** 14.04 LTS

## Problem Description
The customer inquired about the EndPoint Protector (EPP) VM running on Ubuntu 14.04 LTS, specifically regarding the end of support (EoS) scheduled for April 2024. They requested information to facilitate their migration to a new appliance.

## Environment Details
- **Operating System:** Ubuntu 14.04 LTS
- **Network Configuration:** VMs configured with both static and DHCP IP addresses.

## Troubleshooting Steps
1. Customer reported that the web server was not starting on the VM.
2. Confirmed that both VMs (native import and manual VM creation with attached VHD) were reachable via ping.
3. Verified that MAC addresses matched the VMs in the ARP table.
4. Customer attempted various network configurations without success.
5. Technical support suggested ensuring the VM had exactly two network adapters, both set to bridged mode.

## Root Cause
The issue was identified as being related to the web server (nginx) not starting due to a missing or misconfigured network interface card (NIC). In previous cases, similar issues arose when the VM did not have the required network configuration.

## Solution
The problem was resolved by configuring the VM to have a second NIC adapter, ensuring both NICs were set to bridged mode. This configuration allowed the web server to start successfully, enabling access to the web interface.

## Notes
- Ensure that any VM running the EPP has at least two network adapters configured correctly to avoid similar issues in the future.
- Monitor the support status of the operating system, as Ubuntu 14.04 LTS will reach EoS in April 2024, necessitating migration to a supported version.