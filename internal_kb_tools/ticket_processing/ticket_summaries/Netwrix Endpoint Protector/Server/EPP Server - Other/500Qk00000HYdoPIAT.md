## Ticket Metadata
- **Ticket ID:** 500Qk00000HYdoPIAT
- **Case Number:** 425212
- **Status:** Closed - Resolved
- **Account/Company:** PrivatBank
- **Contact Name:** Danylo Didenko
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** Not specified

## Problem Description
The customer, PrivatBank, reported that the EPP server time was displaying GMT+3 instead of the updated GMT+2 time zone following a recent change in Ukraine's time zone. The server time was one hour ahead of the actual time, causing discrepancies in time-sensitive operations.

## Environment Details
- **Server Type:** EPP Server
- **Location:** Ukraine
- **Time Zone Change:** From GMT+3 to GMT+2

## Troubleshooting Steps
1. Reviewed the server's current time settings.
2. Confirmed the time zone change in Ukraine.
3. Scheduled a remote session to address the time discrepancy.
4. Attempted to adjust the server time settings during the remote session.

## Root Cause
The root cause of the issue was the recent change in Ukraine's time zone from GMT+3 to GMT+2, which was not reflected in the EPP server settings.

## Solution
The issue was resolved by adjusting the server time settings to reflect the new GMT+2 time zone. This adjustment was performed during a scheduled remote session with the customer.

## Notes
- Ensure that time zone changes in regions where servers are located are promptly updated in server settings to avoid similar issues in the future.
- It is advisable to monitor server time settings regularly, especially after any regional time zone changes.