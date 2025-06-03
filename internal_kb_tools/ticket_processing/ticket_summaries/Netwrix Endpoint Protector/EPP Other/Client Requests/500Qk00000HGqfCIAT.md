## Ticket Metadata
- **Ticket ID:** 500Qk00000HGqfCIAT
- **Case Number:** 424480
- **Status:** Closed - Resolved
- **Account/Company:** axio / CapFloat Financial Services Private Limited
- **Contact Name:** Andrei Pop
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Client Requests
- **Version:** NONE

## Problem Description
The customer reported an issue where they were unable to create a new policy in the Netwrix Endpoint Protector, receiving an error when attempting to exceed the existing limit of 48 policies.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** EPP Other

## Troubleshooting Steps
1. Verified the current policy limit set within the Netwrix Endpoint Protector.
2. Attempted to create a new policy to replicate the error.
3. Reviewed system logs for any error messages related to policy creation.
4. Confirmed with the customer the exact error message received during the policy creation attempt.

## Root Cause
The issue was caused by a limitation in the number of policies that could be created, which was set to a maximum of 48.

## Solution
The limit for the number of policies was increased from 48 to 80, allowing the customer to successfully create new policies without encountering errors.

## Notes
- Ensure to monitor policy limits for customers who may require the creation of multiple policies.
- Consider documenting the process for increasing policy limits for future reference to expedite similar requests.