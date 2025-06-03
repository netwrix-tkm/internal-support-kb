## Ticket Metadata
- **Ticket ID:** 500Qk00000IBfdPIAT
- **Case Number:** 426737
- **Status:** Closed - Resolved
- **Account/Company:** Singapore- Black Sesame Technologies
- **Contact Name:** Helin Lu
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** NONE

## Problem Description
The customer reported that after resolving a previous issue with a stuck server upgrade, they were unable to access the CAP logs from the dashboard. The logs were continuously loading and eventually caused the page to crash.

## Environment Details
- Platform: Netwrix Endpoint Protector
- Collector Code: Server

## Troubleshooting Steps
1. Verified the status of the server upgrade and confirmed it was resolved.
2. Attempted to access the CAP logs from the dashboard multiple times, observing that the page would hang and eventually crash.
3. Investigated the database tables associated with the CAP logs to check for any configuration issues.

## Root Cause
The issue was identified as being caused by the tables related to the CAP logs not having partitions enabled. This lack of partitioning led to performance issues when attempting to load the logs, resulting in the page hanging and crashing.

## Solution
The resolution involved enabling partitions for the affected tables. Once the partitions were enabled, the CAP logs loaded successfully without any further issues.

## Notes
- It is recommended to ensure that partitioning is enabled for large tables in the database to prevent similar performance issues in the future.
- Regular monitoring of server performance and log access can help identify potential issues before they escalate.