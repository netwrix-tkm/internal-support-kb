## Ticket Metadata
- **Ticket ID:** 500Qk00000JsatDIAR
- **Case Number:** 430698
- **Status:** Closed - Resolved
- **Account/Company:** The Baupost Group
- **Contact Name:** Charlie Davidson
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for SharePoint
- **Feature:** Credentials
- **Version:** 11.6

## Problem Description
The customer reported issues with generating permissions reports for users after migrating their on-prem user home directories to OneDrive. Specifically, they were unable to see all subdirectories, only a limited set including Social, Documents, Form Template, and Style Library.

## Environment Details
- **Netwrix Enterprise Auditor (NEA) Version:** 11.6.0.112
- **Platform:** SharePoint Online

## Troubleshooting Steps
1. Identified overlapping jobs causing host resource issues.
2. Created new App-registrations and Certificate for the connection using the Instant Job Wizard.
3. Corrected configuration errors for the SharePoint Online permissions job.
4. Restarted the console and tested a Zero level Job, which was successful.
5. Adjusted the scheduling of SharePoint Online scans to run sequentially to prevent resource contention.
6. Corrected the profile for the SPAC_SystemScans.

## Root Cause
The issue was primarily due to incorrect configuration settings in the Netwrix Enterprise Auditor, specifically related to the SharePoint Online permissions job. Overlapping jobs were also causing resource contention, leading to incomplete data collection.

## Solution
The resolution involved:
- Correcting the configuration for the SharePoint Online permissions job.
- Ensuring that the jobs were scheduled to run one after another to avoid overlapping and resource issues.
- Successfully testing the connection and scanning process after the configuration changes.

## Notes
- Ensure that job configurations are verified after migrations to prevent similar issues.
- Monitor job scheduling to avoid overlapping, which can lead to resource contention and incomplete data collection.
- Refer to the Netwrix help center for detailed guidance on configuring SharePoint Online permissions: [Netwrix Help Center](https://helpcenter.netwrix.com/bundle/EnterpriseAuditor_11.6/page/Content/EnterpriseAuditor/Admin/Jobs/InstantJobs/SP_RegisterAzureAppAuth.htm).