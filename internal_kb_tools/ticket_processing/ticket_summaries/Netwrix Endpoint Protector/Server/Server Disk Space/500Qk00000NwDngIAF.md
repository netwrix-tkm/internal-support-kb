## Ticket Metadata
- **Ticket ID:** 500Qk00000NwDngIAF
- **Case Number:** 441698
- **Status:** Closed - Resolved
- **Account/Company:** 1Rivet
- **Contact Name:** Subetharan Muthuswami
- **Product:** Netwrix Endpoint Protector
- **Component:** Server Disk Space
- **Feature:** Server
- **Version:** NONE

## Problem Description
The customer reported that the storage drive was full and requested assistance in clearing space.

## Environment Details
- The issue was related to the Netwrix Endpoint Protector platform, specifically concerning server disk space management.

## Troubleshooting Steps
1. Identified that the space was occupied by shadow files.
2. Proposed to connect to the server to clear space.
3. Confirmed with the customer to delete shadow files older than 30 days.
4. Removed shadow files older than 30 days.

## Root Cause
The storage drive was full due to the accumulation of shadow files that were not deleted in a timely manner.

## Solution
The issue was resolved by removing shadow files that were older than 30 days, which successfully reduced the occupied space on the storage drive to 67%.

## Notes
- It is advisable to regularly monitor and manage shadow files to prevent storage issues in the future.
- Consider implementing a policy for automatic deletion of shadow files older than a specified duration to maintain optimal storage levels.