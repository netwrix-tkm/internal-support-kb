```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000NRDDlIAP
- **Case Number:** 440354
- **Status:** Closed - Resolved
- **Account/Company:** Netwrix Technical Support
- **Contact Name:** Tay Caliguiri
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Windows File Systems
- **Feature:** Access Auditing
- **Version:** 11.6

## Problem Description
The customer reported that the FSAA (File System Access Auditing) scoping was not functioning as expected, resulting in all shares being collected instead of only the specified DFS (Distributed File System) shares.

## Environment Details
- **Product Version:** 11.6
- **Build Number:** 138
- **Previous Working Version:** NEA 12

## Troubleshooting Steps
1. Dropped all FS data for the host to ensure a clean slate.
2. Configured all shares to be excluded and set DFS only scoping.
3. Ran FSAA and performed a Bulk Import.
4. Verified the results, which showed all top-level shares being collected, not just the DFS ones.

## Root Cause
The root cause of the issue was not definitively identified. However, it was noted that the problem may have been related to the interaction between fully qualified domain names (FQDN) and short names being used simultaneously.

## Solution
The issue was resolved after repeatedly dropping the data approximately ten times, which allowed the system to scan and align appropriately. This process cleared any potential stuck states that were causing the unexpected behavior.

## Notes
- It is recommended to ensure that both FQDN and short names are not used simultaneously in future configurations to avoid similar issues.
- If the problem recurs, consider escalating to R&D for further investigation.
- Always verify that all relevant data has been cleared before re-scanning to prevent residual data from affecting results.
```