## Ticket Metadata
- **Ticket ID:** 500Qk00000NXaAlIAL
- **Case Number:** 440543
- **Status:** Closed - Resolved
- **Account/Company:** Jayman Built
- **Contact Name:** Sahil Umatia
- **Product:** Netwrix Enterprise Auditor
- **Component:** SharePoint Online Auditor
- **Feature:** Credentials
- **Version:** 11.6

## Problem Description
The customer reported that the SharePoint Online Auditor application's secret key had expired. After generating a new client secret in Entra AD and updating it in the Netwrix Auditor console, the SharePoint scan failed to run successfully, indicating a connection failure.

## Environment Details
- The customer is using Netwrix Enterprise Auditor version 11.6.
- The issue arose after an update was installed on January 27, 2025, related to a previous ticket for OneDrive reports.

## Troubleshooting Steps
1. Renewed the app secret key and updated it in the Netwrix console.
2. Updated and replaced the Entra app self-signed certificate.
3. Added Microsoft Graph permissions for the Entra app: `Sites.Read.All` and `Sites.FullControl.All`.
4. Tested Entra app credentials with Microsoft Graph - confirmed no issues.
5. Rebooted the Netwrix and SQL server.
6. Checked the service principal login for the Entra app - successful.

## Root Cause
The Netwrix Enterprise Auditor (NEA) does not utilize the app secret for connecting to Azure; instead, it requires a certificate for authentication. The failure to connect was due to the incorrect assumption that the app secret could be used in place of a certificate.

## Solution
The issue was resolved by configuring the connection to use certificates instead of the app secret. The customer was provided with documentation to recreate the connection string using certificates, following the guide linked below:
- [Netwrix Documentation on Configuring SharePoint Connection](https://helpcenter.netwrix.com/bundle/EnterpriseAuditor_11.6/page/Content/EnterpriseAuditor/Admin/DataCollector/SPAA/ConfigureJob.htm#SharePoi)

## Notes
- For future reference, ensure that the NEA is configured to use certificates for authentication with Azure services, rather than relying on app secrets.
- The customer confirmed that scans are now working correctly and plans to delete the app secret, retaining only the certificate for authentication.