## Ticket Metadata
- **Ticket ID:** 500Qk00000IuczVIAR
- **Case Number:** 428465
- **Status:** Closed - Resolved
- **Account/Company:** WOLTERSKLUWE (FORMERLY CRONER CCH GROUP LTD)
- **Contact Name:** Prashant Sangawar
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Disk Space
- **Version:** NONE

## Problem Description
The customer reported that the EPP (Endpoint Protector) Portal was displaying an "Internal Server Error."

## Environment Details
- The issue was related to the server disk space being filled up, which likely contributed to the internal server error.

## Troubleshooting Steps
1. Initial communication was established with the customer to schedule a remote session for further investigation.
2. The support team requested availability from the customer for a remote session to analyze the disk space usage.
3. A remote session was conducted to investigate the cause of the disk space issue.

## Root Cause
The root cause of the internal server error was identified as the presence of older sysbackup files that were consuming excessive disk space.

## Solution
The issue was resolved by removing the older sysbackup files, which freed up sufficient disk space and allowed the EPP Portal to function correctly without displaying the internal server error.

## Notes
- It is advisable to regularly monitor disk space usage and manage backup files to prevent similar issues in the future.
- Customers should be informed about the importance of maintaining adequate disk space for optimal performance of the EPP Portal.