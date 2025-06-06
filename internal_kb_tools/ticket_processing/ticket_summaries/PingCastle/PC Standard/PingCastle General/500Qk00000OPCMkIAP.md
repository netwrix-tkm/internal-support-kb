## Ticket Metadata
- **Ticket ID:** 500Qk00000OPCMkIAP
- **Case Number:** 443070
- **Status:** Closed - Resolved
- **Account/Company:** PricewaterhouseCoopers, Société coopérative
- **Contact Name:** Thomas Fargeix
- **Product:** PingCastle
- **Component:** PC Standard
- **Feature:** PingCastle General
- **Version:** 3.3

## Problem Description
The customer reported that two user accounts, whose passwords were previously synchronized with a Read-Only Domain Controller (RODC), continued to be flagged as synchronized even after being added to the `msDS-NeverRevealGroup` and having their passwords changed. This issue persisted for several months.

## Environment Details
- The issue involves user accounts in an Active Directory environment utilizing a Read-Only Domain Controller (RODC).
- The `msDS-NeverRevealGroup` attribute is used to prevent password replication for specified accounts.

## Troubleshooting Steps
1. Identified two user accounts whose passwords were previously synchronized with the RODC.
2. Added these user accounts to a group that is part of the `msDS-NeverRevealGroup` attribute.
3. Changed the passwords for the identified user accounts.
4. Waited several months to verify if the accounts were still reported as synchronized with the RODC.
5. Developed a PowerShell script to assist in troubleshooting.
6. Reviewed documentation regarding the `rODCPurgeAccount` change.

## Root Cause
The root cause of why the accounts remained reported as synchronized with the RODC after remediation steps was not definitively identified during the troubleshooting process. There was uncertainty regarding whether additional actions were required beyond adding the accounts to the denied list for password replication.

## Solution
The issue was addressed by:
- Finalizing and sharing a PowerShell script with the customer to assist in further troubleshooting.
- The customer was advised to evaluate the feasibility of implementing the `rODCPurgeAccount` change, although caution was expressed due to limited documentation on this procedure.

## Notes
- It is important to verify whether the information about the accounts is derived solely from the `msDS-RevealedUsers` attribute or if other sources are involved.
- Additional actions may be necessary to fully remove accounts from being reported as synchronized, beyond simply changing passwords and adding them to the `msDS-NeverRevealGroup`.
- Future cases should consider the potential use of the `rODCPurgeAccount` change, but thorough documentation review is recommended before implementation.