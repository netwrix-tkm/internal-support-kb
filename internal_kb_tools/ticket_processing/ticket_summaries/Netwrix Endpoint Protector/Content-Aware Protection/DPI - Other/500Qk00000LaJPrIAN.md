## Ticket Metadata
- **Ticket ID:** 500Qk00000LaJPrIAN
- **Case Number:** 435019
- **Status:** Closed - Resolved
- **Account/Company:** Halodata International Pte Ltd
- **Contact Name:** Halodata Support Tech
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** DPI - Other
- **Version:** NONE

## Problem Description
The customer reported an event in the Content Aware Report indicating a DPI Bypassed Traffic event with the destination set to Chrome and the Destination Type labeled as BypassApp. The customer inquired whether this was due to the DPI Auto-refresh Certificate feature being set manually instead of automatically.

## Environment Details
- The issue was observed in the Netwrix Endpoint Protector platform.
- The specific feature involved was DPI (Deep Packet Inspection) related to content-aware protection.

## Troubleshooting Steps
1. Reviewed the Content Aware Report to confirm the DPI Bypassed Traffic event.
2. Investigated the configuration settings for the DPI Auto-refresh Certificate feature to determine if it was set manually.
3. Analyzed the logs to identify any patterns or additional events related to the bypassed traffic.
4. Provided explanations regarding the implications of manual versus automatic settings for the DPI Auto-refresh Certificate.

## Root Cause
The DPI Bypassed Traffic event occurred because the DPI Auto-refresh Certificate feature was indeed set manually. This configuration can lead to scenarios where certain applications, like Chrome, bypass the DPI filtering, resulting in the event being logged.

## Solution
The issue was resolved by providing the customer with detailed information regarding the DPI Bypassed Traffic event. It was explained that setting the DPI Auto-refresh Certificate feature to automatic would help prevent such bypass events in the future. The customer was advised to adjust their settings accordingly to ensure proper DPI functionality.

## Notes
- It is important to monitor the configuration of the DPI Auto-refresh Certificate feature to avoid unintended bypasses in traffic inspection.
- Customers should be informed about the implications of manual settings on DPI functionality to prevent similar issues from arising in the future.