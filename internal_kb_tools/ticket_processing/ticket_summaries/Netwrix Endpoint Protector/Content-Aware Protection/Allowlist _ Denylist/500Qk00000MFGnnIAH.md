## Ticket Metadata
- **Ticket ID:** 500Qk00000MFGnnIAH
- **Case Number:** 436791
- **Status:** Closed - Resolved
- **Account/Company:** Segal Benz
- **Contact Name:** Anoush d'Orville
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** Allowlist / Denylist
- **Version:** Not specified

## Problem Description
The customer reported a false positive issue where users were receiving notifications despite the website `segaldev.crm.dynamics.com` being added to the allow list.

## Environment Details
- The issue was related to the Netwrix Endpoint Protector's Content-Aware Protection feature, specifically the Allowlist and Denylist policies.

## Troubleshooting Steps
1. Initial discussion with support regarding the false positive notifications.
2. Scheduled a remote session to investigate the issue further.
3. Reviewed the CAP - Deep Packet Inspection (Policy Allowlist) and Regular Expression (Policy Denylist) usage.
4. Added additional entries to the Allowlist dictionary during the remote session.
5. Performed an EPP server upgrade.
6. Initiated the EPP client software upgrade job.

## Root Cause
The root cause of the false positive notifications was not explicitly identified in the case. However, it was determined that the Allowlist configuration needed to be updated to prevent the false positives.

## Solution
The issue was resolved by:
- Adding more options to the Allowlist dictionary, which allowed the system to correctly recognize the specified website.
- Upgrading the EPP server and initiating the client software upgrade, which ensured that the latest policies and configurations were applied.

## Notes
- Ensure that the Allowlist is regularly reviewed and updated to prevent similar false positive issues in the future.
- Consider documenting any changes made to the Allowlist for future reference.
- Regularly check for updates to the EPP server and client software to maintain optimal performance and security.