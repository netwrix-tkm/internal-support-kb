## Ticket Metadata
- **Ticket ID:** 500Qk00000OqVupIAF
- **Case Number:** 444209
- **Status:** Closed - Resolved
- **Account/Company:** Berwind
- **Contact Name:** Chan Pin
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for SharePoint
- **Feature:** Data Collection
- **Version:** 11.6

## Problem Description
The customer reported that multiple SharePoint Online sites listed in SharePoint Online were not appearing in the Resource Audit of the Netwrix Enterprise Auditor (AIC). The customer was using version 11.6 of the application.

## Environment Details
- **Application Version:** 11.6
- **Build Number:** 139
- **Affected Component:** SharePoint Online sites

## Troubleshooting Steps
1. Reviewed the SharePoint resource in AIC and confirmed that 15 sites were missing.
2. Identified that the SPSEEK scan was scoped to a particular site, limiting the results.
3. Removed the scoping limitation for the SPSEEK scan.
4. Dropped all existing SharePoint data from the SQL database and renamed the local copy to start fresh.
5. Ran a new SPSEEK scan with an initial depth of 2 levels, later increased to 4 levels.
6. Advised the customer to extend the scan depth further by unchecking the "Limit scanned depth to:" option for a complete scan.
7. Reduced the logging level to "Warning" to prevent log bloat and memory resource errors during subsequent scans.
8. Created a separate ticket for inconsistencies in user account reporting across Active Directory and Entra ID.

## Root Cause
The issue was caused by the SPSEEK scan being scoped to a single SharePoint site, which prevented other sites from being included in the audit. Additionally, the SPAA scan had been disabled for a long time due to an expired certificate, leading to outdated or incomplete data in the database.

## Solution
1. Created and uploaded a new self-signed certificate to the Azure App registration.
2. Updated the connection profile in Netwrix Enterprise Auditor to use the new certificate.
3. Removed the inclusion filter for the SPSEEK scan to ensure all sites were scanned.
4. Dropped all existing SPSEEK and SPAA data from the SQL database and started with a clean slate.
5. Successfully ran a fresh SPSEEK scan, which updated the missing sites in the AIC.
6. Confirmed with the customer that the sites were now visible in the AIC, resolving the primary issue.

## Notes
- The customer still experienced issues with a few user Active Directory accounts not appearing consistently across AD and Entra ID reports, necessitating a new ticket for further investigation.
- A new issue was identified related to memory resources during the SHAREPOINTACCESS scan, which may require additional attention in future cases.