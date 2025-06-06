## Ticket Metadata
- **Ticket ID:** 500Qk00000EDUkzIAH
- **Case Number:** 417657
- **Status:** Closed - Resolved
- **Account/Company:** Lhind DLH
- **Contact Name:** Fabian Schroedter
- **Product:** PingCastle
- **Component:** PC Standard
- **Feature:** PingCastle General
- **Version:** 3.2.0.1

## Problem Description
The customer reported an issue with PingCastle version 3.2.0.1 where they encountered a "Wrong User/Pass for GPO" error when attempting to access Group Policy Objects (GPOs). The login was successful using the provided credentials, but access to GPOs was denied.

## Environment Details
- **PingCastle Version:** 3.2.0.1
- **Previous Version Noted:** 2.9.2.0
- **User Credentials:** username@example.com

## Troubleshooting Steps
1. Verified that the login credentials were correct and successfully logged in.
2. Reviewed the trace.log file for error messages related to GPO access.
3. Investigated the use of the `--user` argument in the context of GPO access.
4. Discussed the implications of using the `runas` command for domain and trusted domain scenarios.
5. Explored the possibility of UNC path hardening affecting access to GPOs.

## Root Cause
The issue was identified as being related to the use of the `--user` argument, which is discouraged due to SYSVOL hardening that requires integrity. This hardening causes problems with impersonation, which is utilized by PingCastle. Additionally, if the `runas` command is not functioning properly, it indicates that the workstation must belong to the domain or a trusted domain for PingCastle to operate correctly.

## Solution
The recommended solution was to avoid using the `--user` argument and instead utilize the `runas` command to execute PingCastle under the appropriate identity. If `runas` is not viable, the user was advised to right-click the program to run it under another identity. This approach resolved the access issues with GPOs.

## Notes
- It is important to ensure that the workstation is part of the domain or a trusted domain when using PingCastle.
- Future users should be aware that GPO access may be restricted due to SYSVOL hardening, and using the `--user` argument can lead to access denial.
- For centralized scanning of Active Directories, consider the implications of UNC path hardening, as it may limit access in non-domain joined scenarios.