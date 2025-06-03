## Ticket Metadata
- **Ticket ID:** 500Qk00000DaZpPIAV
- **Case Number:** 416233
- **Status:** Closed - Resolved
- **Account/Company:** Booking.com
- **Contact Name:** Serhat Demir
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Client
- **Feature:** EPP Client - Other
- **Version:** 6.2.3.0052 (test build)

## Problem Description
The customer reported that the Netwrix Endpoint Protector (EPP) was generating a 0-byte `.tmp` file in the `C:\Windows\Temp` directory approximately every 10 seconds, resulting in an accumulation of around 70,000 files on a single endpoint.

## Environment Details
- The issue was observed on a Windows endpoint running Netwrix Endpoint Protector.
- The specific version of the EPP client in use was not initially specified but was later identified as needing an update.

## Troubleshooting Steps
1. The support team acknowledged the issue and requested logs from the customer for further analysis.
2. A test build (version 6.2.3.0052) was provided to the customer to address the issue.
3. The support team identified that the problem was related to the `libevent` library used in the Deep Packet Inspection module of EPP.
4. A subsequent test build (version 6.2.3.0057) was sent to the customer after confirming the fix in the library.

## Root Cause
The root cause of the issue was identified as a bug in the `libevent` library, which was improperly handling temporary files due to the use of Windows 10 features for Unix domain sockets. This resulted in the creation of temporary files that were not being cleaned up.

## Solution
The issue was resolved by recompiling the `libevent` library without support for Unix domain sockets for Windows. The customer was provided with a test build (version 6.2.3.0052) that included this fix. After testing, the customer confirmed that the issue was resolved, leading to the closure of the ticket.

## Notes
- Customers experiencing similar issues with excessive temporary file generation should be advised to check for updates to the EPP client.
- If the issue persists after updating, further investigation into the specific libraries used by EPP may be necessary.
- It is recommended to monitor the temp directory for unusual file generation patterns as a proactive measure.