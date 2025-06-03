## Ticket Metadata
- **Ticket ID:** 500Qk00000NBBSkIAP
- **Case Number:** 439637
- **Status:** Closed - Resolved
- **Account/Company:** University of Texas Health Science Center in Houston
- **Contact Name:** Joseph Valle
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Install/Uninstall
- **Version:** 10.1

## Problem Description
The customer reported an issue where a group of computers could not switch to a new Endpoint Protector (EPP) department with different settings. After uninstalling the original client and installing the new client, the old department code persisted.

## Environment Details
- The customer utilized the uninstall tool from the Endpoint Protector website to remove the original client.
- The issue was observed across multiple computers.

## Troubleshooting Steps
1. Used the uninstall tool from [Endpoint Protector](http://download.endpointprotector.com/debug_agent/epp_uninstall.zip) to remove the original client.
2. Attempted to reinstall the branded EPP client, but the old department code remained.
3. Conducted a remote session with the customer to further investigate the issue.
4. Provided a silent uninstall script to ensure complete removal of the old client.
5. Reinstalled the branded EPP client after the silent uninstall.

## Root Cause
The root cause of the issue was that the original client was not completely uninstalled, leading to residual settings that retained the old department code.

## Solution
The issue was resolved by:
- Providing the customer with a silent uninstall script to ensure that the original client was fully removed.
- Following the silent uninstall, the branded EPP client was successfully reinstalled, which allowed the new department settings to take effect.

## Notes
- It is recommended to always ensure that the previous client is completely uninstalled before installing a new version to avoid similar issues.
- The customer was advised to test the solution on a larger number of computers after the successful resolution on the initial machines.
- Older EPP clients are compatible with newer EPP server versions, but upgrading clients is recommended to benefit from the latest features and fixes.