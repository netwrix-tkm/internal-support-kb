## Ticket Metadata
- **Ticket ID:** 500Qk00000KahkUIAR
- **Case Number:** 432007
- **Status:** Closed - Resolved
- **Account/Company:** BMW Group AG
- **Contact Name:** Anatoli Lorenz
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Upgrade
- **Version:** 7.2.0

## Problem Description
The customer, BMW Group AG, requested manufacturer support to update their EPP PROD environment to version 7.2.0. They needed confirmation on the feasibility of the update and requested a meeting to discuss the process.

## Environment Details
- The update was to be applied to the EPP PROD environment accessible via the URL: [EPP PROD Environment](https://ygh5qe0.unify.endpointprotector.com/).
- The environment had previously encountered issues with patch 7.1.9, which failed in the UI but was applied successfully in the backend.

## Troubleshooting Steps
1. Confirmed the request for the update to version 7.2.0 and scheduled a meeting with the customer.
2. Attempted to apply patch 7.1.9, which failed in the UI.
3. Applied patch 7.2.0, which required manual actions for successful application.
4. Monitored server resources due to increased load from log ingestion after the patch was applied.
5. Conducted a backup of the environment prior to the upgrade meeting.
6. Investigated issues with log reports not loading after the update, including backend error logs.

## Root Cause
The initial failure of the patch 7.1.9 was attributed to UI issues, while the subsequent challenges with patch 7.2.0 were due to manual actions required for its application and increased server load from log ingestion. The high number of devices needing updates also contributed to the lengthy implementation time.

## Solution
The issue was resolved by:
- Successfully applying patch 7.2.0 after performing the necessary manual actions.
- Optimizing server resources to handle the increased load from log ingestion.
- Addressing the log report loading issues by performing backend operations that allowed logs to be displayed correctly.

## Notes
- It is crucial to prepare a backup before applying updates to avoid data loss.
- Future updates should consider the server load and the number of devices connected to minimize downtime.
- Ensure that all manual actions required for patch applications are documented and communicated to the team to prevent similar issues.