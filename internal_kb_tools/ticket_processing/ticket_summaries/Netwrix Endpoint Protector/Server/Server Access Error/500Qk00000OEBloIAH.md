## Ticket Metadata
- **Ticket ID:** 500Qk00000OEBloIAH
- **Case Number:** 442560
- **Status:** Closed - Resolved
- **Account/Company:** PeopleStrong
- **Contact Name:** Rohit Nawani
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Access Error
- **Version:** NONE

## Problem Description
All administrators were unable to access the Netwrix Endpoint Protector (EPP) portal after entering the Multi-Factor Authentication (MFA) credentials, receiving an error indicating incorrect MFA.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Issue Type:** Insufficient hardware resources

## Troubleshooting Steps
1. The support team requested remote availability from the customer to further investigate the issue.
2. The support team inquired if a user without MFA could log in to check the server time from the Appliance > Server Maintenance section.
3. The case was identified as a duplicate of a previously resolved ticket (00444722).

## Root Cause
The issue was determined to be related to insufficient hardware resources, which affected the MFA functionality and overall access to the EPP portal.

## Solution
The problem was resolved by addressing the insufficient hardware resources, which allowed the MFA process to function correctly, enabling administrators to access the EPP portal successfully.

## Notes
- Ensure that hardware resources are adequately provisioned to support MFA and other functionalities of the Netwrix Endpoint Protector.
- Monitor for similar issues in the future, particularly in environments with limited hardware resources, as they may lead to access problems.