```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000LEgrKIAT
- **Case Number:** 434054
- **Status:** Closed - Resolved
- **Account/Company:** Bank of America Corporation
- **Contact Name:** Greg Dieter
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Windows File Systems
- **Feature:** Database
- **Version:** 11.5

## Problem Description
The customer reported an issue with two fileshares on a NAS server appearing to be connected with the same file share paths. They needed assistance in investigating why StealthAudit was reporting fileshares incorrectly.

## Environment Details
- The issue involved custom views built by the Netwrix team that were not properly filtering data from the gates table, leading to incorrect permissions being displayed.

## Troubleshooting Steps
1. Executed SQL queries to identify discrepancies in share IDs and resource types.
2. Modified the customer script to filter by resource type to distinguish between folder and share resources.
3. Dropped host data from the database for affected hosts and performed rescans.
4. Reviewed custom views to determine how to correct the error in permission presentation.
5. Coordinated with the customer to ensure proper cleanup of remaining servers.

## Root Cause
The issue was caused by deleted and modified shares that retained previous IDs in the database, leading to new IDs being incorrectly assigned and causing mismatches in the reporting of fileshares.

## Solution
The resolution involved:
- Dropping the data for affected hosts from the database.
- Performing a fresh scan to ensure that the data returned was accurate and reflected the current state of the fileshares.
- The customer confirmed that the GTMO_COE fileshare was corrected, and no new corruption issues were observed after the cleanup.

## Notes
- The customer noted that the issues may have originated from the upgrade from version 11.0 to 11.5 in July 2024.
- A follow-up task was established to monitor the remaining servers for similar issues and ensure timely resolution of any new occurrences.
- It is recommended to regularly clean up old data and monitor for any discrepancies post-upgrade to prevent similar issues in the future.
```