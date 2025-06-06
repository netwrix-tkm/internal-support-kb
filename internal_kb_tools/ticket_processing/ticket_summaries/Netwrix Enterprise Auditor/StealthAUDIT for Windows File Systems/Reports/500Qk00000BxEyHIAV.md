## Ticket Metadata
- **Ticket ID:** 500Qk00000BxEyHIAV
- **Case Number:** 412142
- **Status:** Closed - Resolved
- **Account/Company:** Columbia University
- **Contact Name:** Iurii Druchuk
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Windows File Systems
- **Feature:** Reports
- **Version:** 11.6

## Problem Description
The Broken Inheritance Analysis job was failing to complete within the expected time frame, escalating from an average of 2 hours and 30 minutes to over 40 hours before timing out. The job appeared to get stuck on a specific task, leading to repeated timeouts and eventual job abortion.

## Environment Details
- SQL Server resources: 400GB total space with approximately 210GB free.
- The job was configured to analyze around 2 million files and folders.
- The database was set to Simple Recovery Mode.
- The tempdb was initially sized at 12GB with autogrowth settings, but had been adjusted to allow for more space.

## Troubleshooting Steps
1. Increased the timeout period from 1440 to 2880 minutes, which temporarily reduced the frequency of timeouts but did not resolve the underlying issue.
2. Limited the scope of the analysis tasks to only the file server by modifying the SQL script to include a WHERE clause.
3. Reviewed SQL resources and configurations, including the size of tempdb and EnterpriseAuditor log files.
4. Collected DEBUG level logs and screenshots of error messages for further analysis.
5. Conducted a meeting to discuss findings and next steps with the technical support team.

## Root Cause
The primary cause of the issue was identified as the addition of workstation scanning to the Broken Inheritance job, which significantly increased the workload and processing time. Additionally, the SQL Server's tempdb was not adequately sized to handle the increased demands, leading to performance degradation and eventual job failures.

## Solution
The issue was resolved by scoping the analysis tasks to only the file server, which reduced the workload significantly. This was achieved by modifying the SQL script to include a WHERE clause when joining the FSAA_Hosts table. This adjustment allowed the job to complete successfully without timing out.

## Notes
- It is crucial to monitor the size and performance of the tempdb in SQL Server, especially when running large analysis jobs.
- Future configurations should consider the workload implications of adding additional scanning tasks, particularly for environments with a large number of files and folders.
- Regular reviews of job performance and SQL resource allocation can help preemptively identify potential issues before they escalate.