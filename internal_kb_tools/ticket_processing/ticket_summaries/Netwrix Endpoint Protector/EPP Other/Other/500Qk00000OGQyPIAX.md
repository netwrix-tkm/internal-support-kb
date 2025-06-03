## Ticket Metadata
- **Ticket ID:** 500Qk00000OGQyPIAX
- **Case Number:** 442576
- **Status:** Closed - Resolved
- **Account/Company:** White Rock
- **Contact Name:** Evgeny Zinchenko
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Other
- **Version:** 6.2.4.2

## Problem Description
The customer reported that they were unable to deploy the Endpoint Protector (EPP) via Microsoft Intune on three different machines, each with varying configurations. The installation consistently failed, and the customer sought assistance in resolving the issue.

## Environment Details
- Deployment method: Microsoft Intune
- Machines involved: Three different endpoints with varying configurations
- Previous installation: Manual installation of EPP was performed on the machines prior to the Intune deployment attempts.

## Troubleshooting Steps
1. **Initial Assessment**: Customer confirmed multiple attempts to deploy EPP via Intune, with failures occurring on all three machines.
2. **Remote Session Scheduled**: A remote session was arranged to investigate the installation errors further.
3. **Manual Installation Attempt**: During the remote session, the EPP client was installed manually, which succeeded, but the Intune deployment resulted in an error:
   - **Error Message**: "Product: Endpoint Protector -- Error 1904. Module C:Program FilesCoSoSysEndpoint Protectori386EPPMailChecker.dll failed to register. HRESULT -1073741819."
4. **Log Analysis**: The customer was instructed to run the installation command with logging enabled and share the log file for analysis.
5. **Further Troubleshooting**: Additional steps included uninstalling the client, attempting to deploy an older version, and using specific command-line parameters for installation.
6. **Final Resolution Steps**: The customer was provided with a command to uninstall using a zap tool, restart the endpoint, and then install the latest version with specific parameters.

## Root Cause
The issue was identified as being related to the way Intune interpreted the MSI file during installation. The initial command provided to the customer contained additional spaces that caused the installation to fail.

## Solution
The issue was resolved by providing the correct command for deployment via Intune, which included:
```bash
WSIP="Server_IP" WSPORT="443" DEPARTMENT_CODE="defdef" INSTALL_NOTES_EXT="0" INSTALL_OUTLOOK_EXT="0" /q REBOOT=ReallySuppress
```
The customer confirmed that this command worked without issues, allowing the EPP to be successfully installed via Intune.

## Notes
- Ensure that any command provided for installation via Intune is free of unnecessary spaces or formatting errors.
- The zap tool used for uninstallation is an internal tool and should be used with caution, ensuring it is deleted after use and not shared with third parties.
- Future deployments should be tested in a controlled environment to confirm compatibility before wide-scale implementation.