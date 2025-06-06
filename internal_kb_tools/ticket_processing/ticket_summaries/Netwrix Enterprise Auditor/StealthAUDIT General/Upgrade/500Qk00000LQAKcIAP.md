## Ticket Metadata
- **Ticket ID:** 500Qk00000LQAKcIAP
- **Case Number:** 434488
- **Status:** Closed - Resolved
- **Account/Company:** EverBank
- **Contact Name:** Bradley Dickinson
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Upgrade
- **Version:** 11.6.0.132

## Problem Description
The customer, EverBank, requested an upgrade of their StealthAudit application from version 11.5 to version 11.6. The upgrade was planned for the Dev environment, and they required support during the upgrade process.

## Environment Details
- **Upgrade Date:** March 20, 2025, at 3 PM
- **Components Involved:**
  - Console Server
  - Proxy Server (used for NetApp scans)
  - Sensitive Data Discovery Add-on
  - SharePoint Sensitive Data Agent
  - Activity Monitor

## Troubleshooting Steps
1. Scheduled pre-flight and upgrade meetings.
2. Upgraded StealthAudit from version 11.5.210 to 11.6.0.132.
3. Verified functionality of:
   - ADI scan
   - Reporting console
   - Activity Monitor (AIC)
4. Upgraded the following components:
   - Sensitive Data Discovery
   - File Server Proxy
   - SharePoint Proxy
   - Sensitive Data Add-on
5. Investigated certificate errors related to FSAA scans and SharePoint scans.
6. Resolved folder structure issues in SharePoint jobs post-upgrade.

## Root Cause
The upgrade process introduced changes that affected the folder structure of SharePoint jobs and caused certificate errors in the FSAA scans. The errors were primarily due to legacy configurations and missing properties in the upgraded environment.

## Solution
- The upgrade was successfully completed, and the following components were verified to be functioning correctly:
  - ADI scan
  - Reporting console
  - AIC
- The folder structure for SharePoint jobs was restored to its pre-upgrade state.
- A separate enhancement request was opened to address the warning/error labeling issue in future versions.

## Notes
- The error regarding the "IsSystemList" property in SharePoint scans was identified as a cosmetic issue and should not impact functionality. An enhancement request was opened to address this in future updates.
- The customer was advised to ensure that firewall settings allowed access to necessary ports (HTTP/HTTPS) for proper functionality.
- Future upgrades should consider the potential for legacy configurations to cause issues and ensure thorough testing in a Dev environment before proceeding to production.