## Ticket Metadata
- **Ticket ID:** 500Qk00000NCWJsIAP
- **Case Number:** 439695
- **Status:** Closed - Resolved
- **Account/Company:** Oregon Social Learning Center
- **Contact Name:** Mike Kinner
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Windows File Systems
- **Feature:** Configuration
- **Version:** 11.6

## Problem Description
The customer needed assistance configuring the Netwrix Enterprise Auditor (NEA) after replacing two DFS file servers (SAN01 and SAN02) with a single new file server (NAS01). The customer was unsure about the necessary changes, particularly regarding the DFS configuration.

## Environment Details
- **Current Software Versions:**
  - AIC: 11.6.0.3
  - NAM: 7.0.2987
  - NEA: 11.6.0.42
- **Previous Upgrade Date:** November 23, 2024

## Troubleshooting Steps
1. Scheduled a meeting with the customer to assist with the configuration.
2. Reconfigured the FileServer list in NEA to scan only the NAS01 server.
3. Removed the SAN01 and SAN02 servers from the configuration.
4. Validated that the jobs were set up to run against the new NAS01 server.
5. Ran test FSAA and FSAC jobs to ensure connectivity to the new server and verify data import.
6. Confirmed that AIC recognized the new server and could access the newly scanned data.

## Root Cause
The issue arose from the need to update the NEA configuration to reflect the changes in the file server infrastructure, specifically the transition from multiple DFS servers to a single new server.

## Solution
The issue was resolved by:
- Reconfiguring the NEA to only include the new NAS01 server.
- Ensuring that all relevant jobs were correctly set up to run against the new server.
- Successfully running tests to confirm that the new server was operational and that data was being imported correctly.

## Notes
- It is important to ensure that all old servers are removed from the configuration to avoid any conflicts or confusion in future operations.
- Regular updates to the software should be considered to maintain compatibility and security; the last upgrade was noted to be in November 2024.