```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000MATYkIAP
- **Case Number:** 436653
- **Status:** Closed - Resolved
- **Account/Company:** Canada Guaranty
- **Contact Name:** Parinkumar Patel
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** EPP Client - Other
- **Version:** Not specified

## Problem Description
The customer reported that the EPP agent creates an outbound block rule for the QUIC protocol in the local Windows Firewall on endpoints. They requested clarification on the necessity of this rule and whether it could be disabled.

## Environment Details
- The issue was observed on endpoints running Windows with the Netwrix Endpoint Protector EPP client installed.

## Troubleshooting Steps
1. The customer inquired about the purpose of the outbound block rule created by the EPP client.
2. Technical support checked internal documentation and confirmed the existence of a block rule for the QUIC protocol.
3. An internal discussion was initiated to seek confirmation from engineering regarding the necessity of the rule.
4. The support team communicated with the customer regarding the status of their inquiry and the potential impact of removing the rule.

## Root Cause
The EPP client cannot monitor the QUIC protocol, which necessitates the creation of the outbound block rule to prevent potential security issues. This rule is particularly relevant for less common browsers that may utilize QUIC.

## Solution
The official response confirmed that the outbound block rule for QUIC is not essential for the operation of mainstream browsers (like Chrome and Edge) since QUIC can be disabled through settings. The customer was advised that they could safely disable this firewall rule without impacting their day-to-day operations.

## Notes
- It is important to inform customers that while the rule is not necessary for mainstream browsers, it may be relevant for less common browsers that utilize the QUIC protocol.
- Future inquiries regarding similar firewall rules should be directed to engineering for confirmation on necessity and potential impacts of removal.
```