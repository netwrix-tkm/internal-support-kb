## Ticket Metadata
- **Ticket ID:** 500Qk00000OcHObIAN
- **Case Number:** 443623
- **Status:** Closed - Resolved
- **Account/Company:** CMS Distribution
- **Contact Name:** Eoin McAllister
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Server - Other
- **Feature:** EPP Server - Other
- **Version:** Not specified

## Problem Description
The customer reported that they were unable to log in to the Netwrix Endpoint Protector (EPP) due to password issues. After being prompted to change the password, both the new and old passwords failed to grant access.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Server

## Troubleshooting Steps
1. Initial inquiry sent to the customer to gather more details about the issue, including any error messages received and whether they were the only administrator on the EPP UI.
2. Customer responded indicating that after changing the password, neither the new nor the old password worked for logging in.
3. A remote session was proposed to reset the password.
4. The remote session was scheduled for a time convenient for the customer.

## Root Cause
The issue was caused by a failure in the password change process, which resulted in both the old and new passwords being invalidated, preventing access to the EPP.

## Solution
During the scheduled remote session, the support engineer successfully reset the password for the customer. After the reset, the customer was able to log in without further issues.

## Notes
- Ensure that users are aware of the password change process and confirm that the new password meets any specified criteria.
- It may be beneficial to implement a confirmation step after a password change to verify that the new password is functioning correctly before logging out.