## Ticket Metadata
- **Ticket ID:** 500Qk00000FFVkPIAX
- **Case Number:** 419796
- **Status:** Closed - Resolved
- **Account/Company:** CMS Distribution
- **Contact Name:** Adrian Stanca
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Upgrade
- **Version:** 6.2

## Problem Description
The customer reported that they were unable to upgrade their clients to version 6.2.2.1 because most of the clients were greyed out in the upgrade interface, indicating that they could not be selected for the upgrade.

## Environment Details
- The clients were running a vulnerable version of the software prior to the attempted upgrade.

## Troubleshooting Steps
1. Reviewed the upgrade interface to confirm which clients were greyed out.
2. Attempted to initiate the upgrade process but found that the clients remained unselectable.
3. Deleted the old upgrade job that was likely causing the issue.
4. Informed the customer on how to clear old unused licenses.
5. Restarted the upgrade job after the old job was cancelled.

## Root Cause
The issue was caused by an old upgrade job that was still active, which prevented the clients from being selected for the new upgrade process.

## Solution
The problem was resolved by cancelling the old upgrade job and starting a new one. This allowed the clients to be selected for the upgrade to version 6.2.2.1.

## Notes
- It is important to ensure that no old upgrade jobs are active before attempting to initiate a new upgrade to avoid similar issues in the future.
- Customers should be advised to clear any old unused licenses that may interfere with the upgrade process.