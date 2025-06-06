## Ticket Metadata
- **Ticket ID:** 500Qk00000NJCxwIAH
- **Case Number:** 439919
- **Status:** Closed - Resolved
- **Account/Company:** Hugh Chatham Memorial Hospital
- **Contact Name:** Justin Snow
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Upgrade
- **Version:** 10.0

## Problem Description
The customer needed to upgrade StealthAUDIT and other Stealthbits applications to the latest version, as they had recently taken over the system. They were informed that upgrading StealthAUDIT would cover all application upgrades.

## Environment Details
- **Current Versions Prior to Upgrade:**
  - StealthAUDIT (SA): 10.0.0.168
  - Access Information Center (AIC): 10.0.0.73
  - Sensitive Data Add-On (SDD): 10.0.0.87

## Troubleshooting Steps
1. Customer provided the output of a PowerShell script detailing the installed versions of the applications.
2. Scheduled meetings for upgrade preparation and execution.
3. Reset the Default ADMIN profile to access the AIC for configuration checks.
4. Executed SQL queries to verify and enable necessary configurations.
5. Uninstalled older versions of the applications.
6. Installed the new versions:
   - StealthAUDIT (SA): 11.5.0.279
   - Access Information Center (AIC): 11.5.0.138
   - Sensitive Data Add-On (SDD): 11.5.0.65
7. Verified functionality of URLs and rebuilt the Reports Folder.
8. Enabled LongPathsEnabled in the registry and set the Host PageFile to use only the E: Drive.
9. Recommended increasing vCPUs from 4 to 8 for better performance.

## Root Cause
The issue stemmed from the outdated versions of the StealthAUDIT applications, which required an upgrade to ensure compatibility and access to the latest features and security updates.

## Solution
The upgrade was successfully completed by:
- Resetting the Default ADMIN profile to access the AIC.
- Executing necessary SQL queries to enable the built-in Admin.
- Uninstalling the outdated applications and installing the latest versions.
- Ensuring all configurations were correct and functional post-upgrade.

## Notes
- It is recommended to enable LongPathsEnabled on all Windows File Servers.
- A reboot is required for the LongPathsEnabled setting to take full effect.
- Future upgrades should consider increasing the vCPUs to enhance performance, especially for environments with heavy data processing needs.