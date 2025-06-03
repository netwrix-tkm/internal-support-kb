## Ticket Metadata
- **Ticket ID:** 500Qk00000OLwCrIAL
- **Case Number:** 442860
- **Status:** Closed - Resolved
- **Account/Company:** Satcom Infotech
- **Contact Name:** Thanushree Nagesh
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Client - Other
- **Feature:** Notifications
- **Version:** Server version 5.9.4.1 & client version 6.2.4.2

## Problem Description
The customer, Calpion, reported an issue with notifications that users were receiving from the Netwrix Endpoint Protector (EPP). Despite disabling notifications in the Content Aware Policy (CAP), users continued to receive notifications.

## Environment Details
- Deployment Mode: SaaS
- Server Version: 5.9.4.1
- Client Version: 6.2.4.2
- Issue Duration: Approximately 10 days prior to the support ticket creation.

## Troubleshooting Steps
1. The customer disabled client notifications in the CAP policy.
2. A remote session was scheduled to investigate the issue further.
3. During the remote session, the support team reviewed the notification settings and policies.

## Root Cause
The issue was identified as a caching/indexing problem within the EPP system, which caused the notifications to persist despite being disabled in the policy settings.

## Solution
The issue was resolved during the remote session by:
- Disabling the notifications directly from the policy settings.
- Ensuring that the changes were correctly applied and that the system was updated to reflect these changes.

## Notes
- It is important to verify that changes made in the CAP policy are correctly applied and reflected in the system to prevent similar issues in the future.
- Regular checks on caching and indexing processes may help in identifying potential issues before they affect users.