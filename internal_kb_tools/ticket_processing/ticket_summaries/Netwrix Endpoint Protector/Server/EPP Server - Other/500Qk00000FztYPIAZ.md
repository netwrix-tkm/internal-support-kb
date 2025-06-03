## Ticket Metadata
- **Ticket ID:** 500Qk00000FztYPIAZ
- **Case Number:** 421558
- **Status:** Closed - Resolved
- **Account/Company:** Stanford University
- **Contact Name:** Spencer Chinn
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** 5.9.4.0

## Problem Description
After updating to EPP version 5.9.4.0, the customer was unable to save changes to system settings due to an error indicating that the phone number in the "Main Administrator Contact Details" was not valid. The original format of the phone number was (650) 723-3333, which was rejected by the system.

## Environment Details
- **Previous Version:** 5.9.3.0
- **Updated Version:** 5.9.4.0
- **Next Patch Version:** 5.9.4.1

## Troubleshooting Steps
1. Verified the format of the phone number in the "Main Administrator Contact Details."
2. Attempted to save changes with the original phone number format (650) 723-3333.
3. Changed the phone number format to 6507233333 to see if it would allow saving.
4. Identified that the issue was related to a new validation rule introduced in version 5.9.4.0.
5. Confirmed with engineering that the issue would be addressed in the upcoming patch (5.9.4.1).

## Root Cause
The issue was caused by a new validation rule implemented in EPP version 5.9.4.0, which only accepted numeric input for the Administrator Phone Number. This change did not accommodate common phone number formats, such as (000) 000-0000, leading to the inability to save system settings.

## Solution
The issue was resolved by updating the EPP Server to version 5.9.4.1, which modified the phone number validator to accept the format (000) 000-0000. After the update, the customer was able to save changes to the system settings without encountering the error.

## Notes
- Ensure that any future updates to the phone number validation logic are communicated clearly to users to prevent similar issues.
- It is advisable to test any new validation rules in a staging environment before deployment to avoid disruptions in service.