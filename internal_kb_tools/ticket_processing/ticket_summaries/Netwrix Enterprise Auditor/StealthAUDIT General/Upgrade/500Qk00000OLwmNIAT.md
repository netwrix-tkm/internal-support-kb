## Ticket Metadata
- **Ticket ID:** 500Qk00000OLwmNIAT
- **Case Number:** 442867
- **Status:** Closed - Resolved
- **Account/Company:** Beiersdorf Shared Services GmbH
- **Contact Name:** San Johannsen
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Upgrade
- **Version:** 12.0

## Problem Description
The customer requested assistance to update StealthAudit from version 11.0 to the current version, which was identified as 12.0.

## Environment Details
- Starting version: 11.0
- Target version: 12.0
- The customer also had the Access Information Center (AIC) installed.

## Troubleshooting Steps
1. Advised the customer to upgrade to version 11.6 first to confirm functionality before proceeding to version 12.0.
2. Recommended taking snapshots of the StealthAUDIT server and SQL Database Server for backup purposes.
3. Provided upgrade instructions and links to the relevant documentation for both versions.
4. Confirmed the successful upgrade to version 11.6.
5. Discussed the next steps for upgrading to version 12.0.
6. Addressed issues with the AIC not being accessible from clients and SSL certificate warnings.

## Root Cause
The initial issue stemmed from the need to upgrade from an outdated version of StealthAudit (11.0) to a more current version (12.0). During the upgrade process, configuration settings for the AIC were not correctly aligned with the new version, leading to accessibility issues.

## Solution
- The upgrade to version 12.0 was successfully completed after confirming the functionality of version 11.6.
- The AIC's configuration was adjusted to use the correct port (443 instead of the default 481) in its config file, which resolved the accessibility issue.
- Restarting the server after the configuration change allowed the AIC to function properly.

## Notes
- Ensure that any SSL certificates are correctly configured and trusted in the system to avoid warnings.
- It is advisable to check port bindings and configurations in IIS for the AIC after upgrades.
- Future upgrades should follow the documented procedures closely to prevent similar issues.