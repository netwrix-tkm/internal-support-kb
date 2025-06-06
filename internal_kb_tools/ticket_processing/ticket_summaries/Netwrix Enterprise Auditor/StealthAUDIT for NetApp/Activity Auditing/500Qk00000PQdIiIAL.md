## Ticket Metadata
- **Ticket ID:** 500Qk00000PQdIiIAL
- **Case Number:** 445885
- **Status:** Closed - Resolved
- **Account/Company:** EverBank
- **Contact Name:** Bradley Dickinson
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for NetApp
- **Feature:** Activity Auditing
- **Version:** 11.6 (build 11.6.0.132)

## Problem Description
The FSAC System scan in Netwrix Enterprise Auditor failed with the error message: "Requested registry access is not allowed." This occurred while attempting to retrieve the SBTFileMon.INI path from the registry.

## Environment Details
- **Software Version:** Netwrix Enterprise Auditor version 11.6 (build 11.6.0.132)
- **Registry Key Involved:** `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\SBTLogging\Parameters\ConfigPath`

## Troubleshooting Steps
1. Open the Netwrix Enterprise Auditor version 11.6.
2. Initiate an FSAC System scan.
3. Observe the error message indicating "Requested registry access is not allowed" while attempting to retrieve the SBTFileMon.INI path from the specified registry key.
4. Investigate permissions for the registry key involved.

## Root Cause
The issue was determined to be related to insufficient permissions to access the specified registry key, which prevented the scan from retrieving the necessary configuration file path. The exact root cause (misconfiguration, permissions issue, or software defect) was not definitively identified.

## Solution
To resolve the issue, the following steps were taken:
- Navigate to the file located at `C:\ProgramData\Netwrix\Activity Monitor\Agent\SBTFileMon.ini` on the server ISR-MMR-FS1.
- Under the `[FILE_MONITOR1]` section, locate the line `STEALTHAUDIT=ON`.
- Change this line to `STEALTHAUDIT=OFF` and save the file.
- Initiate a new FSAC System scan, which completed successfully.

## Notes
- Ensure that the necessary permissions are granted for registry access to avoid similar issues in the future.
- Monitor the configuration settings in the SBTFileMon.ini file, as changes can impact the functionality of the FSAC System scan.