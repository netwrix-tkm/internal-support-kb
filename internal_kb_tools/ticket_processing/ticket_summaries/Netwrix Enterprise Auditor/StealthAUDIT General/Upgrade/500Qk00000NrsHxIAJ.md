## Ticket Metadata
- **Ticket ID:** 500Qk00000NrsHxIAJ
- **Case Number:** 441473
- **Status:** Closed - Resolved
- **Account/Company:** HBK Capital Management
- **Contact Name:** Gill Cerros
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Upgrade
- **Version:** 11.5

## Problem Description
The customer requested guidance on upgrading from version 11.5 to 12.0 of Netwrix software. They were unsure if their current features (threat prevention, threat manager, and FSAA) were compatible with the upgrade process, and they needed confirmation on the upgrade steps.

## Environment Details
- Current version: 11.5.1332.890
- Instance type: EC2 instance
- Database: RDS instance

## Troubleshooting Steps
1. Provided the customer with links to the upgrade documentation for both 11.5 to 11.6 and 11.6 to 12.0.
2. Recommended performing an upgrade to 11.6 first to ensure stability before proceeding to 12.0.
3. Suggested taking full snapshots of both the StealthAUDIT and SQL servers prior to the upgrade.
4. Offered to schedule a preflight meeting to review current settings and discuss the upgrade process in detail.

## Root Cause
The customer was seeking a structured approach to upgrade their software version, which required confirmation of compatibility and detailed upgrade instructions.

## Solution
The issue was resolved by providing the customer with comprehensive documentation for the upgrade process, including:
- Upgrade from 11.5 to 11.6: [Upgrade Guide](https://helpcenter.netwrix.com/bundle/EnterpriseAuditor_11.6/page/Content/EnterpriseAuditor/Install/Application/Upgrade/Wizard.htm)
- Upgrade from 11.6 to 12.0: [Upgrade Guide](https://helpcenter.netwrix.com/bundle/AccessAnalyzer_12.0/page/Content/EnterpriseAuditor/Install/Application/Upgrade/Wizard.htm)

The customer acknowledged receipt of the documentation and indicated they would proceed with the upgrade at their convenience.

## Notes
- It is strongly advised to have a Netwrix engineer assist with the upgrade process to ensure a smooth transition.
- Always take full backups of the servers before performing any upgrades to prevent data loss.
- Ensure that all current features and integrations are compatible with the new version before proceeding with the upgrade.