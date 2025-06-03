## Ticket Metadata
- **Ticket ID:** 500Qk00000LUrlxIAD
- **Case Number:** 434719
- **Status:** Closed - Resolved
- **Account/Company:** Provable Labs
- **Contact Name:** Alexei Kozlenok
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Install/Uninstall
- **Version:** NONE

## Problem Description
The customer reported that after successfully installing the EPP Client application on a Linux machine, the application did not show any server connection, and the machine was not visible in the Web UI.

## Environment Details
- Operating System: Linux
- Product: Netwrix Endpoint Protector (EPP) Client

## Troubleshooting Steps
1. Gathered initial details regarding the connectivity issue.
2. Scheduled a remote session to investigate the cause further.
3. Reviewed the installation process and configuration files, particularly the `options.sh` file.

## Root Cause
The issue was identified as a misconfiguration in the `options.sh` file, specifically related to the export lines that were commented out, preventing the EPP Client from establishing a connection with the EPP Server.

## Solution
The issue was resolved by:
- Reinstalling the latest version of the EPP Client.
- Uncommenting the necessary export lines within the `options.sh` file.
After these changes, the EPP Client was able to communicate with the EPP Server as expected.

## Notes
- Ensure that the `options.sh` file is correctly configured during installation to avoid similar connectivity issues in the future.
- Always verify the visibility of the client in the Web UI post-installation to confirm successful communication with the server.