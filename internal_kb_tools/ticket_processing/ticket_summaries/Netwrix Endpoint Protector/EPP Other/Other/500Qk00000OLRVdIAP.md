## Ticket Metadata
- **Ticket ID:** 500Qk00000OLRVdIAP
- **Case Number:** 442847
- **Status:** Closed - Resolved
- **Account/Company:** PEERS CONSULTORIA E SERVIÇOS
- **Contact Name:** Mauricio Rodrigues
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Other
- **Version:** 5.9.4.0

## Problem Description
The customer reported that their endpoint protection (EPP) was not functioning, and they were unable to access the admin panel. They suspected the issue might be related to the virtual machine (VM) hosting the EPP.

## Environment Details
- The EPP was running on a VM with Ubuntu version 18.04.
- The current EPP version was 5.9.4.0.
- Disk space on the system was verified to be 12G used out of 88G available.

## Troubleshooting Steps
1. Joined a remote session with the customer.
2. Restarted the VM hosting the EPP.
3. Verified that the customer could access the EPP console after the restart.
4. Confirmed that the customer had created a snapshot of the VM.
5. Upgraded the EPP appliance version to EPP 5942.
6. Discussed the customer's request to upgrade the Ubuntu version from 18.04 to the latest version.
7. Opened a new ticket for migration and server upgrade (Ticket ID: 00446163).

## Root Cause
The initial issue was resolved by restarting the VM, which restored access to the EPP console. The underlying cause of the access issue was not explicitly identified but was likely related to the VM's operational state.

## Solution
The issue was resolved by:
- Restarting the VM, which allowed the customer to regain access to the EPP console.
- Upgrading the EPP appliance to version 5942 as per the customer's request.

## Notes
- The customer expressed a desire to upgrade the Ubuntu version from 18.04 to the latest version in the future.
- A follow-up ticket was opened for the migration and server upgrade, indicating ongoing support for the customer's infrastructure needs.
- It is important to ensure that snapshots are created before making significant changes to the VM or EPP configurations to facilitate recovery if issues arise.