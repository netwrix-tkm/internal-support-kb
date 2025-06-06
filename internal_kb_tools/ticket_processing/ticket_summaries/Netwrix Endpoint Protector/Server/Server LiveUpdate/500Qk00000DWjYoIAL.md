## Ticket Metadata
- **Ticket ID:** 500Qk00000DWjYoIAL
- **Case Number:** 416043
- **Status:** Closed - Resolved
- **Account/Company:** Kreis Weseler Abfallgesellschaft mbH & Co. KG
- **Contact Name:** Adrian Stanca
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server LiveUpdate
- **Version:** Not specified

## Problem Description
The customer reported an issue where the installation of Hotfix 1.1 via Live Update resulted in a loop. The hotfix continued to show as available in Live Update, despite being listed as installed under "View applied updates." Attempts to reinstall the hotfix did not resolve the issue, leading to it being displayed twice under applied updates.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Server

## Troubleshooting Steps
1. Verified the installation status of Hotfix 1.1 through the "View applied updates" section.
2. Attempted to reinstall the hotfix to check if the issue would resolve itself.
3. Checked for any conflicting updates or system logs that might indicate the cause of the loop.

## Root Cause
The root cause of the issue was identified as a bug in the Live Update mechanism that caused the hotfix to be incorrectly flagged as both installed and available for installation simultaneously.

## Solution
The issue was resolved when the vulnerabilities associated with the hotfix were addressed in a subsequent update. The customer was advised to ensure that their system was updated to the latest version to prevent similar issues in the future.

## Notes
- It is important to monitor the status of hotfixes and updates regularly to avoid confusion with installed and available updates.
- Customers should be encouraged to report any discrepancies in update statuses promptly to facilitate quicker resolutions.