## Ticket Metadata
- **Ticket ID:** 500Qk00000EQxyvIAD
- **Case Number:** 418124
- **Status:** Closed - Resolved
- **Account/Company:** Kerry Group Services International Limited
- **Contact Name:** Cameron Bowlds
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for SharePoint
- **Feature:** Configuration
- **Version:** Not specified

## Problem Description
The customer reported issues with a StealthAUDIT SharePoint scan, receiving errors related to SharePoint App Authentication context and unspecified errors during the scanning process. Additionally, they requested assistance with upgrading to a newer version of the software.

## Environment Details
- The customer was using an older version of the Netwrix Enterprise Auditor.
- The issue involved SharePoint scanning and Azure App Authentication.

## Troubleshooting Steps
1. Verified the Azure Client ID and its API permissions.
2. Attempted to run the SP_RegisterAzureAppAuth Job, which initially failed due to authentication issues.
3. Installed the Azure AD module for PowerShell and the Microsoft.Graph module to resolve PowerShell warnings.
4. Suggested performing Azure App Auth registration manually on the Azure portal.
5. Monitored the SPAA scan job and adjusted the scan depth to 0 level to facilitate progress.

## Root Cause
The root cause of the issue was identified as the Azure Client ID not being able to properly authenticate, which led to the failure of the SharePoint App Authentication context.

## Solution
The issue was resolved by:
- Retrofitting an existing Azure Client ID and verifying the account's API permissions.
- Applying the generated `spaa.cert` to the Azure Client ID.
- Configuring the path to the certificate file and adding it as a password to the connection profile of the SPAA job.
- Dropping the scan depth to 0 level and monitoring the scan until it progressed past the initializing step.

## Notes
- Ensure that the Azure Client ID has the correct API permissions before running the SPAA scan.
- Future upgrades should be addressed in separate tickets to avoid confusion with ongoing issues.
- Documentation for SharePoint Online Access & Sensitive Data Auditing Configuration should be referenced for proper setup and permissions.