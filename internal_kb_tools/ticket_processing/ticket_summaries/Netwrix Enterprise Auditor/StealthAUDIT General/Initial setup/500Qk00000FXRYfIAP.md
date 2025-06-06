## Ticket Metadata
- **Ticket ID:** 500Qk00000FXRYfIAP
- **Case Number:** 420475
- **Status:** Closed - Resolved
- **Account/Company:** G-III Apparel Group
- **Contact Name:** David Wong
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Initial setup
- **Version:** 11.6

## Problem Description
The customer reported an error during the SEEK Bulk Import job, specifically a UNIQUE constraint failure related to the `DLPID` in the `TBL_FSAA_ResourceMap` table.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Collector Code:** StealthAUDIT General
- **Product Version:** 11.6

## Troubleshooting Steps
1. Ran a repair on the host that was experiencing errors.
2. Executed the `FS_SDD_DELETE` job to clear the DLP data from the T1 database.
3. Deleted all DPL data related to the T2 database from the two hosts that were encountering issues.
4. Started both jobs based on their schedules and awaited results.

## Root Cause
The issue was caused by a UNIQUE constraint violation in the SQLite database, specifically indicating that there were duplicate entries for the `DLPID` in the `TBL_FSAA_ResourceMap` table.

## Solution
The resolution involved:
- Repairing the affected host.
- Clearing the DLP data from the T1 database using the `FS_SDD_DELETE` job.
- Deleting all DPL data related to the T2 database from the problematic hosts.
After these actions were taken, the SEEK Bulk Import job was able to proceed without errors.

## Notes
- Ensure that there are no duplicate entries for `DLPID` in the `TBL_FSAA_ResourceMap` table to prevent similar UNIQUE constraint violations in the future.
- Regularly monitor the database for integrity issues and perform maintenance as necessary to avoid disruptions during bulk import jobs.