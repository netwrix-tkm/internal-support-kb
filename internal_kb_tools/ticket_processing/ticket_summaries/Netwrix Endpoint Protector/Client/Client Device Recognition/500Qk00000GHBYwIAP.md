## Ticket Metadata
- **Ticket ID:** 500Qk00000GHBYwIAP
- **Case Number:** 422152
- **Status:** Closed - Resolved
- **Account/Company:** Bridgecom Semiconductors GmbH
- **Contact Name:** Amy Zhang
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Device Recognition
- **Version:** NONE

## Problem Description
The customer requested assistance with managing USB device read and write permissions for a specific group. They wanted to set all USB devices to be read-only by default, while allowing registered devices to have read and write access. Additionally, they sought clarification on the permission levels (1, 1+, 2) associated with the 'Allow Access if device is Trusted Device' setting.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Client

## Troubleshooting Steps
1. Reviewed the current configuration settings for USB device permissions.
2. Investigated the definitions and implications of the permission levels (1, 1+, 2) in the context of trusted devices.
3. Provided guidance on how to set specific devices to have read and write permissions while maintaining read-only access for others.

## Root Cause
The issue stemmed from a lack of clarity regarding the configuration settings for USB device permissions within the Netwrix Endpoint Protector. The customer needed specific instructions on how to implement their desired permission structure.

## Solution
The issue was resolved by guiding the customer to set up specific devices within the Netwrix Endpoint Protector configuration. This involved:
- Configuring the default setting for USB devices to be read-only.
- Allowing registered devices to have read and write permissions as per the customer's requirements.
- Clarifying the meaning of the permission levels (1, 1+, 2) and how they relate to trusted devices.

## Notes
- Ensure that users are aware of the implications of setting devices as trusted, as this can affect security policies.
- It may be beneficial to provide documentation or a reference guide that outlines the definitions and configurations for USB device permissions to prevent similar inquiries in the future.