## Ticket Metadata
- **Ticket ID:** 500Qk00000FPPiXIAX
- **Case Number:** 420243
- **Status:** Closed - Resolved
- **Account/Company:** Ansaldo Nuclear Ltd
- **Contact Name:** Wayne Evans
- **Product:** Netwrix Endpoint Protector
- **Component:** Active Directory Sync
- **Feature:** AD Sync - Other
- **Version:** NONE

## Problem Description
The customer requested confirmation on the syntax for connecting to Active Directory (AD) to import Admin users for managing Endpoint Protector (EPP). They reported that the same credentials successfully connected to AD for syncing machines, but the connection did not work in this instance.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Active Directory Sync

## Troubleshooting Steps
1. Customer verified the syntax used for connecting to AD.
2. Confirmed that the same credentials were previously successful for syncing machines.
3. Reviewed the group name used in the connection attempt.

## Root Cause
The issue was caused by an incorrect group name in the AD connection settings.

## Solution
The customer resolved the issue by adjusting the group name in the AD connection settings to the correct one.

## Notes
- Ensure that the group names used in AD connections are verified for accuracy to avoid similar issues in the future.
- It may be beneficial to provide customers with a checklist for common configuration settings when connecting to AD.