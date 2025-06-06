## Ticket Metadata
- **Ticket ID:** 500Qk00000OwTOsIAN
- **Case Number:** 444568
- **Status:** Closed - Resolved
- **Account/Company:** Stamford Health
- **Contact Name:** Wajid Fazal
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Active Directory
- **Feature:** Inventory
- **Version:** 11.6

## Problem Description
The customer reported that the AD Summary scan job was failing, with error messages indicating issues related to duplicate domain entries. The customer requested assistance in reviewing the problem, as evidenced by screenshots provided.

## Environment Details
- The issue occurred after an upgrade of the Netwrix Auditor, although no specific timeline or prior troubleshooting steps were documented.
- The scan job was configured to include multiple domain controllers per domain.

## Troubleshooting Steps
1. Opened the Netwrix Enterprise Auditor console.
2. Navigated to the AD Summary scan job.
3. Assigned a host list that included multiple domain controllers per domain.
4. Ran the AD Summary scan job.
5. Observed job failure and reviewed the error messages generated.

## Root Cause
The failure of the AD Summary scan job was caused by a record of a replaced domain controller (DC) that was still using the same fully qualified domain name (FQDN). This record was being picked up by the host discovery query, leading to duplicate domain entries during the scan job.

## Solution
The issue was resolved by performing the following steps:
1. Removed the DNS entry and FQDN associated with the replaced domain controller and its respective IP address.
2. Modified the host list to target the currently active domain controller.

These actions eliminated the duplicate domain error messages, allowing the AD Summary scan job to complete successfully.

## Notes
- It is important to ensure that any replaced domain controllers are properly removed from DNS and host lists to prevent similar issues in the future.
- The customer did not attend a scheduled meeting, which delayed further investigation; timely communication is crucial for resolving such issues efficiently.
- Future upgrades of the Auditor should be monitored closely for any potential impacts on existing configurations.