## Ticket Metadata
- **Ticket ID:** 500Qk00000KhaSyIAJ
- **Case Number:** 432488
- **Status:** Closed - Resolved
- **Account/Company:** Regina Maria
- **Contact Name:** Cristian Voicu
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Upgrade
- **Version:** 5.9.4.1

## Problem Description
The Regina Maria team reported very slow progress on the Client Software Upgrade job while attempting to upgrade their clients to version 6.2.4.1006 to resolve interoperability issues with Bitdefender.

## Environment Details
- **Current Server Version:** 5.9.4.1
- **Target Client Version:** 6.2.4.1006

## Troubleshooting Steps
1. Confirmed the creation of the upgrade job under System Configuration > Client Software Upgrade.
2. Verified the server version to ensure compatibility with the client upgrade.
3. Communicated with the customer regarding the status of the upgrade job.
4. Suggested uninstalling the client from endpoints and redeploying the latest version via Intune.
5. Discussed the need to wait for the next server release to perform the client upgrade.

## Root Cause
The slow progress of the Client Software Upgrade job was attributed to the existing server version (5.9.4.1) not being compatible with the new client version (6.2.4.1006) until a new server release was available.

## Solution
The issue was resolved by advising the customer to uninstall the client from all endpoints (except for approximately 250 that were not visible in the console) and to deploy the latest client version via Intune. The ticket was closed with the understanding that the customer would test the client upgrade again once the next patch was released.

## Notes
- It is important to keep in mind that client upgrades may require a new server release to be effective.
- Future tickets related to client upgrades should consider the server version and its compatibility with the desired client version.
- The customer was advised to open a new ticket if issues persisted after the next client upgrade attempt.