## Ticket Metadata
- **Ticket ID:** 500Qk00000JljZsIAJ
- **Case Number:** 430520
- **Status:** Closed - Resolved
- **Account/Company:** Motorola Solutions Inc
- **Contact Name:** Joe Cutter
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client - BSOD
- **Version:** Latest version of EPP-client

## Problem Description
Linux clients running the latest version of the EPP-client were experiencing kernel panics when users attempted to browse to a repository directory and initiate syncing. The issue resulted in the entire computer crashing during the sync process.

## Environment Details
- **Operating System:** Linux
- **Client Version:** Latest version of EPP-client

## Troubleshooting Steps
1. Collected user reports regarding the issue, including specific scenarios that triggered the kernel panic.
2. Investigated the possibility of running sync operations with trace logging enabled.
3. Tested the effect of throttling sync operations on the client.
4. Assessed the impact of disabling parallelization during the sync process.

## Root Cause
The root cause of the kernel panic was not explicitly identified in the case. However, user feedback indicated that certain configurations, such as throttling and disabling parallelization, mitigated the issue, suggesting a potential conflict in how the EPP-client handled resource allocation during sync operations.

## Solution
The issue was resolved by implementing workarounds based on user feedback:
- Running sync operations with trace logging enabled.
- Throttling the sync process to reduce resource strain.
- Disabling parallelization during sync operations to prevent kernel panics.

These adjustments allowed users to successfully sync without encountering crashes.

## Notes
- Future users experiencing similar issues should consider applying the workarounds mentioned above.
- It may be beneficial to monitor for updates or patches from Netwrix that address the underlying cause of the kernel panic in future releases of the EPP-client.
- Document any new findings or changes in behavior if the issue reoccurs, as this may assist in identifying a permanent fix.