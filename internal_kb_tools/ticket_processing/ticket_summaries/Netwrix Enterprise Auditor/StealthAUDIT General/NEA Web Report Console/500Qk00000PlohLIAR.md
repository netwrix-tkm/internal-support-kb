## Ticket Metadata
- **Ticket ID:** 500Qk00000PlohLIAR
- **Case Number:** 446679
- **Status:** Closed - Resolved
- **Account/Company:** EverBank
- **Contact Name:** Bradley Dickinson
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** NEA Web Report Console
- **Version:** 11.6

## Problem Description
All reports in the development environment stopped updating after the migration of the reporting system to new servers on 4/25/2025. The last successful update occurred on 4/19/2025.

## Environment Details
- **Migration Date:** 4/25/2025
- **Last Successful Update:** 4/19/2025
- **Affected Environment:** Development

## Troubleshooting Steps
1. Performed a migration of the reporting system to new servers.
2. Verified the last update time of the reports in the development environment (expected to be 4/19/2025).
3. Observed that no reports had updated since the migration date of 4/25/2025.
4. Proposed a meeting to review the configuration file for the reporting site.
5. Investigated the webserver configuration and DNS settings.

## Root Cause
The issue was caused by a misconfiguration in the webserver. Specifically, the reporting site was connecting to the wrong server due to a DNS issue, and the webserver's certificate binding was incorrect.

## Solution
The issue was resolved by performing the following steps:
1. Edited the webserver configuration to bind the correct certificate.
2. Restarted the webserver service.
3. Updated the DNS IP address to ensure the reporting site connected to the correct server.

These actions restored the reporting system's functionality, allowing reports to update as expected.

## Notes
- Ensure that DNS settings and certificate bindings are verified after any server migration to prevent similar issues.
- Regularly check the configuration files for any discrepancies post-migration to ensure proper connectivity and functionality.