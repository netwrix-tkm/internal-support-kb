```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000BpepvIAB
- **Case Number:** 411942
- **Status:** Closed - Resolved
- **Account/Company:** Mordor Intelligence Pvt. Ltd.
- **Contact Name:** Mohammad Azam
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Other
- **Version:** NONE

## Problem Description
The customer reported that a Gmail block policy had been applied, but Gmail was still accessible on some systems despite the policy being enabled.

## Environment Details
- The issue was observed on multiple systems within the customer's network.
- The customer confirmed that the deny list policies were enabled.

## Troubleshooting Steps
1. The customer opened the policy deny lists and enabled all deny list policies.
2. The customer confirmed that DPI (Data Protection Integration) was enabled on the affected systems.
3. The customer added `https://mail.google.com/*` to the deny list.
4. The support engineer requested the customer to ensure DPI was enabled and to check if the domain was correctly added to the deny list.
5. The support engineer requested log files to investigate further.
6. A remote connection was proposed to troubleshoot the issue directly.

## Root Cause
The issue was identified as a conflict caused by two computers having the same name, which prevented the block policy from being applied correctly.

## Solution
The resolution involved changing the name of one of the conflicting computers. After renaming, the URL was successfully blocked, and Gmail access was restricted as intended.

## Notes
- Ensure that all computers on the network have unique names to avoid conflicts with policy applications.
- Regularly verify that deny list policies are correctly configured and applied across all systems.
- Consider conducting periodic audits of the policy application status to ensure compliance.
```