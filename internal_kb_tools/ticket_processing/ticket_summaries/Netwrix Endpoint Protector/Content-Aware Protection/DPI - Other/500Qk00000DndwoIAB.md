```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000DndwoIAB
- **Case Number:** 416619
- **Status:** Closed - Resolved
- **Account/Company:** Booking.com
- **Contact Name:** Serhat Demir
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** DPI - Other
- **Version:** 5.9.4.1

## Problem Description
The user reported an "ERR_CONNECTION_RESET" error when attempting to access the website kayak.pl, while kayak.nl was accessible. This issue occurred in both Chrome and Edge browsers.

## Environment Details
- The issue was related to the Netwrix Endpoint Protector (EPP) software, specifically its Deep Packet Inspection (DPI) feature.
- The user experienced synchronization issues with Zoom Workspace during the same timeframe.

## Troubleshooting Steps
1. Verified access to kayak.nl, which was successful.
2. Attempted to access kayak.pl, which resulted in the "ERR_CONNECTION_RESET" error.
3. Restarted the Endpoint Protector (EPP) service, which did not resolve the issue.
4. Unloaded the agent service using Windows tools, which allowed successful access to kayak.pl.
5. Restarted the agent service after loading the page, and it continued to work.

## Root Cause
The "ERR_CONNECTION_RESET" error was caused by the EPP's DPI feature, which dropped the connection due to a certificate validation error. This was linked to a recent update of the certificate for kayak.pl, which had briefly expired.

## Solution
The issue was resolved by providing a test build of the EPP software (version 5.9.4.1) to the customer. This version included fixes for the ERR_CONNECTION_RESET error and related issues. The customer confirmed that the problem was addressed after testing the new build.

## Notes
- Users should avoid using the "Ignore Trust" option in the Peer Certificate Validation settings, as it decreases security.
- If users encounter similar issues with websites presenting certificate errors, they can enable the "Bypass Invalid Peer Certificates" option under DPI Bypass to allow access while still receiving reports on bypassed websites.
- It is important to monitor for any recurrence of the issue and to collect logs without workarounds if the problem persists.
```