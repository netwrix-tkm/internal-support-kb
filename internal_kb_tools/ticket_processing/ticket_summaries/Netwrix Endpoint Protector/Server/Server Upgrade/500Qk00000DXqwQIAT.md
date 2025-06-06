## Ticket Metadata
- **Ticket ID:** 500Qk00000DXqwQIAT
- **Case Number:** 416103
- **Status:** Closed - Resolved
- **Account/Company:** Grampian Housing Association
- **Contact Name:** Martin Laws
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Upgrade
- **Version:** 5930

## Problem Description
The customer reported issues after applying the security patch upgrade EPP4-U8800, as the dashboard continued to prompt that the upgrade was not installed correctly.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Build Number:** 5930

## Troubleshooting Steps
1. Verified the application of the security patch upgrade EPP4-U8800.
2. Checked the dashboard for any error messages or prompts regarding the upgrade status.
3. Confirmed the installation logs to ensure the patch was applied correctly.
4. Investigated any potential conflicts or issues with previous versions or patches.
5. Applied the Deployed Hotfix adv-2024-002 as a potential resolution.

## Root Cause
The issue was identified as a miscommunication between the dashboard and the installed patch, which led to the dashboard incorrectly indicating that the upgrade was not installed.

## Solution
The problem was resolved by successfully applying the Deployed Hotfix adv-2024-002, which corrected the dashboard's reporting and confirmed that the upgrade EPP4-U8800 was installed correctly.

## Notes
- Ensure to monitor the dashboard after applying upgrades to confirm that the status reflects the correct installation.
- If similar issues arise, consider checking for any additional hotfixes that may address dashboard reporting discrepancies.