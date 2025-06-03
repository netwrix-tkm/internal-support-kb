## Ticket Metadata
- **Ticket ID:** 500Qk00000BwQdJIAV
- **Case Number:** 412118
- **Status:** Closed - Resolved
- **Account/Company:** FAIR Health, Inc.
- **Contact Name:** Chris Meagher
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Install/Uninstall
- **Version:** 5.9.1.7, 5.9.2.8, 6.0.1.6 (Windows)

## Problem Description
The customer reported an issue where they were unable to uninstall the Netwrix Endpoint Protector client. The error message indicated that "The feature you are trying to use is on a network resource that is unavailable," specifically referencing a temporary file located at `C:\Windows\Temp\SIE1116.tmp`.

## Environment Details
- Multiple versions of the client were installed on different machines:
  - 5.9.1.7 (Windows)
  - 5.9.2.8 (Windows)
  - 6.0.1.6 (Windows)

## Troubleshooting Steps
1. The customer attempted to uninstall the client using:
   - The web console.
   - Control Panel > Programs & Features.
2. The customer provided screenshots of the error encountered during the uninstallation attempts.
3. The support engineer requested additional details regarding the uninstall method used (MDM, console, or manual).
4. The support engineer inquired about the number of computers affected by the issue.
5. The support engineer provided a tool (EppZapTool) for manual uninstallation after receiving the customer's agreement to the disclaimer regarding its use.

## Root Cause
The root cause of the issue was identified as the unavailability of the temporary installation file required for the uninstallation process. This could occur due to file deletion or permission issues on the system.

## Solution
The issue was resolved by using the EppZapTool provided by the support engineer. The customer was instructed to:
1. Download the tool from the provided link.
2. Run the tool twice with administrative rights.
3. Reboot the computer after running the tool.

The customer confirmed that the tool worked successfully on the first machine, and they planned to apply it to the remaining affected machines.

## Notes
- Ensure that the EppZapTool is only used by authorized administrators to prevent unauthorized uninstallation of the client.
- Always verify that the necessary installation files are available before attempting to uninstall software.
- Document any similar issues with specific error messages and resolutions for future reference.