## Ticket Metadata
- **Ticket ID:** 500Qk00000HfBvPIAV
- **Case Number:** 425502
- **Status:** Closed - Resolved
- **Account/Company:** ING companies
- **Contact Name:** Marco Vinicius Aguemi Cabral
- **Product:** Netwrix Endpoint Protector
- **Component:** Active Directory Sync
- **Feature:** AD Sync - Other
- **Version:** Not specified

## Problem Description
The customer reported an issue where users were unable to authenticate into the Netwrix Appliance using Active Directory (AD) accounts. Although the AD sync and test functions worked correctly, attempts to log in with AD accounts resulted in a message indicating that the password was expired, despite the customer confirming that this was not the case.

## Environment Details
- The issue occurred within the Netwrix Endpoint Protector environment.
- The customer was using Active Directory for authentication.

## Troubleshooting Steps
1. Verified that the AD sync and test functions were operational.
2. Checked the password status of the AD accounts to confirm they were not expired.
3. Reviewed the password policy settings to identify any enforced changes.
4. Attempted to log in with various AD accounts to replicate the issue.

## Root Cause
The root cause of the issue was identified as an enforced password policy within the Netwrix Appliance settings that required all users to change their passwords, even when they were not expired. This policy was inadvertently applied, leading to the authentication failures.

## Solution
The issue was resolved by disabling the enforced password change requirement in the appliance settings. Once this setting was reverted, users were able to log in successfully with their existing passwords without being prompted to change them.

## Notes
- It is important to monitor password policy settings when integrating with Active Directory to avoid unexpected authentication issues.
- Future feature requests regarding password policies can be submitted through a new support ticket, specifying the desired changes and details.