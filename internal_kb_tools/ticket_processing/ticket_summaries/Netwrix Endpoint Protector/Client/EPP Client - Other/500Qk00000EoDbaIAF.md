```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000EoDbaIAF
- **Case Number:** 418922
- **Status:** Closed - Resolved
- **Account/Company:** Arista Networks, Inc.
- **Contact Name:** Bharani M
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Client - Other
- **Feature:** Serial Number Lookup
- **Version:** Not specified

## Problem Description
The customer reported a recurring issue with the serial number lookup functionality in the Netwrix Endpoint Protector. Each time a machine was looked up by its serial number, the host associated with that serial number would change unexpectedly.

## Environment Details
- The issue was reported in a multi-user environment where multiple machines were being monitored.
- Specific mention of a new Mac setup that experienced the same issue.

## Troubleshooting Steps
1. Customer was asked to upload a file to the backend of their EPP server.
2. A remote session was scheduled to further investigate the issue.
3. The support team raised the issue with the development team for further analysis.
4. The customer was instructed to generate logs on computers that swapped serial numbers.
5. Additional logs were to be generated on the EPP server, and devices were to be re-registered.
6. The customer was provided with a SQL file (`connectedProcedure.sql`) to upload to the EPP server for further diagnostics.

## Root Cause
The root cause of the issue was not definitively identified during the troubleshooting process. The problem appeared to be related to how the EPP server managed serial number associations with user accounts, particularly in environments with multiple users and machines.

## Solution
The issue was ultimately resolved when the customer could not replicate the problem after following the troubleshooting steps. The support team advised closing the ticket as the issue seemed to have resolved itself.

## Notes
- It is important for users to ensure that they can replicate the issue consistently before escalating to support.
- Future cases should consider checking for any updates or patches to the EPP software that may address similar issues with serial number management.
- Customers should be prepared to provide logs and other diagnostic information to expedite troubleshooting.
```