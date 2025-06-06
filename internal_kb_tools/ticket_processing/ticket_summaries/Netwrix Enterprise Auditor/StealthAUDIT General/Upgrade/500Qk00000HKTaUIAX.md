## Ticket Metadata
- **Ticket ID:** 500Qk00000HKTaUIAX
- **Case Number:** 424673
- **Status:** Closed - Resolved
- **Account/Company:** Exeter Finance LLC
- **Contact Name:** Bao Luu
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Upgrade
- **Version:** 11.6

## Problem Description
The customer requested assistance with upgrading multiple Netwrix applications, including Netwrix Enterprise Auditor, Access Information Center, Active Monitor, and Sensitive Data Discovery, to their latest versions.

## Environment Details
- Current versions before upgrade:
  - Netwrix Enterprise Auditor (NEA): 11.6.0.69
  - NEA Access Information Center (AIC): 11.6.0.12
  - NEA Sensitive Data Discovery (SDD): 11.6.0.11
- Target versions after upgrade:
  - Netwrix Enterprise Auditor (NEA): 11.6.0.117
  - NEA Access Information Center (AIC): 11.6.0.25
  - NEA Sensitive Data Discovery (SDD): 11.6.0.13

## Troubleshooting Steps
1. Scheduled the upgrade for November 4, 2024, at 8 AM Central Time.
2. Ran the SA_Upgrade_Prep script to collect necessary installation configurations.
3. Increased CPU count recommendation from 8 to 16 logical cores.
4. Executed the upgrade process for the applications.
5. Monitored the Active Directory scan post-upgrade, which was running longer than expected (48 hours).
6. Investigated logs for potential deadlock issues during the scan.

## Root Cause
The prolonged Active Directory scan was caused by a deadlock situation in the SQL database, where multiple processes were competing for the same resources, leading to one process being chosen as a deadlock victim.

## Solution
- The upgrade was successfully completed, and the applications were updated to their latest versions.
- The long-running scan was resolved by terminating the conflicting job and re-running the scan, which completed successfully afterward.

## Notes
- Ensure that scheduled tasks do not overlap, especially those that may access the same database resources, to prevent deadlocks.
- Confirm that the SQL Server recovery model is set to Simple to minimize locking issues during heavy operations.
- Future upgrades should include a review of scheduled tasks to avoid conflicts during critical operations.