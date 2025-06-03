## Ticket Metadata
- **Ticket ID:** 500Qk00000NLFreIAH
- **Case Number:** 439990
- **Status:** Closed - Resolved
- **Account/Company:** PrivatBank
- **Contact Name:** CoreWin Tech
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Custom Classes
- **Version:** 5.9.4.1

## Problem Description
The customer, PrivatBank, reported an issue while attempting to add a bulk list of 1100 USB flash drives to the Allowed Specific Devices. When using the Bulk enrollment .xls file from the EPP console to add a test batch of 9 USB devices, the Device Wizard incorrectly assigned the VID and PID numbers, replacing them with "Genera". However, when the same devices were added manually via text input, they were added correctly.

## Environment Details
- The customer is using EPP version 5.9.4.1.
- The server experienced high resource usage, particularly with MySQL, which was consuming significant CPU resources due to incoming logs and shadows.

## Troubleshooting Steps
1. Attempted to recreate the issue in the support environment using the Specific Devices in Device Control.
2. Verified that the XLS file provided by the customer was invalid when uploaded to the server.
3. Downloaded a fresh sample XLS file, copied the details from the customer's file, and successfully uploaded it, which generated the correct VID and PID.
4. Investigated the server's high resource usage and identified that MySQL was the primary cause.
5. Discussed the issue with the customer and suggested fine-tuning policies and limiting file shadowing to necessary scenarios.

## Root Cause
The root cause of the issue was identified as the encoding changes made by Libre Office when saving the XLS file. This alteration caused the EPP server to misinterpret the VID and PID data, leading to incorrect entries.

## Solution
The issue was resolved by:
- Advising the customer to avoid using Libre Office for editing the XLS files intended for bulk device enrollment.
- Suggesting the use of a different application (e.g., Microsoft Excel) to ensure proper encoding.
- Recommending a review of server policies and file shadowing settings to optimize resource usage.

## Notes
- The customer is planning to migrate to a new EPP instance, which may resolve some of the performance issues.
- It is important to ensure that any files used for bulk uploads are saved in a compatible format to prevent similar issues in the future.