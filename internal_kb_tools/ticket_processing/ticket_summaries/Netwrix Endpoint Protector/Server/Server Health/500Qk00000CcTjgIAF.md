## Ticket Metadata
- **Ticket ID:** 500Qk00000CcTjgIAF
- **Case Number:** 413921
- **Status:** Closed - Resolved
- **Account/Company:** Arista Networks, Inc.
- **Contact Name:** Ian OBrien
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Health
- **Version:** 1.1 (vulnerability patch)

## Problem Description
The customer reported that after running a live update on their server, it stopped logging any Data Loss Prevention (DLP) activity from clients. This issue arose immediately following the update performed by their administrator.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Server Age:** 5.3 years

## Troubleshooting Steps
1. Initial communication established with the customer to acknowledge the issue.
2. Engineers investigated the problem and confirmed it was related to the vulnerability patch.
3. A manual workaround was discussed and scheduled for implementation.
4. A Zoom meeting was set up to apply the manual fix.
5. Follow-up checks were conducted to verify if logs were being generated post-fix.

## Root Cause
The issue was identified as a result of the vulnerability patch (version 1.1) applied during the live update, which caused the server to stop logging DLP activities.

## Solution
The issue was resolved by applying a manual workaround for the vulnerability patch. After the fix was implemented, the server began logging DLP activities again, confirming that it was functioning as expected.

## Notes
- Ensure to monitor the effects of any vulnerability patches before applying them in a production environment.
- It is advisable to have a rollback plan or manual workaround ready when deploying updates that may affect critical logging functionalities.