```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000OKXoPIAX
- **Case Number:** 442798
- **Status:** Closed - Resolved
- **Account/Company:** Hawaii Pacific Health
- **Contact Name:** Steven Schiesl
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for NetApp
- **Feature:** Data Collection
- **Version:** 12.0.0.1053

## Problem Description
The customer reported an error during the FSAA Bulk Import process, specifically a MERGE statement error indicating that the same row was attempted to be updated or deleted multiple times. This issue was isolated to one host, DRF-ERNIE2, while other similar hosts were functioning correctly.

## Environment Details
- The issue occurred on a NetApp server.
- The SQL Server version in use was 2019 Standard (64-bit).
- The problem arose after an upgrade to version 12.0.

## Troubleshooting Steps
1. **Initial Review**: Analyzed logs provided by the customer, which indicated a MERGE statement error.
2. **Log Collection**: Requested additional logs including FSAA scan and bulk import job exports, proxy logs, and T2 database files.
3. **Debugging**: Ensured that both the FSAA scan and bulk import jobs were set to DEBUG level for detailed logging.
4. **Repair Attempt**: Instructed the customer to run a repair on the database for the problematic host.
5. **Testing in Lab**: Copied the T2s and the client's bulk import job to a lab environment and successfully ran the bulk import without issues.
6. **Escalation**: Escalated the ticket to Tier 2 support for further investigation into the root cause.

## Root Cause
The root cause was identified as a conflict in the database where multiple source rows matched a single target row during the MERGE operation. This was likely exacerbated by issues stemming from the recent upgrade to version 12.0, which included changes to the database schema.

## Solution
The issue was resolved by applying a hotfix provided by development. After the hotfix was applied, the customer was instructed to rerun the repair tool and then the bulk import job, which successfully completed without errors.

## Notes
- It is important to monitor for similar issues after upgrades, especially when schema changes are involved.
- Ensure that all relevant logs are collected and analyzed thoroughly to identify potential conflicts in the database.
- Future cases should consider running the repair tool as a first step if similar MERGE statement errors are encountered.
```