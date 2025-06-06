## Ticket Metadata
- **Ticket ID:** 500Qk00000OTKYbIAP
- **Case Number:** 443288
- **Status:** Closed - Resolved
- **Account/Company:** Hughes Federal Credit Union
- **Contact Name:** Zach Metz
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Disk Space
- **Version:** Not specified

## Problem Description
The customer reported that their EPP Appliance was running low on disk space, displaying a warning message indicating only 6.71 GB of free space available from a total of 19.52 GB. This situation was affecting the functionality and performance of the EPP Server.

## Environment Details
- EPP Appliance with 20 GB of memory space.
- Previous similar issue reported in January 2025.

## Troubleshooting Steps
1. Customer authorized backend access to the EPP Appliance.
2. Technical support engineer accessed the appliance and removed older files to clear space.
3. Disk usage was reduced from 65% to 52%.
4. Informed the customer about the need to migrate to a newer EPP Appliance with more disk space (50 GB) to prevent recurring issues.

## Root Cause
The EPP Appliance was operating with insufficient disk space (20 GB), which was inadequate for the customer's logging and backup needs, leading to repeated warnings about low disk space.

## Solution
The issue was partially resolved by clearing old files and reducing disk usage. However, the long-term solution involved recommending the customer migrate to a newer EPP Appliance with a larger capacity (50 GB) to avoid future disk space issues.

## Notes
- The customer was informed that DevOps is planning to expand the size of the EPP Appliance in the near future.
- The customer expressed willingness to wait for the disk space expansion.
- It is advisable for customers to regularly monitor disk space and consider upgrading their appliances if they frequently encounter low disk space warnings.