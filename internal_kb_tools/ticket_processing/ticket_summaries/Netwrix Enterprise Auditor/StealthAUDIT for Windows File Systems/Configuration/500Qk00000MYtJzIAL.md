## Ticket Metadata
- **Ticket ID:** 500Qk00000MYtJzIAL
- **Case Number:** 437726
- **Status:** Closed - Resolved
- **Account/Company:** SpecialtyCare
- **Contact Name:** Sean Dion
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Windows File Systems
- **Feature:** Configuration
- **Version:** 11.5.0.240

## Problem Description
The customer reported that a DFS server, which is part of the "ALL WINDOWS SERVERS (NO DCS)" host group, was not being scanned by the file system jobs, resulting in no data being collected.

## Environment Details
- The server in question is new and was added to the environment a few months prior to the ticket being opened.
- The version of the Netwrix Enterprise Auditor in use is 11.5.0.240.

## Troubleshooting Steps
1. Verified that StealthAudit was able to communicate with the server.
2. Confirmed that the DFS server was included in the appropriate host group.
3. Reviewed logs from the last run, which indicated errors related to the DFS scan.
4. Scheduled a meeting to further investigate the issue with full admin access to the Netwrix Enterprise Auditor server.
5. Updated the FSDFS job to point to a Domain Controller (DC) instead of a list of hosts.

## Root Cause
The issue was caused by the FSDFS job being incorrectly configured to reference a list of hosts rather than a Domain Controller. This misconfiguration prevented the job from correctly populating data for the DFS server.

## Solution
The issue was resolved by updating the FSDFS job configuration to point to a Domain Controller. After this change, the 0-FSDFS System Scans completed successfully, and the missing file server began reporting under the necessary job group. Data for the previously missing server was confirmed to be present within the FSAA Tables and the Access Information Center (AIC).

## Notes
- It is unclear why changing the job to reference a DC resolved the issue, as the previous configuration should have worked.
- The ticket can be reopened within 30 days of closure if any related errors return by replying to the closure email.
- Future configurations should ensure that DFS jobs are correctly pointed to a Domain Controller to avoid similar issues.