## Ticket Metadata
- **Ticket ID:** 500Qk00000CpiwCIAR
- **Case Number:** 414468
- **Status:** Closed - Resolved
- **Account/Company:** NovoEd
- **Contact Name:** Farnaz Ronaghi
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device Rights
- **Version:** Not specified

## Problem Description
The customer needed to disable removable media access only for a specific subset of devices, rather than globally across all devices. They were seeking guidance on how to implement this selective policy using Netwrix Endpoint Protector.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Feature in Use:** Device Control

## Troubleshooting Steps
1. The customer initially disabled removable media globally using the Global access settings.
2. The support technician provided instructions to create a specific group for the devices that should have access to removable media.
3. The customer was guided to edit the rights of the newly created group to allow access to storage devices.

## Root Cause
The issue arose from the customer's initial configuration, which applied a global setting to disable removable media across all devices. The need for a more granular control led to the request for assistance.

## Solution
The issue was resolved by following these steps:
1. Navigate to **Device Control -> Groups** in the Netwrix Endpoint Protector interface.
2. Create a new group that includes only the machines that should have access to removable devices.
3. Edit the rights for this group to allow access to storage devices.

This configuration allowed the customer to enforce the removable media policy selectively on the desired subset of laptops.

## Notes
- It is important for users to understand the difference between global settings and group-specific settings in Netwrix Endpoint Protector to avoid similar issues in the future.
- Users should regularly review group configurations to ensure that device control policies align with organizational needs.