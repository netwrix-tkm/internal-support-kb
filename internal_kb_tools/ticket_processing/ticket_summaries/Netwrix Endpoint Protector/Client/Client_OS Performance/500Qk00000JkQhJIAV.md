## Ticket Metadata
- **Ticket ID:** 500Qk00000JkQhJIAV
- **Case Number:** 430448
- **Status:** Closed - Resolved
- **Account/Company:** Beacons Pharmaceuticals Pte Ltd
- **Contact Name:** Halodata Support Tech
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client/OS Performance
- **Version:** NONE

## Problem Description
The customer reported that the Outlook application was shutting down immediately after the installation of the Endpoint Protector (EPP) client on their PC.

## Environment Details
- **Affected Application:** Outlook 2019
- **Issue Trigger:** Installation of EPP client
- **Advanced Scanning ID:** 5940

## Troubleshooting Steps
1. Reviewed the video and EPP client logs provided by the customer.
2. Identified that Outlook 2019 was affected by the Advanced Scanning feature of the EPP client.
3. Attempted to replicate the issue in a controlled environment to confirm the behavior.

## Root Cause
The issue was caused by the Advanced Scanning feature of the EPP client, which interfered with the normal operation of Outlook 2019, leading to the application shutting down unexpectedly.

## Solution
To resolve the issue, Outlook was added to the Advanced Scanning exception list within the EPP client settings. This adjustment allowed Outlook to function normally without being affected by the scanning processes.

## Notes
- It is recommended to monitor the performance of Outlook after adding it to the exception list to ensure that no further issues arise.
- Future installations of the EPP client should consider reviewing application compatibility, especially with commonly used software like Outlook.