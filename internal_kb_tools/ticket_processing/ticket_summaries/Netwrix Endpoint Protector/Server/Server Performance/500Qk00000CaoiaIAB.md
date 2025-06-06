```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000CaoiaIAB
- **Case Number:** 413849
- **Status:** Closed - Resolved
- **Account/Company:** Nixon Peabody LLP
- **Contact Name:** Danielle Rochford
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Performance
- **Version:** 5.8.1.0 (EPP server), Clients Windows v5.8.3.7 and v5.9.2.8

## Problem Description
After applying the hotfix for ADV-2024-002, the customer reported that logs from endpoints ceased to be received, with only "Policy Received" logs appearing. Content-aware report logs stopped immediately after the hotfix was applied.

## Environment Details
- EPP server version: 5.8.1.0
- Hosting: On-premises
- Hotfix applied: Offline Patch
- Client versions: Windows v5.8.3.7 and v5.9.2.8

## Troubleshooting Steps
1. Confirmed the issue with the customer and gathered environment details.
2. Informed the customer that Netwrix had received similar reports regarding the hotfix affecting log processing.
3. Temporarily paused distribution of the hotfix until a replacement was available.
4. Requested additional information from the customer regarding server and client versions.
5. Scheduled a remote session to apply a new hotfix if necessary.

## Root Cause
The issue was identified as a known problem with CoSoSys Endpoint Protector Hotfix #1, which caused the system to stop processing certain events after deployment.

## Solution
- A revised hotfix was deployed, which resolved the issue of missing logs.
- The customer successfully applied the updated hotfix to their test server, confirming that logs were being received as expected.
- The customer then applied the hotfix to their production server, restoring normal log processing.

## Notes
- It is important to monitor the deployment of hotfixes and be aware of any known issues that may arise.
- Customers should be advised to test hotfixes in a controlled environment before applying them to production systems.
- Ensure that communication regarding hotfix issues is clear and timely to prevent prolonged disruptions in service.
```