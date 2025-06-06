```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000BppDRIAZ
- **Case Number:** 411948
- **Status:** Closed - Resolved
- **Account/Company:** Honeywell International
- **Contact Name:** Scott Stefani
- **Product:** Netwrix Enterprise Auditor
- **Component:** Action Module
- **Feature:** File System
- **Version:** 11.5

## Problem Description
The customer reported that after upgrading the SATagParser to resolve an issue with XML Excel file tagging, the SATagParser.CLI.EXE began generating log files within its executable folder. The client requested a way to either specify a different location for the logs or to disable log creation entirely.

## Environment Details
- **SATagParser.cli.dll Version:** 1.0.3.0
- **SATagParser.dll Version:** 11.5.20.1306
- **XMLTagParser.exe Version:** 11.5.1.1306
- **Product Version:** 11.5
- **Build Number:** 11.5.1379.1101

## Troubleshooting Steps
1. Confirmed the issue with log files being created in the executable folder.
2. Reviewed the versions of the SATagParser components to ensure compatibility.
3. Engaged the R&D team to investigate the issue further.
4. Developed a hotfix to address the log file creation issue.
5. Tested the hotfix in a lab environment to confirm it resolved the issue without generating logs.

## Root Cause
The issue was identified as a product defect in the SATagParser.CLI.EXE, which was incorrectly configured to output log files in the executable directory after the upgrade.

## Solution
A hotfix (SA_11.5_098) was released to redirect the log output to the bin folder instead of the executable folder. The following steps were provided to the customer for applying the hotfix:
1. Unblock the hotfix zip file in the Windows property dialog if applicable.
2. Close all instances of StealthAUDIT (check Task Manager for all users).
3. Stop the 'StealthAUDIT File System Action Module Applet' service if running.
4. Update all files in the `%SAInstallDir%` with the new files from the hotfix.

The hotfix was confirmed to work as expected, eliminating the log output issue.

## Notes
- Ensure that the hotfix is applied in a controlled manner, following the provided instructions carefully.
- Monitor for any new log files after applying the hotfix to confirm that the issue is fully resolved.
- Future upgrades should be tested in a lab environment to catch similar issues before deployment.
```