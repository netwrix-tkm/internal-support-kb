## Ticket Metadata
- **Ticket ID:** 500Qk00000LnWqjIAF
- **Case Number:** 435621
- **Status:** Closed - Resolved
- **Account/Company:** Crestron Electronics
- **Contact Name:** Dean Bardowell
- **Product:** Netwrix Enterprise Auditor
- **Component:** Access Information Center
- **Feature:** Reports
- **Version:** 11.5

## Problem Description
The customer reported that the Activity Information Center (AIC) was displaying Nasuni activity in C: paths instead of UNC paths, making it difficult to utilize the activity data effectively. All activity from multiple filers was being stored under a single host in AIC, which complicated data retrieval.

## Environment Details
- **Application Server:** AZR-NWXAPPSRV (where StealthAudit is installed)
- **Monitoring Tool:** Activity Monitor
- **File System Activity Collector (FSAC) and File System Activity Analyzer (FSAA)** jobs were involved in the monitoring process.

## Troubleshooting Steps
1. Reviewed the configuration of FSAC and FSAA jobs and discovered incorrect host mappings.
2. Modified the host list and query settings to target all Nasuni hosts instead of a singular host.
3. Adjusted the Bulk Import host lists for each scan to include all Nasuni hosts.
4. Ran the scans and monitored their status, confirming successful scanning of each Nasuni filer.
5. Temporarily set the file scan depth to 0 for testing purposes and confirmed the new file structure in AIC.
6. Reset the file scan depth back to 10 for subsequent scheduled scans.
7. Divided FSAA System scans and Bulk Import into different job groups for better management.
8. Resolved bulk import errors related to database mismatches by removing host data for individual Nasuni hosts.
9. Reconfigured the FSAA system scan job to target local hosts and used a static Nasuni host list.
10. Verified that activity details were displayed correctly under each Nasuni filer in AIC.

## Root Cause
The issue was caused by the FSAC system scans being configured to use a host query method that pointed to a singular host. This configuration led to all file system activity being displayed under one host in AIC, without a proper file system structure for the multiple Nasuni hosts.

## Solution
The resolution involved modifying the query settings to point to the NAS agent used as a proxy host and selecting all Nasuni files within the host list. After these adjustments, the scans were able to collect permissions and activity data from all Nasuni hosts, allowing for a structured display of activity in AIC. The UNC paths were successfully displayed, resolving the original issue.

## Notes
- Ensure that the host list and query settings are correctly configured to avoid similar issues in the future.
- The UNC path display in AIC is a requirement for StealthAudit to properly identify and enumerate shares, which is essential for building the file structure within AIC.
- Monitor the FSAC and FSAA scans regularly to ensure they are functioning as expected and to catch any potential issues early.