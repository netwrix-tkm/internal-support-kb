## Ticket Metadata
- **Ticket ID:** 500Qk00000IdtqJIAR
- **Case Number:** 427860
- **Status:** Closed - Resolved
- **Account/Company:** Eglin Federal Credit Union
- **Contact Name:** Glenda Coley
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for SQL
- **Feature:** Data Collection
- **Version:** 11.6

## Problem Description
The customer reported that SQL data was not being reliably collected, with specific errors occurring during SQL instance discovery and collection jobs.

## Environment Details
- SQL Server instances were hosted on various Windows machines.
- Issues were related to network connectivity and database permissions.

## Troubleshooting Steps
1. Investigated the error in the `PasswordIssues` job, which was failing to truncate the `SA_Password_List` table due to a login failure for an unspecified user.
2. Reviewed logs for SQL jobs that indicated they had never run, despite having data.
3. Attempted to change the host list for SQL jobs but observed no improvement.
4. Corrected firewall settings and permissions for several SQL servers that were not responding:
   - Ensured the correct ports were open.
   - Verified SQL services were enabled on the appropriate network protocols.
   - Adjusted firewall rules to allow specific IPs.
5. Created a dynamic SQL host list to automate the discovery of SQL servers.
6. Validated that SQL jobs were running as expected and monitored for errors.

## Root Cause
The primary issue was related to misconfigured permissions and network settings on the SQL servers, which prevented successful data collection. The `PasswordIssues` job specifically failed due to an attempt to connect without a valid user.

## Solution
- A dynamic filter for servers running SQL was created and set up to run against the SQL database scans.
- The SQL Instance Discovery Job was modified to use an active list of all Windows hosts, ensuring new SQL hosts were automatically discovered.
- All SQL Collection jobs were configured to target only the SQL servers identified by the SQL Instance Discovery Job.
- After implementing these changes, all previously reported errors cleared, and SQL data collection became reliable.

## Notes
- Ensure that proper permissions and firewall rules are in place for SQL servers to avoid similar issues in the future.
- Regularly review and update the dynamic SQL host list to accommodate any changes in the environment.
- Monitor SQL jobs closely after configuration changes to confirm they are running as expected.