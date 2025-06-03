## Ticket Metadata
- **Ticket ID:** 500Qk00000NcBhzIAF
- **Case Number:** 440758
- **Status:** Closed - Resolved
- **Account/Company:** Trustly
- **Contact Name:** Rodrigo Monteiro
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Upgrade
- **Version:** Not specified

## Problem Description
The customer reported that the Netwrix Endpoint Protector (EPP) was not updating when selecting groups where users were added based on their username. The updates were only successful for groups where users were added based on their hostname.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Issue Type:** Other
- **Ticket Type:** Unexpected Behavior

## Troubleshooting Steps
1. Clarified the issue with the customer regarding the upgrade process through the console.
2. Confirmed that the customer was selecting the correct groups for the upgrade.
3. Identified that groups synced from Active Directory (AD) were not updating, while manually created groups were functioning correctly.

## Root Cause
The issue was identified as a limitation in the EPP client upgrade process, where the system did not properly handle updates for groups based on usernames when synced from AD.

## Solution
The resolution involved recommending a best practice for future upgrades: to target computers instead of users when performing EPP client upgrades. This approach ensures that all relevant endpoints receive the updates without the issues encountered with user-based group selections.

## Notes
- It is important to follow the recommended best practice of targeting computers for client upgrades to avoid similar issues in the future.
- Ensure that any groups synced from AD are verified for compatibility with the upgrade process before proceeding.