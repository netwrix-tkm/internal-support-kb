## Ticket Metadata
- **Ticket ID:** 500Qk00000FoGaRIAV
- **Case Number:** 421100
- **Status:** Closed - Resolved
- **Account/Company:** Innovaccer
- **Contact Name:** Gaurav Sonone
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Upgrade
- **Version:** NONE

## Problem Description
The customer reported that after applying the Hotfix (ADV-2024-002) to the server, they were unable to upgrade the client software to the recommended versions as these versions were not available in the Client Software Upgrade section under System Configurations.

## Environment Details
- **Hotfix Applied:** ADV-2024-002
- **Platform:** Netwrix Endpoint Protector

## Troubleshooting Steps
1. Verified that the Hotfix ADV-2024-002 was successfully deployed on the server.
2. Checked the Client Software Upgrade section under System Configurations for the availability of recommended client versions.
3. Reviewed server logs for any errors or warnings related to the client upgrade process.
4. Confirmed that the server was properly configured to allow client upgrades.

## Root Cause
The root cause of the issue was identified as a misconfiguration in the server settings that prevented the recommended client versions from being displayed in the Client Software Upgrade section.

## Solution
The issue was resolved by correcting the server configuration settings, which allowed the recommended client versions to be displayed properly in the Client Software Upgrade section. After the configuration was updated, the customer was able to successfully upgrade the client software.

## Notes
- Ensure that server configurations are verified after applying any hotfixes to prevent similar issues in the future.
- It is advisable to document any changes made to server settings for future reference and troubleshooting.