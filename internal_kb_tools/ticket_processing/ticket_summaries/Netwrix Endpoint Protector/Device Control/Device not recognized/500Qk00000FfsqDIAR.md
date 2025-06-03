## Ticket Metadata
- **Ticket ID:** 500Qk00000FfsqDIAR
- **Case Number:** 420833
- **Status:** Closed - Resolved
- **Account/Company:** BMW Group AG
- **Contact Name:** Christian Spies
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device not recognized
- **Version:** 7.1.0.0 (Server), 6.2.2.3001 (Client)

## Problem Description
The customer reported that after connecting a Canon DR-6030C scanner to the server, the external device was not recognized by the server console, preventing it from being whitelisted.

## Environment Details
- Affected device: Canon Electronics Inc. / DR-6030C
- Server Version: 7.1.0.0
- Client Version: 6.2.2.3001

## Troubleshooting Steps
1. Confirmed the scanner was connected and powered on.
2. Checked the server console for device recognition.
3. Reviewed log files for any errors related to device detection.
4. Recommended the customer to apply the upcoming 7.2.0 patch.
5. Suggested whitelisting the device using its VID/PID.
6. Engaged the R&D and QA teams for further investigation.
7. Followed up with the customer multiple times to check if the issue persisted after applying the patch.

## Root Cause
The issue was related to a MySQL error that prevented the scanner from being inserted into the server's device list. This scenario occurred when specific devices were connected, and the agent was installed for the first time on that computer.

## Solution
The customer successfully whitelisted the scanner by using its VID and PID. However, the underlying issue of the scanner not being recognized in the Endpoint Protector server remains unresolved. Further investigation is needed to determine why the scanner was not recognized initially.

## Notes
- It is important to ensure that the server is updated to the latest version (7.2.0 or later) to avoid similar issues in the future.
- Customers should be advised to use VID/PID for whitelisting devices when they encounter recognition issues.
- Continuous monitoring and feedback from customers after updates are crucial for identifying and resolving such issues promptly.