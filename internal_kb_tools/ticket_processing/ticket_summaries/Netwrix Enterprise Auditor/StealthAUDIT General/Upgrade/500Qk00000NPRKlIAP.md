## Ticket Metadata
- **Ticket ID:** 500Qk00000NPRKlIAP
- **Case Number:** 440257
- **Status:** Closed - Resolved
- **Account/Company:** G-III Apparel Group
- **Contact Name:** David Wong
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Upgrade
- **Version:** 11.6

## Problem Description
The customer requested assistance in upgrading the Netwrix Enterprise Auditor from version 11.6.0.92 to 11.6.0.138.

## Environment Details
- The upgrade involved transitioning from version 11.6.0.92 to a later version, with the schema job already completed prior to the upgrade request.

## Troubleshooting Steps
1. Scheduled a pre-flight call to collect system information before the upgrade.
2. Provided a backup script to ensure data safety during the upgrade process.
3. Conducted the upgrade to version 12.0 instead of the initially requested 11.6.0.138.
4. Validated that Active Directory Integration (ADI) scans were functioning correctly post-upgrade.
5. Confirmed that the schema creation was completed successfully.

## Root Cause
The initial request was for an upgrade to version 11.6.0.138; however, it was determined that upgrading directly to version 12.0 was more beneficial and aligned with the latest features and improvements.

## Solution
The upgrade was successfully completed to version 12.0. Post-upgrade validation confirmed that all functionalities, including ADI scans and schema creation, were operational.

## Notes
- Ensure that customers are aware that upgrades may involve moving to a more recent version than initially requested for optimal performance and features.
- Always provide backup scripts and schedule pre-flight calls to gather necessary system information before proceeding with upgrades.