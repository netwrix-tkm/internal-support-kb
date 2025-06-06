## Ticket Metadata
- **Ticket ID:** 500Qk00000CzGQrIAN
- **Case Number:** 414855
- **Status:** Closed - Resolved
- **Account/Company:** SSI Sviluppo Sistemi Informativi srl - Dis
- **Contact Name:** Massimo Chierici
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Health
- **Version:** Not specified

## Problem Description
The customer, a Netwrix partner, reported an issue while trying to install the Netwrix Endpoint Protector (EPP) appliance. The web interface was inaccessible due to an error indicating that the high-performance web server failed to start during the virtual appliance boot process.

## Environment Details
- The issue was encountered on both VMware and Hyper-V versions of the EPP appliance.
- The virtual machine (VM) was initially configured with only one network interface card (NIC).

## Troubleshooting Steps
1. The customer attempted to boot the EPP appliance on both VMware and Hyper-V platforms but encountered the same issue.
2. The support technician suggested checking the VM settings, specifically the number of network cards attached.
3. The customer confirmed that only one NIC was attached to the VM.

## Root Cause
The root cause of the issue was identified as the absence of a second network interface card (NIC) on the virtual machine. The EPP appliance requires two NICs to function correctly during the boot process.

## Solution
The issue was resolved by attaching a second network card to the virtual machine. Once the second NIC was added and configured to point to the same network, the EPP VM booted correctly, and the web interface became accessible.

## Notes
- Ensure that both network cards are attached and configured properly when setting up the EPP appliance to avoid similar issues in the future.
- It may be beneficial to document the network configuration requirements for the EPP appliance in the installation guide to assist future users.