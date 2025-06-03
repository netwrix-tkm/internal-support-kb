## Ticket Metadata
- **Ticket ID:** 500Qk00000KsbThIAJ
- **Case Number:** 432954
- **Status:** Closed - Resolved
- **Account/Company:** ZS
- **Contact Name:** Harshvardhan Mithapelli
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client/OS Performance
- **Version:** 5941

## Problem Description
The user reported that they were unable to access the website analytics.emburse.com, which had been accessible until the previous week. There were no block logs generated in the Content Aware Protection (CAP) portal, leading to confusion about the sudden blocking of the site by the Endpoint Protector (EPP).

## Environment Details
- The issue occurred in an environment using Netwrix Endpoint Protector.
- The user had other security applications running, including Zscaler, CrowdStrike, Carbon Black, and Global VPN.

## Troubleshooting Steps
1. Collected logs from the user to analyze the issue.
2. Confirmed that the website was accessible when EPP was disabled.
3. Suggested testing the EPP client with other security applications disabled to rule out conflicts.
4. Escalated the ticket to R&D for further investigation.
5. Whitelisted the domain analytics.emburse.com as a temporary fix.

## Root Cause
The root cause of the issue was not definitively identified, but it was suspected that the EPP was blocking the website due to its security policies, possibly in conflict with other security applications running in the environment.

## Solution
The issue was resolved by whitelisting the domain analytics.emburse.com in the EPP settings, which allowed the user to access the website without further interruptions. The customer confirmed that this solution worked and subsequently closed the ticket.

## Notes
- It is important to monitor for similar issues in the future, especially when multiple security applications are in use, as they may conflict with each other.
- Ensure that any changes to security policies or whitelists are documented to prevent similar issues from arising unexpectedly.
- Consider advising users to regularly check their EPP settings and logs for any changes that may affect website accessibility.