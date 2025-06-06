## Ticket Metadata
- **Ticket ID:** 500Qk00000MfywQIAR
- **Case Number:** 438076
- **Status:** Closed - Resolved
- **Account/Company:** Howard County, MD
- **Contact Name:** Frank Salah
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Upgrade
- **Version:** 11.6

## Problem Description
The customer requested assistance with upgrading the following products: StealthAudit, StealthDefend, and StealthIntercept. Additionally, they wanted to review the SSL certificate used for StealthDefend and potentially create a new certificate with their internal certificate authority.

## Environment Details
- Current version of StealthAudit: 11.5
- Products involved in the upgrade: 
  - StealthAUDIT Access Information Center
  - StealthAUDIT Sensitive Data Discovery
  - StealthAUDIT

## Troubleshooting Steps
1. Scheduled a meeting to discuss the upgrade process.
2. Performed a pre-flight process which included:
   - Taking screenshots of global settings and custom job settings.
   - Full backups of the Jobs folder, GlobalOptions, and SPProfiles.xml.
   - Backups of the SSL certificate bindings for all web applications.
3. Confirmed that no PostgreSQL was installed on the application server.
4. Discussed the need for a snapshot of the application server and a backup of the StealthAudit database before the upgrade.
5. Ensured that the latest version of the installer was downloaded and unblocked.

## Root Cause
The issue stemmed from the need for a proactive upgrade to the latest version (11.6) of the Netwrix Enterprise Auditor. Additionally, it was discovered that the SSL certificate used for StealthDefend was either not installed on the application server or had possibly expired.

## Solution
The following steps were taken to resolve the issue:
1. Upgraded the StealthAudit console and all associated applications from version 11.5 to NEA 11.6.0.137, following the "Enterprise Auditor Core Upgrade Instructions."
2. Updated the SSL certificate bindings for both the Access Information Center (AIC) and Published Reports. The expired or missing certificate was removed using the command:
   ```bash
   netsh http del sslcert ipport=0.0.0.0:8082
   ```
3. A new SSL certificate was added using the command:
   ```bash
   netsh http add sslcert ipport=0.0.0.0:8082 appid= certhash=
   ```
   The port numbers were adjusted to target both the AIC (port 481) and the Published Reports (port 8082), ensuring the updated certificate hash was included.

## Notes
- Ensure that all scheduled jobs are stopped or will not run during the upgrade process to avoid conflicts.
- Always verify that the installer for the upgrade is unblocked before proceeding with the installation.
- Regularly check the status of SSL certificates to prevent issues related to expired certificates.