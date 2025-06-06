## Ticket Metadata
- **Ticket ID:** 500Qk00000NboFBIAZ
- **Case Number:** 440734
- **Status:** Closed - Resolved
- **Account/Company:** Chubb INA Holdings Inc.
- **Contact Name:** Karoline Robb
- **Product:** Netwrix Enterprise Auditor
- **Component:** Upgrade
- **Feature:** Upgrade
- **Version:** 11.6

## Problem Description
The customer requested assistance to upgrade their current Netwrix Enterprise Auditor console from version 11.5 to 11.6, with a specific focus on integrating CyberArk.

## Environment Details
- **Old Version:** 11.5.1355.1197
- **New Version:** 11.6.0.141
- **CyberArk Integration:** Required for the upgrade process.

## Troubleshooting Steps
1. Scheduled a pre-flight meeting to discuss the upgrade process and gather necessary configuration files.
2. Conducted the upgrade to NEA version 11.6.0.141 successfully.
3. Attempted to upgrade to AIC version 11.6.0.37 but encountered issues due to the lack of the Windows account password for "StealthID."
4. Attempted to enable the NEA Reporting Module but found that an SSL certificate was not assigned to the NEA Application server.
5. Followed up with the customer to obtain the necessary password and SSL certificate.

## Root Cause
The inability to upgrade to AIC 11.6.0.37 was due to not having the password for the Windows account "StealthID." Additionally, the NEA Reporting Module could not be enabled because there was no SSL certificate assigned to the NEA Application server.

## Solution
1. The customer was able to obtain the password for the "StealthID" account, allowing the upgrade to AIC 11.6.0.37 to proceed successfully.
2. The customer requested an SSL certificate for the NEA Application server, which was a prerequisite for enabling the NEA Reporting Module.
3. After obtaining the certificate, the customer successfully installed it on the server.

## Notes
- Ensure that the necessary credentials and SSL certificates are available before attempting upgrades involving CyberArk integration.
- It is advisable to have a backup of the current configuration before proceeding with any upgrades.
- If similar issues arise, verify the connection profiles and credentials assigned to jobs in the Netwrix environment.