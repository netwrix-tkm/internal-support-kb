## Ticket Metadata
- **Ticket ID:** 500Qk00000NuBgJIAV
- **Case Number:** 441583
- **Status:** Closed - Resolved
- **Account/Company:** Exeter Finance LLC
- **Contact Name:** Bao Luu
- **Product:** Netwrix Enterprise Auditor
- **Component:** Netwrix Activity Monitor
- **Feature:** Upgrade
- **Version:** 12.0.0.1061 (upgraded from 11.6.0.117)

## Problem Description
The customer requested assistance with upgrading the Netwrix Enterprise Auditor (NEA) and the Netwrix Activity Monitor (NAM) to their latest versions.

## Environment Details
- **Previous NEA Version:** 11.6.0.117
- **New NEA Version:** 12.0.0.1061
- **Previous AIC Version:** 11.6.0.25
- **New AIC Version:** 12.0.0.48

## Troubleshooting Steps
1. Upgraded NEA from version 11.6.0.117 to 12.0.0.1061.
2. Upgraded AIC from version 11.6.0.25 to 12.0.0.48.
3. Recovered AIC access by checking SSL certificate binding using the command:
   ```bash
   netsh http show sslcert
   ```
   - Found that the SSL certificate for AIC was not bound to the port.
4. Recovered NEA Published Reports Access by ensuring that the "Netwrix Enterprise Auditor Web Server" service was running with the correct service account credentials.

## Root Cause
The issues encountered during the upgrade were primarily due to:
- The SSL certificate for the AIC not being properly bound to the port, which prevented access.
- The NEA Web Server service not running under the correct service account credentials, which restricted access to published reports.

## Solution
The issue was resolved by:
1. Successfully upgrading both NEA and AIC to their respective latest versions.
2. Binding the SSL certificate to the appropriate port for AIC access.
3. Configuring the "Netwrix Enterprise Auditor Web Server" to run with the correct service account credentials, restoring access to published reports.

## Notes
- Ensure that SSL certificates are correctly bound to their respective ports during upgrades to avoid access issues.
- Always verify that services are running under the correct credentials after an upgrade to prevent access restrictions.
- Document any changes made during the upgrade process for future reference.