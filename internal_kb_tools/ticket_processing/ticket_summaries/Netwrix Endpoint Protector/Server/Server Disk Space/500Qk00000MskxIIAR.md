## Ticket Metadata
- **Ticket ID:** 500Qk00000MskxIIAR
- **Case Number:** 438678
- **Status:** Closed - Resolved
- **Account/Company:** Infibeam Avenues Limited / CCAvenue
- **Contact Name:** Akash Shivtare
- **Product:** Netwrix Endpoint Protector
- **Component:** Server Disk Space
- **Feature:** Server
- **Version:** NONE

## Problem Description
The customer, Infibeam Avenues Limited, reported that their EPP Appliance was running low on disk space and required assistance to free up space.

## Environment Details
- The issue was identified on the customer's system partition, which was critically low on disk space.

## Troubleshooting Steps
1. **Initial Assessment:** The support team requested a screenshot of the "System Information" page from the customer to assess the disk space usage.
2. **Remote Session Scheduling:** A remote session was proposed to further investigate the issue.
3. **Customer Response:** The customer provided the requested screenshot and confirmed that they were available for a remote session.
4. **Snapshot Requirement:** The support team requested the customer to prepare a snapshot of their Endpoint Protector appliance prior to the remote session for safety.
5. **Log Review:** During the remote session, it was discovered that the SIEM logs were not being sent due to a connectivity issue, contributing to the low disk space.

## Root Cause
The low disk space was primarily caused by accumulated SIEM logs that were not transmitted due to connectivity issues, leading to their retention on the appliance.

## Solution
The issue was resolved by clearing the accumulated SIEM logs from the appliance, which freed up the necessary disk space. The customer confirmed that they could delete the logs, allowing the support team to proceed with the cleanup.

## Notes
- Ensure that customers are aware of the importance of monitoring disk space and the potential impact of untransmitted logs.
- It is advisable to have a snapshot of the appliance ready before performing any significant changes to prevent data loss or downtime.