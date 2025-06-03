## Ticket Metadata
- **Ticket ID:** 500Qk00000NQkMvIAL
- **Case Number:** 440299
- **Status:** Closed - Resolved
- **Account/Company:** Zensoft Services
- **Contact Name:** Prasanth Ganesan
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** CAP Policies
- **Version:** None

## Problem Description
Messages sent in Microsoft Teams chat were being detected as HTML files, resulting in them being blocked by the Netwrix Endpoint Protector.

## Environment Details
- The customer was using Crowdstrike, which could not be disabled during troubleshooting.
- The issue affected both Teams replies and Outlook emails.

## Troubleshooting Steps
1. Collected logs for both email and Teams (Log.zip and log-1.zip).
2. Disabled Optical Character Recognition (OCR) settings, but the issue persisted.
3. Tested multiple Data Loss Prevention (DPI) settings, toggling DPI on and off for Teams.
4. Observed that some classic Outlook replies were blocked, while new emails were sent successfully.
5. Noted that one email was blocked due to a long subject line that resembled a Haskell string.
6. Confirmed that Teams replies were formatted as HTML, which triggered the EPP client to block them.

## Root Cause
1. **Outlook Blocked Email:** The email was blocked due to a long subject line that contained text resembling a Haskell string, which was flagged by the EPP.
2. **Teams Replies:** Teams replies were formatted as HTML, leading the EPP client to misinterpret them as HTML code, resulting in their blockage.

## Solution
- Recommended the customer remove HTML detection from the policy settings in the EPP, as most applications, including Teams, utilize HTML for communication. This change would reduce false positives and allow normal message exchanges.

## Notes
- It is crucial to review and adjust the EPP policies regarding HTML detection, especially for applications that frequently use HTML formatting for messages.
- Future troubleshooting should consider the implications of third-party security software (like Crowdstrike) that may interfere with the EPP's functionality.