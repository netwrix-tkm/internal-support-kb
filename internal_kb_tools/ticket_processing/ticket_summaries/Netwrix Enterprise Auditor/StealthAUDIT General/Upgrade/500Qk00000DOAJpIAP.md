## Ticket Metadata
- **Ticket ID:** 500Qk00000DOAJpIAP
- **Case Number:** 415651
- **Status:** Closed - Resolved
- **Account/Company:** The Carlstar Group LLC (formerly CTP Carlisle Transportation Products)
- **Contact Name:** James Lilley
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Upgrade
- **Version:** 11.5

## Problem Description
The customer reported that after performing an in-place upgrade from Windows Server 2012 R2 to Windows Server 2016, the access tab on the website was not functioning, resulting in a generic 503 error message.

## Environment Details
- **Upgrade Path:** Windows Server 2012 R2 to Windows Server 2016
- **Product Version:** 11.5

## Troubleshooting Steps
1. Reviewed the configuration files for the Access Information Center (AIC) and reports.
2. Identified potential corruption in the configuration file during a team meeting.
3. Uninstalled the existing version of the Access Information Center.
4. Installed the latest version of the Access Information Center.
5. Verified functionality by attempting to load the AIC through the access tab from the Report page.

## Root Cause
The issue was caused by a corrupted configuration file for the Access Information Center, which was likely a result of the upgrade process.

## Solution
The resolution involved uninstalling the corrupted version of the Access Information Center and installing the latest version. After the reinstallation, the customer was able to successfully access the AIC through the access tab on the Report page.

## Notes
- Ensure to back up configuration files before performing upgrades to prevent similar issues.
- Regularly check for updates to the Access Information Center to avoid compatibility issues post-upgrade.