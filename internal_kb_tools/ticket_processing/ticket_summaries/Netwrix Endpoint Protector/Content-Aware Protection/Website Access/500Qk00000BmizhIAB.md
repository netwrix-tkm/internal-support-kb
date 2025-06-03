## Ticket Metadata
- **Ticket ID:** 500Qk00000BmizhIAB
- **Case Number:** 411817
- **Status:** Closed - Resolved
- **Account/Company:** Xebia
- **Contact Name:** Srinivasa Rao Tumula
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** Website Access
- **Version:** 6.0

## Problem Description
The customer reported that an unwanted website was accessed, but no logs were found in the Content Awareness Protection (CAP) system to indicate this event.

## Environment Details
- The issue occurred within the Netwrix Endpoint Protector platform, specifically under the Content-Aware Protection feature.

## Troubleshooting Steps
1. Confirmed whether the URL was included in the URL denylist.
2. Verified if the URL was set in the CAP policy.
3. Checked if the Deep Packet Inspection (DPI) option was enabled.
4. Discussed the possibility of automatically adding categories (e.g., pornography) to the denylist.

## Root Cause
The root cause of the issue was identified as the absence of the specific URL in the denylist and the need for the denylist to be selected in the CAP policy. The DPI option was enabled, but without the URL or domain being explicitly added to the denylist, the system did not log the access attempt.

## Solution
To resolve the issue, it was advised to:
- Include the specific URL or domain in the URL or Deep Packet Inspection denylist.
- Ensure that this denylist is selected in the CAP policy to effectively block access and log any attempts to reach the unwanted website.

## Notes
- It is important to regularly review and update the denylist to include new unwanted categories or URLs to prevent similar issues in the future.
- Currently, there is no feature to automatically add entire categories to the denylist; URLs must be added individually.