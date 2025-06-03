## Ticket Metadata
- **Ticket ID:** 500Qk00000DubtVIAR
- **Case Number:** 416904
- **Status:** Closed - Resolved
- **Account/Company:** CoreWin Distributor
- **Contact Name:** Danylo Didenko
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** CAP Exitpoints / Applications
- **Version:** 10.2

## Problem Description
The customer, Privat Bank, reported unexpected behavior regarding the "Network Share" setting within the CAP policy of Netwrix Endpoint Protector. Although "Network Share" was disabled, logs indicated that a transfer was occurring via "Total Commander," which was selected as an exit point. The customer sought clarification on whether this behavior was expected.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Content-Aware Protection

## Troubleshooting Steps
1. Reviewed the CAP policy settings to confirm the status of "Network Share" and "Total Commander."
2. Analyzed the logs in the Logs Reports to identify any network share transfer activities.
3. Investigated the behavior of the Endpoint Protector in relation to exit points and network share operations.

## Root Cause
The root cause was identified as the Endpoint Protector's default behavior of recognizing file transfers initiated through "Total Commander" as network share operations, even when the "Network Share" option was disabled in the CAP policy.

## Solution
The issue was resolved by providing clarification on the Content Aware Report, confirming that the behavior observed was indeed expected due to the way the Endpoint Protector interprets file transfers through certain applications like "Total Commander."

## Notes
- It is important to inform customers that certain applications may be treated as network share operations by default, regardless of specific policy settings.
- Future inquiries regarding similar behavior should include a review of application-specific settings and their interactions with the CAP policy.