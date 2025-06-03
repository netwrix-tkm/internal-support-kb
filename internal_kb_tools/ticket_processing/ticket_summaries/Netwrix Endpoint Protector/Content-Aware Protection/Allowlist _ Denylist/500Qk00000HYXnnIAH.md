# Support Case Summary

## Ticket Metadata
- **Ticket ID:** 500Qk00000HYXnnIAH
- **Case Number:** 425201
- **Status:** Closed - Resolved
- **Account/Company:** BelWo Services (India) Private Limited
- **Contact Name:** Abhishek Vishwakarma
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** Allowlist / Denylist
- **Version:** NONE

## Problem Description
The customer reported an issue where they were unable to block a specific URL using the content-aware protection feature of Netwrix Endpoint Protector.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Feature in Use:** Allowlist / Denylist

## Troubleshooting Steps
1. Verified the configuration settings for content-aware protection.
2. Reviewed the existing allowlist and denylist entries to ensure the URL was not mistakenly added to the allowlist.
3. Attempted to manually add the URL to the denylist but encountered errors.
4. Consulted documentation for any known issues related to URL blocking.

## Root Cause
The root cause of the issue was identified as a misconfiguration in the Deep Packet Inspection (DPI) settings, which prevented the denylist from functioning correctly.

## Solution
The issue was resolved by providing the customer with detailed steps on how to implement the DPI Denylist and enable Deep Packet Inspection. This involved:
- Accessing the Netwrix Endpoint Protector settings.
- Navigating to the DPI configuration section.
- Adding the desired URL to the denylist.
- Ensuring that Deep Packet Inspection was enabled to allow the denylist to take effect.

## Notes
- Ensure that Deep Packet Inspection is always enabled when using the denylist feature to avoid similar issues in the future.
- Regularly review and update the allowlist and denylist to maintain effective content-aware protection.