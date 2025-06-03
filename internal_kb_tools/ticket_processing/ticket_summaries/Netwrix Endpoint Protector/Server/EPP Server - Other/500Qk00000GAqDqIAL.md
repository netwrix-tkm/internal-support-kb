```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000GAqDqIAL
- **Case Number:** 421905
- **Status:** Closed - Resolved
- **Account/Company:** Satcom Infotech
- **Contact Name:** Prasanth Ganesan
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Server - Other
- **Feature:** DPI (Deep Packet Inspection)
- **Version:** Not specified

## Problem Description
During a proof of concept (POC) for a client, multiple issues were reported related to the Netwrix Endpoint Protector (EPP) system, specifically when the Deep Packet Inspection (DPI) feature was enabled. The issues included:
1. Internet slowness.
2. Inability to assign technicians in the customer’s helpdesk tool.
3. Network failure errors when accessing AWS accounts.
4. Problems with email filtering for specific domains.

## Environment Details
- The issues were encountered in a client environment utilizing Netwrix Endpoint Protector with the DPI feature enabled.

## Troubleshooting Steps
1. The customer reported the issues to Netwrix support, providing logs and screenshots for further investigation.
2. The support team communicated with the engineering team to analyze the reported problems.
3. A test build of the EPP client was provided to the customer for installation and verification.
4. The customer was advised to use webmail as a workaround for Outlook email access issues.

## Root Cause
The root cause of the issues was identified as the DPI feature's impact on network performance and its inability to distinguish between embedded images and email signatures, which affected email filtering functionality.

## Solution
The issue was resolved by:
- Providing a test build of the EPP client (version 6.2.4.0024) to the customer for installation on a test machine.
- Advising the customer to use webmail for Outlook users as a temporary workaround until a permanent fix could be implemented.

## Notes
- The engineering team is still investigating the limitations of the DPI feature regarding email signature and embedded attachment scanning.
- It is important to monitor the performance of the DPI feature in future implementations to avoid similar issues.
- Ensure that trial licenses are managed effectively to prevent interruptions during testing phases.
```