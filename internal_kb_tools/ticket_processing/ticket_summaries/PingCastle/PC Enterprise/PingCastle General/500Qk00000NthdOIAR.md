## Ticket Metadata
- **Ticket ID:** 500Qk00000NthdOIAR
- **Case Number:** 441552
- **Status:** Closed - Resolved
- **Account/Company:** IUC Belastingdienst
- **Contact Name:** Maurice Rosmuller
- **Product:** PingCastle
- **Component:** PC Enterprise
- **Feature:** PingCastle General
- **Version:** 3.2.0.1

## Problem Description
The customer reported alerts from PingCastle indicating that "The LAN Manager Authentication Level allows the use of NTLMv1 or LM" and "Hardened Paths have been modified to lower the security level." Despite verifying that the Group Policy Object (GPO) settings were correct, the alerts persisted, leading to suspicion that PingCastle was not fully loading all GPOs.

## Environment Details
- Active Directory domain: PingCastle
- GPO settings verified and confirmed to be correct.

## Troubleshooting Steps
1. Reviewed the GPO settings in the Active Directory domain.
2. Checked the logs and GPResult provided by the customer.
3. Suggested potential reasons for the alerts, including:
   - GPO located in a parent domain but linked to the current domain.
   - Security filtering on GPO preventing access for the PingCastle account.
   - Firewall restrictions affecting access to SYSVOL.

## Root Cause
The issue was caused by the System (Computer) account used by the PingCastle scheduler lacking read permissions on some of the Group Policy Objects.

## Solution
After identifying the permission issue, the read permissions for the System (Computer) account on the affected GPOs were adjusted. Once the permissions were corrected, PingCastle began to show the correct results, resolving the alerts.

## Notes
- Ensure that the System account used by PingCastle has the necessary permissions on all relevant GPOs to avoid similar issues in the future.
- Be aware of potential limitations in PingCastle regarding GPOs located in parent domains.