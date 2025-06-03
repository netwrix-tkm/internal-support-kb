## Ticket Metadata
- **Ticket ID:** 500Qk00000FVbkEIAT
- **Case Number:** 420399
- **Status:** Closed - Resolved
- **Account/Company:** Helo.ai
- **Contact Name:** Qazi Amir
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Install/Uninstall
- **Version:** EPP version 12.0 & 11.4

## Problem Description
The customer reported an issue with a system running Ubuntu 22.04, where internet access was lost following the installation of the Endpoint Protection Platform (EPP).

## Environment Details
- **Operating System:** Ubuntu 22.04
- **Software Installed:** Endpoint Protection Platform (EPP) version 12.0 & 11.4

## Troubleshooting Steps
1. Verified that the internet connection was functional when the EPP client was disabled.
2. Suggested the customer test the issue with the latest version of the EPP client.
   - Provided the download link for the latest version: 
     ```
     https://download.endpointprotector.com/linux_agent/EPPLinux_v2.4.4.1003/EPPClient_ubuntu_22.04_v2.4.4.1003_x86_64.tar.gz
     ```

## Root Cause
The issue was identified as being caused by the EPP client interfering with the system's network settings, leading to the loss of internet connectivity.

## Solution
The problem was resolved by advising the customer to update to the latest version of the EPP client, which addressed the compatibility issues with Ubuntu 22.04. The customer confirmed that after the update, the internet access was restored, and the case could be closed.

## Notes
- Ensure that customers are always using the latest version of the EPP client, especially when running newer operating systems like Ubuntu 22.04, to avoid similar issues.
- Monitor for any future updates or patches from Netwrix that may address compatibility issues with specific operating systems.