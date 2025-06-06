## Ticket Metadata
- **Ticket ID:** 500Qk00000HAScQIAX
- **Case Number:** 424315
- **Status:** Closed - Resolved
- **Account/Company:** West Yavapai Guidance Clinic, DBA Polara Health
- **Contact Name:** Josh Taylor
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Upgrade
- **Version:** 11.6.0.113

## Problem Description
The customer requested assistance with upgrading from StealthAUDIT (SA) version 11.5.0.232 and SA Access Information Center (AIC) version 11.5.0.108 to Netwrix Enterprise Auditor (NEA) version 11.6.x. During the upgrade process, issues arose with the reporting folder not updating correctly, leading to failed report generation.

## Environment Details
- Previous Versions:
  - StealthAUDIT (SA): 11.5.0.232
  - SA Access Information Center (AIC): 11.5.0.108
- Upgraded Versions:
  - Netwrix Enterprise Auditor (NEA): 11.6.0.113
  - Netwrix Access Information Center (AIC): 11.6.0.25
- IIS was uninstalled from the server during the upgrade.

## Troubleshooting Steps
1. Rebuilt the Reports folder in the `%sainstalldir%` path.
2. Re-published the reports for the main jobs by re-running the related scheduled tasks.
3. Addressed the error regarding the "Tier 1 database schema is not up to date" by adding the "0-Create Schema" job back into the job group and running it twice to confirm all tables were correct.
4. Resolved the issue with the DLMembership11 job by correcting the Active Directory Inventory job to include the extended attribute "physicalDeliveryOfficeName."

## Root Cause
The initial problem was caused by the reporting folder not being updated correctly during the installation of version 11.5.0.232. Additionally, the "0-Create Schema" job was missing from the collection group, which led to schema-related errors.

## Solution
The issue was resolved by:
- Rebuilding the Reports folder and re-publishing the reports.
- Adding the missing "0-Create Schema" job back into the job group and executing it.
- Correcting the Active Directory Inventory job to include the necessary extended attribute, which allowed the DLMembership11 job to complete successfully.

## Notes
- Ensure that all necessary jobs are included in the collection groups during upgrades to prevent schema-related errors.
- Always verify that the reporting folder is correctly updated after an upgrade to avoid issues with report generation.
- After closing a ticket, customers have 30 days to reopen it if related issues arise.