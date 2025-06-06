```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000BZsQbIAL
- **Case Number:** 411398
- **Status:** Closed - Resolved
- **Account/Company:** Chimera Investment Corporation
- **Contact Name:** Dhruman Shah
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Upgrade
- **Version:** 11.5

## Problem Description
The customer requested assistance with upgrading their existing StealthAudit applications to the latest version of Netwrix Audit.

## Environment Details
- Previous Versions:
  - Netwrix Enterprise Auditor (NEA) formerly StealthAUDIT (SA): 11.5.0.245
  - Netwrix Access Information Center (AIC) formerly StealthAUDIT Access Information Center: 11.5.0.130
  - Netwrix Activity Monitor (NAM) formerly Stealthbits Activity Monitor: 6.0.1214
- Target Versions:
  - Netwrix Enterprise Auditor (NEA): 11.6.0.79
  - NEA Access Information Center (AIC): 11.6.0.15
  - NEA Sensitive Data Discovery (SDD): 11.6.0.12
  - Netwrix Activity Monitor (NAM): 7.0.0.3135
  - StealthINTERCEPT Agent (SIa): 7.3.9.160

## Troubleshooting Steps
1. Attempted to run `DBCC CHECKDB` and `DBCC CHECKDB(StealthAudit, REPAIR_REBUILD)` to check for database corruption.
2. Restored the database from backups, but the issue persisted.
3. Rebuilt the StealthAudit database.
4. Re-populated the host list.
5. Rebuilt the Agent connection to the DRProd host to update the NAM console and clear warnings.
6. Created a `BU_` folder under the FileSystem install path to remove duplicate jobs.
7. Confirmed the FileSystem job settings for the two file servers.
8. Scheduled the FileSystem jobs to run as needed.

## Root Cause
The root cause of the issue was identified as corruption in the StealthAudit database, which was not resolved by restoring from backups.

## Solution
The issue was resolved by:
- Upgrading the applications to the specified target versions.
- Rebuilding the StealthAudit database and re-establishing connections to the necessary hosts.
- Ensuring that the FileSystem job settings were correctly configured and scheduled.

## Notes
- Ensure that full admin access to the Netwrix Enterprise Auditor server is available during upgrades to avoid permission issues.
- It is recommended to regularly back up the database to prevent data loss in case of corruption.
- Future upgrades should follow the official upgrade instructions provided in the Netwrix documentation to minimize issues.
```