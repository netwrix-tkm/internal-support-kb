```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000BoZVkIAN
- **Case Number:** 411923
- **Status:** Closed - Resolved
- **Account/Company:** Government of Nova Scotia
- **Contact Name:** Rick Cluett
- **Product:** Netwrix Enterprise Auditor
- **Component:** NEA MGMT Console
- **Feature:** NEA Console
- **Version:** 11.6.0.111

## Problem Description
The customer reported that the NEA console hangs at "Testing SQL Connection" when launching the console. Although rebooting the NEA server temporarily resolves the issue, it disrupts any currently running jobs.

## Environment Details
- The issue is specific to the Health environment and does not occur in the Government environment.
- The NEA system has 32GB RAM and an 8-core CPU, dedicated solely to NEA operations.

## Troubleshooting Steps
1. Confirmed the console was hanging by checking Event ID 1002 in the Windows Application event log.
2. Rebooted the NEA server, which temporarily resolved the issue but interrupted ongoing jobs.
3. Reviewed SQL server logs and reports for any access issues during the hang.
4. Verified that antivirus exclusions were in place on the SA Console server.
5. Set the console to DEBUG mode to capture more detailed logs for future occurrences.
6. Investigated the timing of scheduled database backups and their potential correlation with the console hangs.
7. Checked for any running jobs during the time of the hang, specifically focusing on the "FS Advanced > EMC > FSAC" job.

## Root Cause
The root cause was identified as a potential conflict with stored procedures that run on application startup, which may have been causing the SQL connection to hang intermittently.

## Solution
The issue was resolved by patching the NEA to version 11.6.0.111, which corrected the hanging behavior of the console. Additionally, the team disabled certain stored procedures and jobs that were suspected of causing the issue.

## Notes
- The customer should monitor the console for any further occurrences of the issue after the patch.
- It is recommended to keep the console in DEBUG mode to capture logs if the issue reoccurs.
- Ensure that the "Usage Statistics" option remains unchecked in the application settings to avoid potential conflicts.
- The customer should coordinate with their DBA regarding the timing of SQL database backups to prevent overlaps with console operations.
```