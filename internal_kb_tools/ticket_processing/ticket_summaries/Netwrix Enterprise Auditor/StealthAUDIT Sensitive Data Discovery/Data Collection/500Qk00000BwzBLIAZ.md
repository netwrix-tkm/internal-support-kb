```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000BwzBLIAZ
- **Case Number:** 412144
- **Status:** Closed - Resolved
- **Account/Company:** Axos Bank
- **Contact Name:** Alan A. Moreno
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT Sensitive Data Discovery
- **Feature:** Data Collection
- **Version:** 11.6

## Problem Description
The customer reported that SQL jobs for sensitive data scans were not executing as scheduled or manually.

## Environment Details
- The original NEA host had operating system issues that could not be resolved.
- The customer was using version 11.6 of the Netwrix Enterprise Auditor.

## Troubleshooting Steps
1. **Initial Investigation:** Verified that the SQL jobs were not running and checked for any error messages.
2. **Service Account Check:** Discovered that the service account used for the jobs reported an "Access Denied" error.
3. **Access Verification:** Advised the customer to verify the access of the service account to the reported domain controllers (DCs).
4. **Hostlist Configuration:** The customer created a hostlist with a single host and attempted to run the job group again, but the sensitive data scan still did not run.
5. **Job Execution Monitoring:** Noted that jobs were showing as "running" in the scheduled section but did not appear in the running instances.
6. **Error Logging Review:** Reviewed logs and found that many tasks were still showing as "running" from previous dates.
7. **Add-on Installation:** Identified that the Sensitive Data add-on needed to be installed on the target hosts for the scans to function properly.
8. **Timeout Adjustment:** Increased the timeout for SQL storage connection to accommodate longer running scans.
9. **Testing:** Ran test SQL SDD scans against test hosts to verify functionality.

## Root Cause
The issue was primarily due to the absence of the Sensitive Data add-on on the target hosts, which was necessary for the sensitive data scans to execute. Additionally, access issues with the service account contributed to the failures.

## Solution
- Migrated to a new host and installed the necessary Sensitive Data add-on.
- Adjusted the timeout settings for SQL jobs to accommodate longer execution times.
- Verified that the SQL jobs could run successfully after these changes were implemented.

## Notes
- Ensure that the Sensitive Data add-on is installed on all target hosts before attempting to run sensitive data scans.
- Monitor the execution times of SQL jobs, especially when running multiple jobs in succession, to avoid timeout issues.
- Consider scheduling jobs to run earlier to prevent overlaps that could lead to failures or incomplete logs.
```