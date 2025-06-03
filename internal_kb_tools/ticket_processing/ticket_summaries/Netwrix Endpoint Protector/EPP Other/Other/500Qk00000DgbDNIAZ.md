## Ticket Metadata
- **Ticket ID:** 500Qk00000DgbDNIAZ
- **Case Number:** 416342
- **Status:** Closed - Resolved
- **Account/Company:** Claranet Portugal (OutScope Solutions S.A.)
- **Contact Name:** Helio Ferreira
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Other
- **Version:** 5.9.0.0, 5.9.1.0, 5.9.2.0, 5.9.3.0

## Problem Description
The customer reported issues with deploying a hotfix (Security Update – EPP Server Hotfix #1.1) in the Dashboard tab under Live Update. The hotfix appeared to complete deployment but reappeared after refreshing the page. Additionally, some clients were displayed in grey during an upgrade job, preventing selection despite being online and licensed.

## Environment Details
- **Hotfix Version:** v1.1
- **Affected Versions:** 5.9.0.0, 5.9.1.0, 5.9.2.0, 5.9.3.0

## Troubleshooting Steps
1. Verified the status of the hotfix deployment in the Live Update section.
2. Attempted to deploy the hotfix multiple times, observing that it reached 100% completion each time.
3. Refreshed the Dashboard page to check if the hotfix status changed.
4. Created an Upgrade Job for clients, selecting the newest version and proceeding to the computer selection step.
5. Noted which clients appeared in grey and confirmed their online status and licensing.

## Root Cause
The issue with the hotfix not being applied was due to a backend process not completing successfully, despite the frontend indicating a successful deployment. The greyed-out clients were likely due to a mismatch in version compatibility or licensing issues that were not immediately apparent.

## Solution
The issue was resolved by:
- Restarting the backend services associated with the Netwrix Endpoint Protector, which allowed the hotfix to be applied successfully.
- Ensuring that all clients were updated to compatible versions and verifying their licensing status to allow for successful selection during the upgrade job.

## Notes
- It is recommended to monitor the backend processes after deploying hotfixes to ensure they complete successfully.
- For clients appearing in grey, always verify version compatibility and licensing status before proceeding with upgrades.
- Regularly check for updates and patches to avoid similar issues in the future.