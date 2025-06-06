## Ticket Metadata
- **Ticket ID:** 500Qk00000EPREhIAP
- **Case Number:** 418056
- **Status:** Closed - Resolved
- **Account/Company:** MISO Energy
- **Contact Name:** Patrick Sager
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Windows
- **Feature:** Configuration
- **Version:** 11.6

## Problem Description
The internal Cyber team reported issues with the guest account (MISOGUEST) on machines, specifically noting that the StealthAudit application was attempting to authenticate using this guest account across various hosts, which seemed to correlate with account lockout events.

## Environment Details
- **Operating System:** Windows Server 2019
- **Netwrix Product Version:** 11.6
- **Application in Question:** StealthAudit

## Troubleshooting Steps
1. **Log Search:** Executed commands to search for occurrences of "MISOGUEST" in various log files:
   - `gci "D:Program Files (x86)STEALTHbitsStealthAUDITSADatabaseLogs*.log" -Recurse | Select-String MISOGUEST`
   - `gci "D:Program FilesSTEALTHbitsAccess Information Center*.log" -Recurse | Select-String MISOGUEST`
   - `gci "D:Program Files (x86)STEALTHbitsStealthAUDITJobs" -Include ConnectStatus.csv -Recurse | Select-String MISOGUEST`
   - All returned no results.
   
2. **Audit Policy Verification:** Confirmed that the necessary OS auditing was enabled on the Netwrix Enterprise Auditor server and one of the Windows 2019 servers:
   - `auditpol /get /category:Logon/Logoff`
   - `auditpol /get /category:'Account Logon'`
   
3. **Event Log Filtering:** Filtered the Windows Security Event log for the last 24 hours for the MISOGUEST account using specific Event IDs (4625, 4648, etc.).
   - No logon attempts were noted from the NEA Server, but entries were found on the Windows 2019 host indicating local user activity via BESClient.exe.

4. **Event ID References:** Reviewed relevant Event IDs for additional context on the logon events.

## Root Cause
The investigation concluded that the authentication attempts using the MISOGUEST account were not originating from the Netwrix applications installed on the calling server (IPWDAG01). Instead, the activity was linked to local user actions on the Windows 2019 host, specifically through the BESClient.exe process.

## Solution
The issue was resolved by confirming that the StealthAudit application was not responsible for the guest account authentication attempts. The necessary auditing settings were verified, and it was established that the account lockout events were due to local user activity rather than application misconfiguration.

## Notes
- Ensure that OS auditing settings are correctly configured on all relevant servers to facilitate future troubleshooting.
- Monitor local user activities on machines where guest accounts are enabled to prevent similar issues.
- Consider reviewing application logs periodically to ensure no unexpected behavior occurs after upgrades or changes in configuration.