## Ticket Metadata
- **Ticket ID:** 500Qk00000BnnirIAB
- **Case Number:** 411879
- **Status:** Closed - Resolved
- **Account/Company:** Beacon Roofing
- **Contact Name:** Tony Do
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Initial setup
- **Version:** 11.5

## Problem Description
The customer requested guidance for performing an in-place upgrade of their StealthAudit server from Windows Server 2012 to Windows Server 2019. Additionally, they needed assistance in configuring the reports URL for StealthAudit to use HTTPS instead of HTTP.

## Environment Details
- Current Server OS: Windows Server 2012
- Target Server OS: Windows Server 2019
- Product Version: 11.5

## Troubleshooting Steps
1. The support engineer, Scottie Taylor, communicated with the customer regarding the upgrade process.
2. It was advised against performing an in-place upgrade due to potential risks associated with the NEA application.
3. The customer was recommended to set up a new server and perform a fresh installation/migration of the application.

## Root Cause
The recommendation against an in-place upgrade was based on best practices for maintaining application integrity and stability, particularly for the Netwrix Enterprise Auditor application.

## Solution
The issue was resolved by providing the customer with guidance to:
- Spin up a new server for the installation of Windows Server 2019.
- Perform a fresh installation of the StealthAudit application on the new server.
- Migrate the necessary data and configurations from the old server to the new one.

The customer agreed to follow this approach and indicated they would reach out for further assistance with the migration process.

## Notes
- It is crucial to avoid in-place upgrades for the NEA application to prevent potential issues.
- Future customers should be advised to consider a fresh installation on a new server for major OS upgrades.
- Ensure that all configurations, including URL settings for HTTPS, are reviewed and updated during the migration process.