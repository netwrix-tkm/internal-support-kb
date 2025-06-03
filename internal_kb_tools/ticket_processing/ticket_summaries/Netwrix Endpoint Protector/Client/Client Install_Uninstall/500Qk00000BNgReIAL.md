## Ticket Metadata
- **Ticket ID:** 500Qk00000BNgReIAL
- **Case Number:** 410789
- **Status:** Closed - Resolved
- **Account/Company:** Essex Lake Group, LLC
- **Contact Name:** Shivam Tyagi
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Install/Uninstall
- **Version:** Not specified

## Problem Description
The customer requested assistance in modifying the uninstallation command for the Netwrix Endpoint Protector (EPP) on Windows, specifically to use an installation path instead of the MSI file. Additionally, they reported an extension added in Outlook that needed removal.

## Environment Details
- The customer was using Windows machines.
- The customer was utilizing MDM (Workspace ONE) for device management.
- The MSI file for EPP was not available on the user's machine.

## Troubleshooting Steps
1. The customer initially attempted to use the command:
   ```bash
   msiexec.exe /x "C:\Users\Shivam-PC\Downloads\EPPClientSetup.6.0.1.6.msi" ADMIN_PASSWORD_0=" " REBOOT=ReallySuppress REMOVE_PROP=1 /qn
   ```
   This command did not work.
   
2. Support suggested running the command with administrator rights and provided the same command again for verification.
   
3. The customer clarified that they needed a command to uninstall EPP without the MSI file, as it was not available on the user's machine.

4. Support provided three potential methods for uninstallation:
   - Remote uninstallation from the server side.
   - Using the previously shared command involving the MSI.
   - A zap tool that could be run locally, which required a disclaimer.

5. The customer indicated that their account with EPP was terminated, and they could not access the server for remote uninstallation.

## Root Cause
The issue stemmed from the customer's inability to access the MSI file required for the standard uninstallation command. Additionally, the termination of their account with EPP limited their options for remote management and uninstallation.

## Solution
The resolution involved clarifying that without access to the MSI file, the customer could not use the standard command. The support team suggested:
- Utilizing remote uninstallation if access was available.
- If not, they could consider using the zap tool under extraordinary circumstances, which would require the customer to acknowledge a disclaimer.

## Notes
- It is important for users to maintain access to the MSI files for uninstallation purposes.
- In cases where the MSI is unavailable, alternative methods such as remote uninstallation or specialized tools may be necessary, but these may require additional permissions or disclaimers.
- Future users should ensure they have the necessary administrative rights when executing uninstallation commands.