## Ticket Metadata
- **Ticket ID:** 500Qk00000JPrXgIAL
- **Case Number:** 429671
- **Status:** Closed - Resolved
- **Account/Company:** Tusas Engine Industries
- **Contact Name:** Onur CAN
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device Rights
- **Version:** 4.1

## Problem Description
The customer reported unexpected behavior where, after a device was authorized through a user, other users were able to use the same device on the same computer. This occurred despite the device rights being set to "full" on the computer.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Age of the Issue:** 4.1

## Troubleshooting Steps
1. Reviewed the device authorization settings for users and computers.
2. Checked the configuration of device rights assigned to users and computers.
3. Attempted to replicate the issue by authorizing devices through different users.
4. Analyzed logs for any discrepancies or errors related to device rights.

## Root Cause
The issue was identified as a misconfiguration in the device rights prioritization. The rights were set to prioritize the computer over the user, which allowed multiple users to access the same device.

## Solution
The resolution involved changing the rights prioritization from "Computer" to "User." This adjustment ensured that device access was restricted to the user who authorized the device, preventing other users from using the same device on the same computer.

## Notes
- Ensure that device rights are correctly prioritized based on organizational policies to avoid similar issues in the future.
- Regularly review and audit device authorization settings to maintain compliance and security.