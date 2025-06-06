```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000NaeeQIAR
- **Case Number:** 440679
- **Status:** Closed - Resolved
- **Account/Company:** The Coding Network
- **Contact Name:** Kristen Sherrill
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Performance
- **Version:** Not specified

## Problem Description
The customer reported that after migrating their server to AWS, they experienced intermittent unavailability of the server, indicated by a "504 Gateway Time-Out" error occurring approximately once every seven days. Rebooting the server temporarily resolved the issue, but performance remained poor, with significant delays in response times.

## Environment Details
- The server was migrated to AWS.
- The server was running with insufficient resources for the number of clients connected.

## Troubleshooting Steps
1. Scheduled a remote session to investigate the issue.
2. Suggested allowing SSH access on port 62828 for the EPP Server in AWS.
3. Confirmed that the server was under-resourced for the number of EPP Clients.
4. Increased the server resources during the remote session.
5. Optimized the server resources based on the findings.

## Root Cause
The root cause of the issue was identified as the server being provisioned with less than the minimum required resources for the Netwrix Endpoint Protector (EPP) Server, leading to performance degradation and intermittent unavailability.

## Solution
The issue was resolved by increasing the server resources to meet the minimum requirements for the EPP Server. The resources were optimized during a remote session, which improved server performance and stability.

## Notes
- Ensure that server resources are adequately provisioned based on the number of clients using the EPP Client to prevent similar issues in the future.
- Monitor server performance regularly after migration to cloud environments to identify and address resource limitations proactively.
```