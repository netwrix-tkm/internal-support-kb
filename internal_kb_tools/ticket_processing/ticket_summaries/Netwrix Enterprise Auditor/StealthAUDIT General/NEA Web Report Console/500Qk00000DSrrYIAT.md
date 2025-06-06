## Ticket Metadata
- **Ticket ID:** 500Qk00000DSrrYIAT
- **Case Number:** 415855
- **Status:** Closed - Resolved
- **Account/Company:** CPP Corp
- **Contact Name:** Benjamin Tanner
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** NEA Web Report Console
- **Version:** 11.5

## Problem Description
The customer reported that after updating the certificate as per previous instructions, the "Access" tab on the Published Reports site was no longer loading and instead returned a 500 error.

## Environment Details
- Customer Location: US (Ohio)
- Product Version: 11.5

## Troubleshooting Steps
1. Verified that both sites were secured and compared the certificate thumbprints.
2. Navigated to `%SAInstallDir%Web` and opened the `WebServer.exe.config` file using a text editor.
3. Checked the `AdditionalContentTabs` line for its value.
4. Noted that the value was reset to default/missing.
5. Edited the `AdditionalContentTabs` line to include the correct value: `Access, https://+:481/v2/login?embed`.
6. Restarted the StealthAUDIT Web Server service.

## Root Cause
The issue was caused by the `AdditionalContentTabs` value in the `WebServer.exe.config` file being reset to default or missing after the certificate update.

## Solution
To resolve the issue, the following steps were taken:
1. Ensured both sites were using the same certificate by comparing their thumbprints.
2. Edited the `WebServer.exe.config` file to set the `AdditionalContentTabs` value to:
   ```plaintext
   Access, https://+:481/v2/login?embed
   ```
3. Restarted the StealthAUDIT Web Server service to apply the changes.

## Notes
- Always ensure that the `AdditionalContentTabs` configuration is correctly set after any updates to the certificate or related configurations.
- If encountering a 500 error, check the configuration files for any missing or default values that may have been reset during updates.