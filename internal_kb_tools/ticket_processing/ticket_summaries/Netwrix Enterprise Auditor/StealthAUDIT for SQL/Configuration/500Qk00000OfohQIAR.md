## Ticket Metadata
- **Ticket ID:** 500Qk00000OfohQIAR
- **Case Number:** 443793
- **Status:** Closed - Resolved
- **Account/Company:** Allstate Insurance Company
- **Contact Name:** Stealth Audit
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for SQL
- **Feature:** Configuration
- **Version:** 11.6

## Problem Description
The customer reported that SQL permission scans were only successfully executing on one of their four production SQL servers, despite the DBA team applying all required permissions to each server.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Product Version:** 11.6
- **Collector Code:** StealthAUDIT for SQL

## Troubleshooting Steps
1. Confirmed that all required permissions were applied to all production SQL servers.
2. Conducted a UDL (Universal Data Link) test to verify connectivity.
3. Re-entered passwords for the SQL servers.
4. Verified that the host list correctly identified the servers as SQL servers.
5. Checked the SQL DC Query of permissions scan for proper configuration.
6. Tested connections in the Filters section of the SQL permissions scan.

## Root Cause
The issue was primarily caused by incorrect access settings in SQL, which prevented the scans from executing successfully on three of the four production servers.

## Solution
The issue was resolved by correcting the access settings in SQL. Once the appropriate permissions were applied correctly across all servers, the SQL permission scans executed successfully on all production servers.

## Notes
- It is important to ensure that access settings are consistently applied across all SQL servers to avoid similar issues in the future.
- Regular checks and tests (like UDL tests) should be performed to confirm connectivity and permissions before executing scans.