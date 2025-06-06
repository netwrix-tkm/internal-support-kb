## Ticket Metadata
- **Ticket ID:** 500Qk00000NMkoZIAT
- **Case Number:** 440100
- **Status:** Closed - Resolved
- **Account/Company:** Kootenai Health
- **Contact Name:** Todd Wyman
- **Product:** Netwrix Enterprise Auditor
- **Component:** NEA, AIC
- **Feature:** Upgrade
- **Version:** 11.6.0.138

## Problem Description
The customer reported a bug in their SharePoint SDD scans and requested an upgrade to several components of the Netwrix Enterprise Auditor to the latest cumulative update (CU) release version 11.6.0.138, as they were currently on version 11.6.0.134.

## Environment Details
- Current version: 11.6.0.134
- Components to be updated:
  - Proxy agents and SDD plugins
  - NEA and SDD module
  - Access Information Center (AIC)

## Troubleshooting Steps
1. Confirmed the current versions of the components:
   - NEA: 11.6.0.134
   - AIC: 11.6.0.36
   - FSAA Proxy: 11.6.0.37 (latest)
   - SDD: 11.6.0.18 (latest)
2. Scheduled a preflight meeting to review current settings and discuss the upgrade process.
3. Conducted the preflight meeting to assess the current configuration and plan the upgrade.
4. Upgraded the Netwrix Enterprise Auditor and the Access Information Center to version 11.6.0.138 and 11.6.0.37 respectively.

## Root Cause
The issue was caused by a bug in the SharePoint SDD scans that required an upgrade to the latest version of the Netwrix Enterprise Auditor and its components.

## Solution
The upgrade was successfully performed by:
- Upgrading the Netwrix Enterprise Auditor to version 11.6.0.138.
- Upgrading the Access Information Center to version 11.6.0.37.
- Confirming that the latest versions of the proxy agents and SDD plugins were already in place, thus no further upgrades were necessary for those components.

## Notes
- Ensure to verify the current versions of all components before planning an upgrade to avoid unnecessary updates.
- Always conduct a preflight meeting to assess the current settings and configurations before proceeding with upgrades.
- Advise customers to log in to the report and AIC sites post-upgrade to confirm access and functionality.