## Ticket Metadata
- **Ticket ID:** 500Qk00000OOlejIAD
- **Case Number:** 443029
- **Status:** Closed - Resolved
- **Account/Company:** Ranger Marketing & Vertriebs GmbH
- **Contact Name:** Damian Babik
- **Product:** PingCastle
- **Component:** PingCastle General
- **Feature:** PingCastle General
- **Version:** 3.3

## Problem Description
The customer reported an HTTP Error 500.31 indicating a failure to load the ASP.NET Core runtime. The error message suggested that the specified version of the Microsoft.NETCore.App or Microsoft.AspNetCore.App was not found.

## Environment Details
- **Application:** PingCastlePro.dll
- **Architecture:** x64
- **Required Framework Version:** Microsoft.NETCore.App version 8.0.15
- **Installed Framework Versions:**
  - 6.0.30
  - 8.0.5
- **.NET Location:** C:\Program Files\dotnet

## Troubleshooting Steps
1. Checked the system event log for error messages.
2. Enabled logging for the application process' stdout messages.
3. Attached a debugger to the application process to inspect the issue.
4. Advised the user to install the required .NET hosting bundle.

## Root Cause
The issue was caused by the user not having the correct version of the .NET runtime installed, specifically the Microsoft.NETCore.App version 8.0.15, which was required by the application.

## Solution
The issue was resolved by the user installing the correct .NET hosting bundle for ASP.NET Core version 8.0.15. After installation, the user was instructed to restart IIS and verify the application functionality, which confirmed that the website was operational.

## Notes
- Ensure that the correct version of the .NET runtime is installed before deploying applications that depend on specific versions.
- For future reference, always check the compatibility of the installed .NET versions with the application requirements to prevent similar issues.