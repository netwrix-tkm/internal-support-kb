## Ticket Metadata
- **Ticket ID:** 500Qk00000LXbeEIAT
- **Case Number:** 434819
- **Status:** Closed - Resolved
- **Account/Company:** Tisseo Voyageurs
- **Contact Name:** Duy-Huan Bui
- **Product:** PingCastle
- **Component:** PC Professional
- **Feature:** PingCastle General
- **Version:** 3.3

## Problem Description
The customer was unable to install **PingCastle Pro 3.3.05 (.msi)** on **Windows Server 2019 (French)** with **MS SQL 2019 Express (French) (LocalDB)** and **.NET 8.0.12**. The installation failed at the final step while creating the local database, resulting in a rollback.

## Environment Details
- **Operating System:** Windows Server 2019 (French)
- **Database:** MS SQL 2019 Express (French) (LocalDB)
- **.NET Version:** 8.0.12

## Troubleshooting Steps
1. Reviewed installation logs which indicated an error during the execution of the `GrantApplicationPoolToSql.ps1` script.
2. Identified **Error Code 1603** during the execution of `GrantApplicationPoolToSql`.
3. Investigated the possibility of the **GrantApplicationPoolToSql.ps1** script being missing or inaccessible.
4. Conducted a remote session with the client to gather more information and discuss potential custom installation needs.
5. Engaged with DevOps for further investigation into the installer updates and the specific script execution issue.

## Root Cause
The installation failure was caused by the installer being unable to locate the **GrantApplicationPoolToSql.ps1** script, which is necessary for granting the application pool access to SQL. This issue was linked to internal bugs in the installer.

## Solution
The issue was resolved by releasing a new version of the software (3.3.0.7) that fixed the internal bugs related to the installation process. The updated installer successfully located and executed the **GrantApplicationPoolToSql.ps1** script, allowing the installation to complete without errors.

## Notes
- Ensure that the installation scripts are included and accessible during the installation process to avoid similar issues in the future.
- For custom installations, consider discussing specific requirements with the client beforehand to streamline the process.
- Monitor for any further updates or patches that may address related issues in future versions.