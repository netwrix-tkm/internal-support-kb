## Ticket Metadata
- **Ticket ID:** 500Qk00000LXikZIAT
- **Case Number:** 434829
- **Status:** Closed - Resolved
- **Account/Company:** Better World Technology Private Limited / Directi Group
- **Contact Name:** Shoeb Amin
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device Settings
- **Version:** EPP Server version: 5.9.4.1, EPP client version: 6.2.4.2000

## Problem Description
The Directi team reported that despite having the "Disable Bluetooth File Transfer" option enabled on a test Windows computer, they were still able to transfer files via Bluetooth.

## Environment Details
- **EPP Server Version:** 5.9.4.1
- **EPP Client Version:** 6.2.4.2000

## Troubleshooting Steps
1. Verified the configuration of the "Disable Bluetooth File Transfer" setting on the test Windows computer.
2. Conducted tests to replicate the issue by attempting to transfer files via Bluetooth.
3. Provided instructions to the client on how to properly test the feature.
4. Suggested disabling the Bluetooth File Transfer setting on a user/computer/group level.

## Root Cause
The initial configuration of the "Disable Bluetooth File Transfer" setting was not applied correctly at the user/computer/group level, which allowed file transfers to occur despite the setting being enabled.

## Solution
The issue was resolved by disabling the Bluetooth File Transfer setting specifically on a user/computer/group level as per the provided instructions. After making this adjustment, the client confirmed that the ability to transfer files via Bluetooth was successfully blocked.

## Notes
- Ensure that the "Disable Bluetooth File Transfer" setting is applied at the appropriate level (user/computer/group) to prevent similar issues in the future.
- It is advisable to conduct thorough testing after configuration changes to confirm that the desired restrictions are in place.