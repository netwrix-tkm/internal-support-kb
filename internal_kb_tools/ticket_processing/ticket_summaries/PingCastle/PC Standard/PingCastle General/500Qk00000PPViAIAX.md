## Ticket Metadata
- **Ticket ID:** 500Qk00000PPViAIAX
- **Case Number:** 445795
- **Status:** Closed - Resolved
- **Account/Company:** Kufgem GmbH
- **Contact Name:** Christian Steindl
- **Product:** PingCastle
- **Component:** PC Standard
- **Feature:** PingCastle General
- **Version:** 3.3

## Problem Description
The customer reported an issue with the PingCastle software after upgrading from version 3.3.0.1 to 3.3.0.11. Upon launching the new version, they received an error message stating, "The program is unsupportet since: 2025-05-17 00:00:00Z," leading them to question whether a new license was required despite having renewed it a few months prior.

## Environment Details
- **Software Version:** 3.3.0.11
- **Previous Version:** 3.3.0.1
- **License Status:** Renewed a few months prior to the incident.

## Troubleshooting Steps
1. Verified the license key used for the new version of PingCastle.
2. Checked for any updates or patches related to the software.
3. Attempted to reinstall the application to see if the issue persisted.
4. Consulted internal documentation regarding license propagation for upgraded versions.

## Root Cause
The issue was identified as a failure in the license propagation when downloading and installing PingCastle version 3.3.0.11. The software did not recognize the existing license due to this propagation issue.

## Solution
The problem was resolved by using the auto-updater feature within the PingCastle application. This ensured that the application was updated correctly, allowing it to recognize the existing license key, thus eliminating the error message.

## Notes
- Ensure that users are aware of the importance of using the auto-updater for future upgrades to avoid similar license propagation issues.
- It may be beneficial to remind users to check for updates regularly, especially after a major version change.