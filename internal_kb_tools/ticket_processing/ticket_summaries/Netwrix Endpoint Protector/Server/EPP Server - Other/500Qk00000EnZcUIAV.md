## Ticket Metadata
- **Ticket ID:** 500Qk00000EnZcUIAV
- **Case Number:** 418872
- **Status:** Closed - Resolved
- **Account/Company:** Baader Bank
- **Contact Name:** Florian Wolfschaffner
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** NONE

## Problem Description
The customer reported that no content-aware logs were being recorded by the Netwrix Endpoint Protector, with the log report only showing policy received logs.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Server

## Troubleshooting Steps
1. Verified the logging configuration settings in the Netwrix Endpoint Protector.
2. Checked for any existing updates or patches that might address logging issues.
3. Reviewed server performance and resource utilization to identify potential bottlenecks.
4. Applied hotfix 1.1 to the server.
5. Optimized server settings to enhance performance.

## Root Cause
The issue was identified as a result of server performance limitations that affected the logging functionality. The application of the hotfix and subsequent optimization resolved the underlying performance issues.

## Solution
The issue was resolved by applying hotfix 1.1 to the Netwrix Endpoint Protector server and optimizing the server settings. This allowed the system to properly record content-aware logs as intended.

## Notes
- Ensure that the server is regularly monitored for performance issues to prevent similar logging problems in the future.
- Keep the Netwrix Endpoint Protector updated with the latest patches and hotfixes to maintain optimal functionality.