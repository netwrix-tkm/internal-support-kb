## Ticket Metadata
- **Ticket ID:** 500Qk00000FotogIAB
- **Case Number:** 421114
- **Status:** Closed - Resolved
- **Account/Company:** Kerry Group Services International Limited
- **Contact Name:** Cameron Bowlds
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** NEA Web Report Console
- **Version:** 11.6

## Problem Description
The customer reported an issue with Single Sign-On (SSO) functionality after an update to version 11.6 of the Netwrix Enterprise Auditor. The ADFS configuration was validated as correct, but the SSO was not functioning as expected.

## Environment Details
- **Configuration File Location:** `D:\Program Files (x86)\STEALTHbits\StealthAUDIT\Web\webserver.exe.config`
- **Update Date:** 8/30

## Troubleshooting Steps
1. Verified the ADFS configuration settings were correct and unchanged.
2. Checked the `webserver.exe.config` file for any modifications during the update process.
3. Updated the `WsFederationMetadata`, `WsFederationRealm`, and `WsFederationReply` settings with the correct ADFS information as per the documentation.
4. Attempted to restore older configuration files from 2021 marked with the `.old` extension, but this caused the webserver/Enterprise Auditor to become unresponsive.
5. Restored the `webserver.exe.config` file to its pre-modified state before any changes were made during troubleshooting.

## Root Cause
The issue was caused by the assignment of an old certificate to the Publish Report, which was not compatible with the updated configuration after the version 11.6 update.

## Solution
The issue was resolved by deleting the old certificate that was assigned to the Publish Report and assigning a new certificate. This action restored the SSO functionality.

## Notes
- Ensure that any certificates used for the Publish Report are up-to-date and compatible with the current configuration to avoid similar issues in the future.
- Regularly back up configuration files before applying updates to facilitate easier recovery in case of issues.