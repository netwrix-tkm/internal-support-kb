## Ticket Metadata
- **Ticket ID:** 500Qk00000HwTchIAF
- **Case Number:** 426155
- **Status:** Closed - Resolved
- **Account/Company:** wotton & kearney
- **Contact Name:** Mani Bhagavathula
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device Rights
- **Version:** NONE

## Problem Description
The client reported that users were unable to view existing data on USB drives when using devices with the Netwrix Endpoint Protector (EPP) installed. This issue arose after the client gained full access to the EPP Portal, despite the functionality working in their testing instance.

## Environment Details
- The issue was observed on Windows machines with EPP installed.
- The USB drives were previously used on personal laptops and contained both personal and work-related documents.

## Troubleshooting Steps
1. Enabled the “Allow Access if Trusted Device Level 1+” setting in EPP.
2. Tested USB access by:
   - Copying data onto the USB using a personal laptop.
   - Plugging the USB into a work computer where Easy Lock launched and the drive was password protected.
   - Attempting to access pre-existing personal documents on the USB via File Explorer on the work computer.
   - Testing the USB on a personal desktop computer to confirm access to unencrypted files.

## Root Cause
The root cause of the issue was identified as the behavior of the "Allow Access if Trusted Device Level 1+" setting, which is designed to restrict access to USB devices unless they are accessed through the EasyLock application. This setting prevents users from viewing pre-existing files on the USB drive when connected to a work computer.

## Solution
To resolve the issue, the following steps were taken:
- The right for USB devices was adjusted to allow access, enabling users to view existing files on the USB drive.
- It was recommended to set the right as "Allow Access if Trusted Device Level 1+, otherwise Read Only" or "Read Only" to balance security and accessibility.

## Notes
- Users must encrypt any new data written to the USB using EasyLock to maintain compliance with security policies.
- Future configurations should consider the balance between user access and security settings to avoid similar issues.