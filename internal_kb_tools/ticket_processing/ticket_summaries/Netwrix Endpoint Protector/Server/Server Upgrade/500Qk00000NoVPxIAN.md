## Ticket Metadata
- **Ticket ID:** 500Qk00000NoVPxIAN
- **Case Number:** 441265
- **Status:** Closed - Resolved
- **Account/Company:** Hitachi Systems India Pvt. Ltd.
- **Contact Name:** Divya Ramachandran S
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Upgrade
- **Version:** None

## Problem Description
The customer inquired whether the Linux agent needed to be upgraded after upgrading their Endpoint Protector Server to version 5.9.4. They had recently upgraded their Linux agent to SLED 15 and wanted clarification on the necessity of further upgrades.

## Environment Details
- **Operating System:** SUSE Linux Enterprise Desktop (SLED) 15 SP3 and SP5
- **Current Agent Version:** 2.4.4.1

## Troubleshooting Steps
1. Confirmed the current version of the Endpoint Protector Client installed on the SLED endpoint machines.
2. Recommended that the Endpoint Protector Client be upgraded alongside the Endpoint Protector Server, as they are developed and released together.
3. Verified that the current agent version (2.4.4.1) was the latest build released under Endpoint Protector 5.9.4.1.
4. Advised the customer to perform a backup of their Endpoint Protector appliance before proceeding with the upgrade.

## Root Cause
The inquiry stemmed from the customer's uncertainty regarding the compatibility and necessity of upgrading the Linux agent after upgrading the server. The confusion was primarily due to the age of the SLED version and the potential lack of the latest EPP client.

## Solution
The issue was resolved by confirming that the current agent version (2.4.4.1) was indeed the latest and that it was compatible with the upgraded Endpoint Protector Server version (5.9.4.1). The customer was advised to proceed with the server upgrade, ensuring they had a backup in place.

## Notes
- It is crucial to perform a snapshot (backup) of the current state of the Endpoint Protector appliance before applying any upgrades to ensure a quick recovery in case of issues.
- Future inquiries regarding upgrades should emphasize the importance of checking compatibility between the server and client versions, especially when dealing with older operating systems.