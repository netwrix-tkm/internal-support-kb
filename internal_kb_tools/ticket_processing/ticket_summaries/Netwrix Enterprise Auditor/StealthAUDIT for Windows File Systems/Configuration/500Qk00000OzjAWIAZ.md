## Ticket Metadata
- **Ticket ID:** 500Qk00000OzjAWIAZ
- **Case Number:** 444706
- **Status:** Closed - Resolved
- **Account/Company:** Extron Electronics
- **Contact Name:** Stephen Byrd
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Windows File Systems
- **Feature:** Configuration
- **Version:** 11.6

## Problem Description
The customer reported that FSAC (File System Activity Collector) was not detecting the `SBTFileMon.ini` file or its configuration for activity on one server. Initially, it was not detecting it on two servers, but one server was later functioning correctly.

## Environment Details
- Two servers were offline due to a network outage and had been removed from the Netwrix Enterprise Auditor (NEA).
- The servers were brought back online with no major changes during the downtime.
- The version of the product in use was 11.6.

## Troubleshooting Steps
1. Verified that NAM (Netwrix Activity Monitor) was configured correctly and that events were searchable.
2. Updated both hosts in NEA, which initially showed as offline with no server fingerprint information. This information populated correctly after the host update.
3. Remotely accessed the `SBTFileMon.ini` file location from the NEA server and verified that the content of the INI file was correct for the setup, ensuring the server name matched the NEA server name.
4. Created activity on both servers; one server began functioning correctly after this step.

## Root Cause
The issue was caused by the `STEALTHAUDIT` setting in the `SBTFileMon.ini` file being set to `ON`, which prevented FSAC from detecting the file correctly. 

## Solution
To resolve the issue, the following steps were taken:
1. Opened the `SBTFileMon.ini` file located at `C:\ProgramData\Netwrix\Activity Monitor\Agent\SBTFileMon.ini` on the server `ISR-MMR-FS1`.
2. Under the `[FILE_MONITOR1]` section, changed the line `STEALTHAUDIT=ON` to `STEALTHAUDIT=OFF`.
3. Saved the changes to the INI file.
4. Initiated a new FSAC System Scan, which confirmed that the server could connect and function correctly.

## Notes
- Ensure that the `STEALTHAUDIT` setting is correctly configured in the `SBTFileMon.ini` file for proper detection by FSAC.
- If similar issues arise, verify the configuration of NAM and the INI file settings before escalating the case.