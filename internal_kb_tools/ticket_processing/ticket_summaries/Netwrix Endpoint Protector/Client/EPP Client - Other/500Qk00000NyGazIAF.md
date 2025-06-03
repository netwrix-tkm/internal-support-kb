## Ticket Metadata
- **Ticket ID:** 500Qk00000NyGazIAF
- **Case Number:** 441815
- **Status:** Closed - Resolved
- **Account/Company:** Sauce Labs
- **Contact Name:** Anish Mehta
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** EPP Client - Other
- **Version:** 3.0.4.1006

## Problem Description
The customer reported that the Content Aware Protection (CAP) tab was missing from two machines after upgrading from version 2.7.2.3 to 3.0.4.1006. They inquired whether this was an intentional change and attempted various methods to resolve the issue.

## Environment Details
- Upgraded from version 2.7.2.3 to 3.0.4.1006
- Upgrade methods used: Jamf upgrade and Upgrade job via EPP dashboard
- Client connection to the server was confirmed via timestamp
- Multiple device restarts were performed

## Troubleshooting Steps
1. Confirmed the absence of the CAP tab on the upgraded clients.
2. Verified that the clients were connected to the server.
3. Attempted to reinstall the client software.
4. Restarted the affected devices multiple times.
5. Scheduled a remote session to investigate further.

## Root Cause
The issue was identified as a result of the affected computers not being added to the appropriate policy that governs the visibility of the Content Aware Protection tab.

## Solution
During the remote session, the support engineer assisted the customer in verifying that the affected computers were added to the correct policy. Once this was done, the Content Aware Protection tab became visible on the clients. The customer confirmed the resolution and authorized the closure of the case.

## Notes
- Ensure that all clients are properly assigned to the necessary policies after upgrades to avoid similar issues in the future.
- It is advisable to verify policy assignments as part of the troubleshooting process when features are missing post-upgrade.