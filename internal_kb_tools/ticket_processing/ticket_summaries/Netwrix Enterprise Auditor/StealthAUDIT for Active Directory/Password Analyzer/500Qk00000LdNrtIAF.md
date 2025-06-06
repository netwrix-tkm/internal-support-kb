## Ticket Metadata
- **Ticket ID:** 500Qk00000LdNrtIAF
- **Case Number:** 435172
- **Status:** Closed - Resolved
- **Account/Company:** TeamHealth
- **Contact Name:** Filmore Thomas
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Active Directory
- **Feature:** Password Analyzer
- **Version:** 11.6

## Problem Description
The customer reported that the `AD_WeakPasswords` job fails to execute properly when run via scheduled tasks. The job logs indicate it reaches the "Beginning analysis of Active Directory accounts" step and then terminates abruptly, leaving a `running.lck` file and showing a runtime of 0 seconds in the console. The job runs successfully when executed interactively.

## Environment Details
- Visual C++ Redistributable (2015-2019) (x86) is installed on the application server.
- The issue occurs specifically with the `AD_WeakPasswords` job when run from the task scheduler.

## Troubleshooting Steps
1. Verified that the scheduled task was configured correctly.
2. Deleted and recreated the scheduled task; the issue persisted.
3. Deleted the job and re-added it from instant solutions; the issue persisted.
4. Attempted to use `procdump.exe` in the StealthAUDIT folder to generate dump files, but none were created when the task stopped.
5. Reviewed event logs during the time of the task execution; no concerning entries were found.
6. Analyzed debug logs attached to the ticket.

## Root Cause
The root cause was identified as a security tool (antivirus) that was terminating the background process of the `AD_WeakPasswords` job when it attempted to access sensitive data from Active Directory.

## Solution
To resolve the issue, the following steps were taken:
1. The security tool was temporarily disabled to allow the job to run successfully.
2. The customer was advised to implement exclusions for the security tool to prevent it from interfering with the `AD_WeakPasswords` job in the future. Detailed instructions for implementing these exclusions were provided via the following link:
   - [Antivirus Exclusions Documentation](https://helpcenter.netwrix.com/bundle/EnterpriseAuditor_11.6/page/Content/EnterpriseAuditor/Admin/Maintenance/AntivirusExclusions.htm)

## Notes
- It is crucial to ensure that any security tools in the environment are configured to allow necessary background processes to run without interruption, especially when dealing with sensitive data.
- Future cases involving scheduled tasks that fail to execute should consider potential conflicts with security software as a primary troubleshooting step.