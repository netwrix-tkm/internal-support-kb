## Ticket Metadata
- **Ticket ID:** 500Qk00000HBuMwIAL
- **Case Number:** 424357
- **Status:** Closed - Resolved
- **Account/Company:** RoundRobin - Reseller
- **Contact Name:** Nayan Rajore
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Access Error
- **Version:** NONE

## Problem Description
The customer reported an inability to log into their on-premises EPP (Endpoint Protector) server. Despite using the same password that had previously worked, access to the portal was suddenly denied without any changes to the configuration.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Server

## Troubleshooting Steps
1. Verified the login credentials to ensure they were correct.
2. Checked for any recent changes in the server configuration or network settings.
3. Attempted to reset the password through standard procedures, but access remained denied.

## Root Cause
The root cause of the login issue was identified as a problem with the root password, which had become invalid or corrupted, preventing successful authentication.

## Solution
The issue was resolved by resetting the root password for the EPP server. After the password reset, the customer was able to log in successfully to the web console.

## Notes
- It is advisable to document any password changes and ensure that backup credentials are available to prevent similar access issues in the future.
- Regularly check for updates or patches for the Netwrix Endpoint Protector to avoid potential security or access issues.