## Ticket Metadata
- **Ticket ID:** 500Qk00000LmewjIAB
- **Case Number:** 435533
- **Status:** Closed - Resolved
- **Account/Company:** Halodata International Pte Ltd
- **Contact Name:** Halodata Support Tech
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Access Error
- **Version:** NONE

## Problem Description
The customer, Viettel telecom, encountered an issue while attempting to access the Cososys server portal after importing a virtual machine file (OVF) onto their Openstack system. They received an error message and were unable to access the server portal.

## Environment Details
- The customer environment has no internet connectivity.
- The virtual machine file was downloaded from Cososys and imported into an Openstack system.

## Troubleshooting Steps
1. Verified the import process of the OVF file into the Openstack system.
2. Checked for any error messages displayed when attempting to access the Cososys server portal.
3. Reviewed the server configuration and settings to ensure compatibility with the imported virtual machine.
4. Confirmed that the environment's lack of internet connectivity was not affecting the server's functionality.

## Root Cause
The issue was primarily due to the lack of internet connectivity in the customer's environment, which likely prevented the Cososys server from properly initializing or accessing necessary resources.

## Solution
The customer resolved the issue by reverting to an on-premises setup instead of using the Openstack system. This change allowed them to access the Cososys server portal without the complications introduced by the virtual machine import.

## Notes
- Future implementations of virtual machines in environments without internet access should be carefully evaluated to ensure all dependencies and configurations are met.
- It is advisable to test the server functionality in a controlled environment with internet access before deploying in a restricted network.