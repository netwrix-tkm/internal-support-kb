## Ticket Metadata
- **Ticket ID:** 500Qk00000NpuPZIAZ
- **Case Number:** 441375
- **Status:** Closed - Resolved
- **Account/Company:** Acacia Communications, Inc.
- **Contact Name:** Nicholas Smits
- **Product:** Netwrix Enterprise Auditor
- **Component:** File System Scanning Proxy
- **Feature:** Proxy
- **Version:** 12.0

## Problem Description
The customer was unable to install the 'File System Scanning Proxy' after upgrading from version 11.6 to 12.0 of the Netwrix Enterprise Auditor. The installation failed with a 'can't find license' error message, and the installer crashed when attempting to browse for the license file on a Server Core environment.

## Environment Details
- Operating System: Server Core (no UI)
- Previous Version: Netwrix Enterprise Auditor v11.6
- Current Version: Netwrix Enterprise Auditor v12.0
- Installer Used: `auditor-enterprise-FileSystemProxy-12.0.0.1030.msi`

## Troubleshooting Steps
1. Attempted to run the 'FS_UpdateProxy' instant job after the upgrade, which failed with a key error.
2. Uninstalled the previous proxy version from the Proxy Servers.
3. Tried to reinstall the proxy using the installer, but encountered a license error.
4. Copied the `StealthAudit.lic` file to the same folder as the installer.
5. Attempted to use the 'Browse' button to locate the license file, which caused the installer to crash.
6. Requested clarification on the license file usage and command line arguments for installation.

## Root Cause
The issue was primarily due to the limitations of the Server Core environment, which does not support the graphical interface required for the installer to function properly. The installer could not locate the license file because the 'Browse' functionality was not operational in this environment.

## Solution
The issue was resolved by using a command line argument to specify the license file directly during installation. The successful command was:
```bash
msiexec /i auditor-enterprise-FileSystemProxy-12.0.0.1030.msi LICENSE_FILE=C:\Users\username\StealthAUDIT.LIC
```
This command allowed the installation to proceed without requiring the graphical interface.

## Notes
- Ensure that the command line argument for the license file is documented for future reference, especially for installations on Server Core environments.
- The previous version of the proxy (11.6) is not compatible with the new version (12.0), so it is essential to uninstall the old version before attempting to install the new one.
- Always verify that no remnants of the previous installation are left on the system before proceeding with a new installation to avoid conflicts.