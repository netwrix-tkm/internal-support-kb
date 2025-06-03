## Ticket Metadata
- **Ticket ID:** 500Qk00000MGvaPIAT
- **Case Number:** 436868
- **Status:** Closed - Resolved
- **Account/Company:** Government (Malta)
- **Contact Name:** Identita Malta
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** NONE

## Problem Description
The customer reported that the admin password could not be changed after it had expired, and the current password was not recognized during the password change process.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Server

## Troubleshooting Steps
1. Verified the status of the admin password and its expiration.
2. Attempted to change the password using the current password, which was not recognized.
3. Reviewed system logs for any errors related to password management.

## Root Cause
The issue was caused by the system not recognizing the current password, which prevented the password change process from completing successfully.

## Solution
The issue was resolved by resetting the admin password to the default password. This allowed the customer to regain access and change the password as needed.

## Notes
- Ensure that the password reset process is documented and communicated to users to avoid confusion in the future.
- It is advisable to check for any system updates or patches that may address similar password management issues.