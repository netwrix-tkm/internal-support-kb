## Ticket Metadata
- **Ticket ID:** 500Qk00000DCWsjIAH
- **Case Number:** 415312
- **Status:** Closed - Resolved
- **Account/Company:** (add)ventures
- **Contact Name:** Mark Laslo
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Upgrade
- **Version:** 5.9.30

## Problem Description
The customer reported an issue during a server upgrade, receiving an error message stating: "Database partitions are disabled! Please contact Support for assistance!"

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Age of the system:** 8.8 years

## Troubleshooting Steps
1. Attempted to identify the cause of the error message regarding disabled database partitions.
2. Deployed the Offline Partitioning Patch to address the partitioning issue.
3. Created a snapshot of the EPP server prior to making changes.
4. Upgraded the system to version 5.9.30.
5. Applied the hotfix (adv-2024-002) to resolve the error.
6. Provided EPP clients containing the hotfix on the client side.

## Root Cause
The root cause of the issue was related to disabled database partitions, which prevented the server upgrade from proceeding successfully.

## Solution
The issue was resolved by:
- Deploying the Offline Partitioning Patch, which enabled the necessary database partitions.
- Applying the hotfix (adv-2024-002) that removed the error message.
- Successfully upgrading the server to version 5.9.30 after addressing the partitioning issue.

## Notes
- Ensure that database partitions are enabled before attempting server upgrades in the future to avoid similar issues.
- Always create a snapshot of the server before performing upgrades or applying patches to facilitate recovery if needed.