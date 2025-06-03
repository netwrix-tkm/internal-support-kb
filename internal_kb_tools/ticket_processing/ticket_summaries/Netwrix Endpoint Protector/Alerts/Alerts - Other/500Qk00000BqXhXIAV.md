## Ticket Metadata
- **Ticket ID:** 500Qk00000BqXhXIAV
- **Case Number:** 411988
- **Status:** Closed - Resolved
- **Account/Company:** IVR Technology Group
- **Contact Name:** IVR Technology Group
- **Product:** Netwrix Endpoint Protector
- **Component:** Alerts
- **Feature:** Alerts - Other
- **Version:** Not specified

## Problem Description
The customer reported that alerts from the Netwrix Endpoint Protector (EPP) stopped sending after a reboot. This issue was similar to a previous case where rebuilding the alert cache resolved the problem.

## Environment Details
- The issue occurred after a reboot of the EPP system.
- The customer had previously experienced similar issues, indicating a recurring problem with the alert cache.

## Troubleshooting Steps
1. Scheduled a remote session to rebuild the alert cache.
2. Deleted the existing alert cache.
3. Rebuilt the alert cache to restore functionality.

## Root Cause
The root cause of the issue was identified as a failure in the alert cache, which became corrupted or non-functional after the system reboot.

## Solution
The issue was resolved by performing the following steps:
- A remote session was conducted where the support engineer deleted the existing alert cache.
- The alert cache was then rebuilt, which restored the alert functionality.

## Notes
- It is advisable to monitor the alert system after any updates or reboots to ensure alerts are functioning correctly.
- If similar issues arise in the future, rebuilding the alert cache should be the first troubleshooting step to consider.