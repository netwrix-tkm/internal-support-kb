## Ticket Metadata
- **Ticket ID:** 500Qk00000EzBUlIAN
- **Case Number:** 419252
- **Status:** Closed - Resolved
- **Account/Company:** Virginia Lottery
- **Contact Name:** James Monteria
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Upgrade
- **Version:** 11.6

## Problem Description
The customer requested assistance with upgrading the Netwrix Enterprise Auditor APP Server (formerly StealthAUDIT) from version 11.6.0.49 to 11.6.0.92. The upgrade aimed to resolve known bugs and enhance the application's performance.

## Environment Details
- **Current Versions Prior to Upgrade:**
  - Netwrix Enterprise Auditor (NEA): 11.6.0.49
  - Netwrix Access Information Center (AIC): 11.6.0.7
  - Stealth Activity Monitor (SAM): 6.0.928
- **Target Versions After Upgrade:**
  - Netwrix Enterprise Auditor (NEA): 11.6.0.92
  - Netwrix Access Information Center (AIC): 11.6.0.23
  - NEA Sensitive Data (SDD): 11.6.0.13
  - Netwrix Activity Monitor (NAM): 7.1.165

## Troubleshooting Steps
1. Reviewed the upgrade documentation for each component:
   - NEA: [Enterprise Auditor Core Upgrade Instructions](https://helpcenter.netwrix.com/bundle/EnterpriseAuditor_11.6/page/Content/EnterpriseAuditor/Install/Application/Upgrade/Wizard.htm)
   - AIC: [Upgrade Procedure](https://helpcenter.netwrix.com/bundle/AIC_11.6/page/Content/Access/InformationCenter/Installation/Upgrade.htm)
   - NAM: [Upgrade Procedure](https://helpcenter.netwrix.com/bundle/ActivityMonitor_7.1/page/Content/ActivityMonitor/Install/Upgrade.htm)
2. Removed IIS from the Roles and Features via Windows Server Manager.
3. Noted the expiration date of the SSL certificate for NEA and AIC URLs (11/1/2024).
4. Prepared commands for updating the SSL certificate post-upgrade.
5. Confirmed antivirus exclusions for Netwrix Enterprise Auditor.
6. Reviewed Azure App Authentication jobs for potential issues.

## Root Cause
The need for the upgrade was driven by the presence of known bugs in the previous versions of the software, which were addressed in the newer versions.

## Solution
The upgrade was successfully executed, transitioning from:
- **From:**
  - NEA: 11.6.0.49
  - AIC: 11.6.0.7
  - SAM: 6.0.928
- **To:**
  - NEA: 11.6.0.92
  - AIC: 11.6.0.23
  - SDD: 11.6.0.13
  - NAM: 7.1.165

Post-upgrade, the SSL certificate update commands were prepared for execution once the new certificate was available.

## Notes
- The SSL certificate for NEA and AIC is set to expire on 11/1/2024; ensure to replace it before this date.
- The installation of new certificates must be done in the Host Certificates store under the personal path via the control panel.
- The guidance for the AADI_RegisterAzureAppAuth job is currently not available; further documentation may be needed for future reference.
- Ensure antivirus exclusions are confirmed as per the guidelines provided in the Netwrix documentation.