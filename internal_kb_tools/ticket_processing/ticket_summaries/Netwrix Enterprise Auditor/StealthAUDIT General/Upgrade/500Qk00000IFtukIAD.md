## Ticket Metadata
- **Ticket ID:** 500Qk00000IFtukIAD
- **Case Number:** 426924
- **Status:** Closed - Resolved
- **Account/Company:** Nexidia
- **Contact Name:** Angie Sawyer
- **Product:** Netwrix Enterprise Auditor
- **Component:** Upgrade
- **Feature:** Upgrade
- **Version:** 11.6.0.122

## Problem Description
The customer reported issues with scheduled jobs not starting after upgrading Netwrix Enterprise Auditor from version 11.5 to 11.6. While jobs could be started manually, they failed to initiate automatically through the Task Scheduler.

## Environment Details
- Upgraded from Netwrix Enterprise Auditor version 11.5 to 11.6.
- The upgrade included configuring both PubReports and AIC to use SSL with an existing certificate.
- The scheduled account was initially removed from role-based access.

## Troubleshooting Steps
1. Verified that the scheduled jobs were not starting automatically.
2. Confirmed that the Task Scheduler showed tasks as starting and completing without errors.
3. Reviewed permissions for the scheduled account, which appeared to have the necessary rights.
4. Conducted a meeting to investigate further.
5. Re-added the scheduled account back into role-based access as an admin.
6. Tested the scheduled jobs after re-adding the account.

## Root Cause
The scheduled account was removed from role-based access, which prevented it from executing scheduled tasks properly after the upgrade.

## Solution
The issue was resolved by re-adding the scheduled account back into role-based access with administrative privileges. After this change, the scheduled jobs began to function correctly.

## Notes
- Ensure that any account used for scheduling tasks has the necessary permissions, including:
  - "Create Files/Write Data" rights on the Windows Task folder and System32 Task folder.
  - Membership in the 'Log on as a Batch Job' local policy.
- It is important to maintain proper role-based access for service accounts to avoid similar issues in the future.