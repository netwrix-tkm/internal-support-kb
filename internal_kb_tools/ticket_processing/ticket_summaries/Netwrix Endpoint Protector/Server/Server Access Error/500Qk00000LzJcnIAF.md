## Ticket Metadata
- **Ticket ID:** 500Qk00000LzJcnIAF
- **Case Number:** 436085
- **Status:** Closed - Resolved
- **Account/Company:** CompasSolutions - @compassolutions.us
- **Contact Name:** Jose Alberto Ramirez Ramirez
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Access Error
- **Version:** Not specified

## Problem Description
The customer reported that they had changed the root user password a few days prior and could not remember it, resulting in a lack of access to the console.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Server

## Troubleshooting Steps
1. Confirmed that the root password had been changed and was not remembered by the customer.
2. Attempted to connect to the server to reset the password.
3. Identified issues with SSM (Systems Manager) access that needed to be addressed.
4. Planned to reach out to DevOps to resolve the SSM access issues.

## Root Cause
The issue was caused by the customer forgetting the newly set root password, which prevented access to the console.

## Solution
The issue was resolved by resetting the root password. After the password reset, access to the console was restored.

## Notes
- Ensure that customers are advised to securely store their passwords to prevent similar issues in the future.
- Monitor SSM access issues proactively to avoid delays in resolving access-related problems.