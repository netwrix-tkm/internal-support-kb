## Ticket Metadata
- **Ticket ID:** 500Qk00000GXffuIAD
- **Case Number:** 422694
- **Status:** Closed - Resolved
- **Account/Company:** CoreWin Distributor
- **Contact Name:** Danylo Didenko
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** Not specified

## Problem Description
The customer, PrivatBank, reported that the time on their EPP test server was incorrect and out of sync. This discrepancy prevented them from logging in due to issues with two-factor authentication.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Server Type:** EPP test server

## Troubleshooting Steps
1. Customer requested a remote session to synchronize the server time.
2. Support technician accessed the server's backend to check the current time settings.
3. Verified the time zone configuration on the server.
4. Adjusted the server time to match the correct time.

## Root Cause
The root cause of the issue was identified as an incorrect time setting on the EPP test server, which was not synchronized with the actual time, leading to failures in two-factor authentication.

## Solution
The issue was resolved by modifying the time settings on the server's backend to ensure it was synchronized with the correct time. This adjustment allowed the customer to successfully log in using two-factor authentication.

## Notes
- Ensure that server time is regularly synchronized with a reliable time source to prevent similar issues in the future.
- Consider implementing monitoring for time discrepancies on critical servers to proactively address potential authentication issues.