# Ticket Metadata
- **Ticket ID:** 500Qk00000EfacHIAR
- **Case Number:** 418549
- **Status:** Closed - Resolved
- **Account/Company:** Engie
- **Contact Name:** Roger CHHIN
- **Product:** PingCastle
- **Component:** PC Enterprise
- **Feature:** PingCastle General
- **Version:** 3.2.0.1

## Problem Description
The customer reported a vulnerability related to the A-NoNetSessionHardening rule in PingCastle. It was identified that the vulnerability is corrected in Windows Server 2022 and Windows 10/11 when updated, but persists in older versions such as Windows Server 2012R2, even when updated.

## Environment Details
- **Affected Operating Systems:** Windows Server 2012R2 and earlier versions.
- **Corrected Operating Systems:** Windows Server 2022, Windows 10/11 (when updated).

## Troubleshooting Steps
1. The customer’s colleague, Olivier, analyzed the situation and confirmed the presence of the vulnerability in older OS versions.
2. Discussion regarding the applicability of the rule to different OS versions was initiated.
3. Consideration of adjustments to the rule for future releases was discussed.

## Root Cause
The root cause of the issue was identified as the A-NoNetSessionHardening rule not accounting for older operating system versions, which still exhibit the vulnerability despite being updated.

## Solution
The resolution involved planning a rule adjustment for the next release of PingCastle. However, it was noted that changes could not be made to the upcoming release due to timing constraints.

## Notes
- Future releases of PingCastle should consider the inclusion of older OS versions in the rule adjustments to prevent similar vulnerabilities from being overlooked.
- It is important to communicate to users that the current version of the rule may not adequately protect older operating systems.