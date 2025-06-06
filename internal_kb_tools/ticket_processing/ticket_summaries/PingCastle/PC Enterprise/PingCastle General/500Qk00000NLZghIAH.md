## Ticket Metadata
- **Ticket ID:** 500Qk00000NLZghIAH
- **Case Number:** 440028
- **Status:** Closed - Resolved
- **Account/Company:** Würth IT GmbH
- **Contact Name:** Corvin Schmid
- **Product:** PingCastle
- **Component:** PC Enterprise
- **Feature:** PingCastle General
- **Version:** 3.3

## Problem Description
The customer reported an issue with the rule S-OldNtlm in PingCastle, which is designed to ban NTLMv1 and old LM protocols. The rule does not differentiate between sending NTLMv1 (Levels 0, 1, 2) and only accepting NTLMv1 (Levels 3 & 4). The customer expressed concern about the security risks associated with sending NTLMv1, particularly regarding potential MITM attacks and easy cracking.

## Environment Details
- **Platform:** PingCastle
- **Collector Code:** PC Enterprise
- **Age:** 5.1

## Troubleshooting Steps
1. The customer attempted to filter domains in the "Consolidation" dashboard to assess risk levels related to LAN Manager authentication.
2. The customer explored the possibility of creating action plans or similar actions but found this functionality unavailable.
3. The customer attempted to modify the S-OldNtlm rule but was unable to change its behavior.

## Root Cause
The root cause of the issue was identified as a limitation in the PingCastle tool, where the S-OldNtlm rule does not provide the necessary granularity to differentiate between sending and accepting NTLMv1. Additionally, there is currently no functionality to create action plans or modify the rule logic.

## Solution
The resolution involved informing the customer that the PingCastle team is considering adding action plans in future updates to unify views related to NTLMv1. However, there is no specific timeline for these updates. The team also noted that modifying the rule logic is not actively being pursued at this time but may be included in future plans.

## Notes
- The customer was advised to monitor future updates for enhancements related to the LMCompatibilityLevel LM & NTLM rules.
- It is important for users to be aware of the security implications of NTLMv1 and to consider alternative configurations to mitigate risks associated with its use.