## Ticket Metadata
- **Ticket ID:** 500Qk00000NYkSzIAL
- **Case Number:** 440590
- **Status:** Closed - Resolved
- **Account/Company:** Satcom Infotech
- **Contact Name:** Sai Nachiappan
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Client - Other
- **Feature:** CAP Logs
- **Version:** 6.2.4.2

## Problem Description
The customer reported that they were not receiving any CAP logs in the EPP UI console. They indicated that the logs were showing data only from three months prior, and some devices were not displaying any logs at all.

## Environment Details
- The customer has two CAP policies: one for MacOS and one for Windows.
- The issue was affecting both MacOS and Windows machines.

## Troubleshooting Steps
1. The support team requested additional details regarding the issue.
2. A remote session was conducted to assist the customer with denylist dictionaries and their Google business accounts.
3. The team updated the client to version 6.2.4.2.
4. DPI for Microsoft Teams was enabled and included as an exit point in the CAP policy.
5. The team verified the URL denylist to ensure it was functioning correctly.
6. A follow-up session was scheduled to address issues related to MacOS machines.

## Root Cause
The primary issue was identified as the EPP certificate not being trusted in the keychain access on the MacOS machines. This prevented the proper logging of CAP events.

## Solution
- During the remote session, the support team successfully resolved the URL denylist issue that was not blocking correctly.
- The EPP certificate was set to "always trust" in the keychain access on the MacOS machine, and the machine was restarted to apply the changes.
- After these adjustments, the logs began to appear correctly in the EPP UI console.

## Notes
- Ensure that the EPP certificate is trusted in the keychain access on MacOS machines to avoid similar issues in the future.
- Regularly verify the functionality of denylist policies to ensure they are blocking as intended.
- Follow-up sessions may be necessary for comprehensive troubleshooting, especially when multiple operating systems are involved.