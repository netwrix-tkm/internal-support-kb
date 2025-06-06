## Ticket Metadata
- **Ticket ID:** 500Qk00000CcGCvIAN
- **Case Number:** 413895
- **Status:** Closed - Resolved
- **Account/Company:** Halodata International Pte Ltd
- **Contact Name:** Halodata Support Tech
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Upgrade
- **Version:** 5.9.3.0

## Problem Description
The customer reported that they were unable to access a live update for a hotfix while using version 5.9.3.0 of the Netwrix Endpoint Protector. Additionally, they requested an upgrade to version 6.2.2.2005.

## Environment Details
- **Current Version:** 5.9.3.0
- **Requested Upgrade Version:** 6.2.2.2005

## Troubleshooting Steps
1. Acknowledged the customer's request and confirmed the issue regarding the unavailability of the hotfix.
2. Informed the customer that Netwrix had temporarily paused the distribution of the hotfix due to reported issues with Hotfix #1, which caused the system to cease processing certain events.
3. Communicated that a revision to Hotfix #1 was in progress and that the client version would be provided once the patch was live again.
4. Followed up with the customer to notify them when the hotfix became available under the Live Update menu.
5. Advised the customer to take a snapshot of their virtualization environment before applying the hotfix.

## Root Cause
The unavailability of the hotfix was due to a temporary pause in distribution by Netwrix, which was implemented after reports of the hotfix causing issues with event processing.

## Solution
The issue was resolved by deploying Hotfix adv-2024-002, which became available under the Live Update menu. The customer was instructed to apply the hotfix and verify that the system was functioning correctly afterward.

## Notes
- Customers should always take a snapshot of their virtualization environment before applying any hotfixes or updates to ensure they can revert back if issues arise.
- It is important to monitor for any announcements regarding hotfixes or patches, especially if previous versions have caused issues.