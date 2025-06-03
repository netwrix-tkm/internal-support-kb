## Ticket Metadata
- **Ticket ID:** 500Qk00000ClfgjIAB
- **Case Number:** 414248
- **Status:** Closed - Resolved
- **Account/Company:** Landratsamt Heidenheim
- **Contact Name:** Alisa Grupp
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** Not specified

## Problem Description
The customer reported an issue where deploying a security update via "Live Update" appeared to complete successfully, but upon refreshing the page, the system indicated that an update was required again.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Server

## Troubleshooting Steps
1. Confirmed the deployment of the security update through "Live Update."
2. Informed the customer that the hotfix would remain listed in the update options even after installation.
3. Suggested checking the "View Applied Patches" section to confirm the patch installation.
4. Provided links to download the necessary client for both MacOS and Windows.
5. Asked the customer to verify if the server was receiving logs.

## Root Cause
The issue was identified as a characteristic of the hotfix deployment process, where the hotfix remains listed in the update options even after successful installation. This behavior is expected and does not indicate a failure in the update process.

## Solution
The issue was resolved by clarifying to the customer that the hotfix would continue to appear in the update options post-installation. The customer was advised to check the "View Applied Patches" to confirm the installation of the patch and to ignore the repeated update prompt. Additionally, the necessary client software was provided for installation.

## Notes
- It is important to inform customers that hotfixes may remain visible in the update options after installation, and this is normal behavior.
- Always ensure that the customer verifies log reception on the server to confirm proper functionality post-update.
- Provide direct download links for any required client software to facilitate a smoother resolution process.