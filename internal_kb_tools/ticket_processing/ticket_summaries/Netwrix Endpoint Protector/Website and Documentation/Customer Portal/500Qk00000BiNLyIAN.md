## Ticket Metadata
- **Ticket ID:** 500Qk00000BiNLyIAN
- **Case Number:** 411636
- **Status:** Closed - Resolved
- **Account/Company:** Connecture Inc.
- **Contact Name:** Aaron Downend
- **Product:** Netwrix Endpoint Protector
- **Component:** Customer Portal
- **Feature:** Website and Documentation

## Problem Description
The customer reported that after increasing their disk space, they were unable to log into the Endpoint Protector (EPP) and had not been receiving any events.

## Environment Details
- The issue occurred after a disk space increase on the server side, specifically within the AWS environment (Production Connecture, Oregon - us-west-2).

## Troubleshooting Steps
1. Initial remote session was proposed to investigate the issue.
2. Suggested another remote session to review settings and make necessary changes.
3. Requested access to a computer with the EPP client installed for potential uninstallation and reinstallation.
4. Generated logs from the EPP client side during a remote session.
5. Discussed potential issues related to server certificates and client registration certificates.
6. Escalated the issue to the DevOps team for further investigation.

## Root Cause
The root cause was identified as an issue with the server certificate stack, which was likely disrupted during the disk space increase.

## Solution
The issue was resolved by regenerating the Server Certificate Stack, which restored the communication between the EPP clients and the server, allowing events to be received again.

## Notes
- It is important to monitor the system for at least a week after resolving similar issues to ensure that logs continue to be received without further interruptions.
- Future cases involving changes to server configurations or disk space should consider checking the server certificate stack as a potential troubleshooting step.