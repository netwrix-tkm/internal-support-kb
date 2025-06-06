## Ticket Metadata
- **Ticket ID:** 500Qk00000NeacHIAR
- **Case Number:** 440881
- **Status:** Closed - Resolved
- **Account/Company:** Micron Technology, Inc
- **Contact Name:** Kurtis Andersen
- **Product:** Netwrix Enterprise Auditor
- **Component:** NEA Web Report Console
- **Feature:** Web Reports
- **Version:** 11.6

## Problem Description
The customer reported a 500 error when attempting to open Web Reports, accompanied by the error message: "Invalid object name 'dbo.SA_WebServer_Events'." This issue occurred during SQL Server authentication from NEA to the SQL database.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Version:** 11.6
- **Build Number:** 138
- **Installation Type:** Fresh install
- **Active Directory Integration (ADI) Tables:** Present

## Troubleshooting Steps
1. Verified SQL Server authentication settings from NEA to SQL DB.
2. Attempted to run the Web Service as a local system and then as an Active Directory (AD) user with rights to SQL Server/DB.
3. Restarted the Web Service; however, logs indicated no successful restart.
4. Rebooted the server, which did not resolve the issue.
5. Reinstalled the Netwrix Enterprise Auditor (NEA).

## Root Cause
The root cause of the issue was not definitively identified. However, it was noted that the service appeared to restart without any logs confirming this action, and the reboot did not rectify the problem. It was suggested that there may have been a misconfiguration related to the storage profile or missing database tables.

## Solution
The issue was resolved by reinstalling the Netwrix Enterprise Auditor (NEA). After the reinstallation, the Web console operated without any further issues.

## Notes
- Ensure that the storage profile is configured correctly in the NEA to prevent similar issues in the future.
- If encountering similar errors, check the service logs for any discrepancies during service restarts.
- Always verify that the necessary database tables are present and correctly configured after installation or updates.