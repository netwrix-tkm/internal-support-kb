```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000GdSKzIAN
- **Case Number:** 422961
- **Status:** Closed - Resolved
- **Account/Company:** Arista Networks, Inc.
- **Contact Name:** Andy Lim (andy.lim@arista.com)
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Client
- **Feature:** EPP Client - Other
- **Version:** 1.7.0-7ubuntu0

## Problem Description
The user reported that the EPP Client is continually crashing on their Ubuntu 22.04 system, displaying an internal error message and prompting to send a problem report to developers.

## Environment Details
- **Operating System:** Ubuntu 22.04
- **Architecture:** amd64
- **Desktop Environment:** GNOME
- **Installation Date:** January 6, 2023
- **Kernel Version:** 5.14.0-1056-oem
- **Executable Path:** /opt/cososys/bin/epp-client

## Troubleshooting Steps
1. Collected crash report details including the error message and stack trace.
2. Verified the installation of the EPP Client and its dependencies.
3. Checked for any known issues with the EPP Client on Ubuntu 22.04.
4. Attempted to restart the application and the system as suggested in the error message.
5. Reviewed system logs for any additional error messages related to the crash.

## Root Cause
The root cause of the issue was identified as a compatibility problem between the EPP Client version 1.7.0-7ubuntu0 and the Ubuntu 22.04 operating system. The crash was triggered by a SIGABRT signal in the QMessageLogger::fatal() function, indicating an internal error within the application.

## Solution
The issue was resolved by updating the EPP Client to a newer version that included fixes for compatibility with Ubuntu 22.04. The customer confirmed that after the update, the application no longer crashed and functioned as expected.

## Notes
- Ensure that the EPP Client is regularly updated to the latest version to avoid compatibility issues with new operating system releases.
- Monitor for any similar crash reports from users on Ubuntu 22.04 and advise them to update their EPP Client if they encounter similar issues.
```