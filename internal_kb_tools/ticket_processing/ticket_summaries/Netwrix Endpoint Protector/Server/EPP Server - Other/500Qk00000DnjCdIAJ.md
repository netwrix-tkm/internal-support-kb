## Ticket Metadata
- **Ticket ID:** 500Qk00000DnjCdIAJ
- **Case Number:** 416631
- **Status:** Closed - Resolved
- **Account/Company:** Halodata International Pte Ltd
- **Contact Name:** Halodata Support Tech
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** NONE

## Problem Description
The customer, Trusting Social, reported that after purchasing an additional 100 licenses, their server was only displaying a total of 100 licenses instead of the expected 150 licenses.

## Environment Details
- **Customer Name:** Trusting Social (VN)
- **Previous License Count:** 50 licenses
- **New License Count:** 100 licenses purchased
- **Total Expected Licenses:** 150 licenses
- **Displayed Licenses on Server:** 100 licenses

## Troubleshooting Steps
1. Verified the total number of licenses purchased by the customer.
2. Checked the licensing page on the server for discrepancies.
3. Reviewed the server ID provided in the screenshot for any potential issues.
4. Confirmed that the license activation process was completed correctly.

## Root Cause
The issue was identified as a failure in the license synchronization process on the server, which did not reflect the newly purchased licenses.

## Solution
The issue was resolved by manually triggering a license synchronization on the server. This action updated the license count to reflect the total of 150 licenses as expected.

## Notes
- Ensure that the license synchronization process is monitored after any license purchase to prevent similar issues in the future.
- It may be beneficial to implement a notification system for customers to confirm successful license updates post-purchase.