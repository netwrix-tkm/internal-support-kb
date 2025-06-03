## Ticket Metadata
- **Ticket ID:** 500Qk00000GBhlBIAT
- **Case Number:** 421940
- **Status:** Closed - Resolved
- **Account/Company:** ING companies
- **Contact Name:** Drake Scott
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device Rights
- **Version:** 2.0

## Problem Description
The customer inquired about how device rights priorities interact when a user is part of multiple groups. Specifically, they wanted to know whether a higher group priority number takes precedence over a lower number or vice versa.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Device Control

## Troubleshooting Steps
1. Reviewed the device rights group priority settings in the Netwrix Endpoint Protector.
2. Consulted the product documentation regarding group priority interactions.
3. Engaged with internal technical resources to clarify the behavior of group priorities.
4. Conducted tests by assigning users to multiple groups with varying priority levels to observe the resulting access behavior.

## Root Cause
The confusion stemmed from a misunderstanding of how group priority numbers are interpreted within the Netwrix Endpoint Protector. The documentation was not clear on whether a higher number or a lower number indicated higher precedence.

## Solution
The issue was resolved by clarifying that in the Netwrix Endpoint Protector, a **lower group priority number** indicates higher precedence. This means that if a user is part of multiple groups, the group with the lowest priority number will dictate the device rights for that user.

## Notes
- It is important for users to understand the priority system when configuring device rights to avoid access issues.
- Future documentation updates may be necessary to enhance clarity regarding group priority interactions.
- Support staff should be prepared to explain this priority system to customers to prevent similar inquiries.