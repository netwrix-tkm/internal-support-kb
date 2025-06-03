## Ticket Metadata
- **Ticket ID:** 500Qk00000DEaAbIAL
- **Case Number:** 415365
- **Status:** Closed - Resolved
- **Account/Company:** Booking.com
- **Contact Name:** Serhat Demir
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** DPI - Other
- **Version:** 5941

## Problem Description
The customer reported an issue where they were unable to browse any websites using multiple browsers (Safari, Chrome, Firefox) when Deep Packet Inspection (DPI) was enabled. The network requests were not visible in the Developer Tools, and repeated errors were logged in the `eppsplit.log` file.

## Environment Details
- The issue was observed on endpoints running the Netwrix Endpoint Protector with DPI enabled.
- The error logs indicated problems with extracting original IP and port information.

## Troubleshooting Steps
1. Verified the issue by testing website access across multiple browsers (Safari, Chrome, Firefox).
2. Checked the Developer Tools' Network tab, which showed no requests being made.
3. Reviewed the `eppsplit.log` file for error messages, which indicated:
   - "Cannot extract the orig ip and port"
   - "Connection not found in NAT state table, aborting connection"
4. Disabled DPI for the agent, which resolved the browsing issue.
5. Provided a test build to the customer for further validation.

## Root Cause
The root cause of the issue was identified as a timing assumption in the SSLsplit communication with the network extension. The network extension was not always ready to provide the necessary port and connection information when requested, leading to unresponsive behavior and internet access issues.

## Solution
The issue was resolved by providing a fix in build version 5941 of the Netwrix Endpoint Protector. The fix eliminated the timing assumptions that caused the network extension to become unresponsive. The customer was advised to test the new build and confirm if the issue was addressed.

## Notes
- Customers experiencing similar issues should ensure they are using the latest version of the Netwrix Endpoint Protector.
- If issues persist after applying the fix, it is recommended to collect logs and escalate the case for further investigation.
- It is important to uninstall any previous versions of the EPP agent before installing test builds to avoid conflicts with the network extension.