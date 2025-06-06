## Ticket Metadata
- **Ticket ID:** 500Qk00000IOJOvIAP
- **Case Number:** 427300
- **Status:** Closed - Resolved
- **Account/Company:** Axos Bank
- **Contact Name:** Alan A. Moreno
- **Product:** Netwrix Enterprise Auditor
- **Component:** Database
- **Feature:** SQL Jobs
- **Version:** 11.6

## Problem Description
The customer reported that the SQL job "JOB_0-SQL DROP" was unable to complete execution, running for over 20 hours without finishing. This issue forced the customer to kill the job multiple times over two consecutive days.

## Environment Details
- The issue occurred in the SQL database associated with the Netwrix Enterprise Auditor.
- The job was blocking other NEA tasks from running due to resource locks.

## Troubleshooting Steps
1. The customer identified that multiple blocking processes in the SQL database were preventing the job from completing.
2. The DBA team was involved to kill the tasks that were blocking the SQL job.
3. After clearing the stuck jobs, the SQL job was re-executed successfully.

## Root Cause
The SQL job was being blocked by another task in the database that was locking resources, preventing the drop table command from proceeding. The specific SQL query causing the blockage was identified as:
```sql
DELETE [SA_SQLServer_EffectiveRoleMembership];
```

## Solution
The issue was resolved by killing the blocking tasks in the SQL database. Once the blocking processes were terminated, the SQL job was able to execute successfully without further issues.

## Notes
- It is important to monitor SQL jobs for potential blocking issues in the future.
- Consider implementing alerts for long-running jobs to proactively address similar issues before they escalate.
- The case can be reopened if related issues arise in the future.