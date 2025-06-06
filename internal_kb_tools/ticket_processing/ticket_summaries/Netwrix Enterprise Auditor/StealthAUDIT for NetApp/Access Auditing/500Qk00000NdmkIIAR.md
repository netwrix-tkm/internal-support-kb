## Ticket Metadata
- **Ticket ID:** 500Qk00000NdmkIIAR
- **Case Number:** 440823
- **Status:** Closed - Resolved
- **Account/Company:** Turkish Airlines
- **Contact Name:** Ibrahim Fil
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for NetApp
- **Feature:** Access Auditing
- **Version:** 11.6

## Problem Description
The customer, Turkish Airlines, reported that file system logs have not been imported into the database since February 16th, 2025. The FSAC System Scan Job was not functioning properly, and errors were also observed with the FSAA System Scan job.

## Environment Details
- The customer upgraded the Netwrix Enterprise Auditor environment from version 11.5 to 11.6 on February 18, 2025.
- The hostname of the StealthAudit and Proxy Server exceeded 15 characters, which is a limitation in the system.

## Troubleshooting Steps
1. Verified that the FSAA System Scan job was configured to use "Automatic" certificate management.
2. Cleared all existing certificates using the `FSAACertificateExchangeManager.exe` tool.
3. Ran the FSAA System Scan job and observed errors related to securing communication between the NEA host and NetAPP host.
4. Checked the NetBIOS names of the StealthAudit server and FSAA Proxy Server to ensure they were shorter than 15 characters.
5. Updated the Hosts file on the StealthAudit server to include the IP address and the first 15 characters of the Proxy Server's hostname.
6. Restarted the FSAA System Scan job to verify if the error persisted.
7. If the error persisted, suggested decreasing the length of the NetBIOS name for both the StealthAudit server and FSAA Proxy Server.
8. Rerun the FSAA System Scan job and confirmed successful completion.
9. Ran the FSAC System Scan job to verify if activity logs were imported into the database.

## Root Cause
The issue was primarily caused by the StealthAudit server's NetBIOS name exceeding 15 characters, which led to failures in securing communication and authentication during the FSAA and FSAC system scans.

## Solution
To resolve the issue, the NetBIOS name for both the StealthAudit server and the FSAA Proxy Server was decreased to comply with the 15-character limit. After making these changes, the FSAA System Scan job was able to run successfully, and the FSAC System Scan job was also verified to function correctly.

## Notes
- Ensure that any future server names comply with the 15-character limit for NetBIOS names to avoid similar issues.
- It is important to verify the configuration of the NetAPP server as per the guidelines provided in the Netwrix documentation to ensure proper functionality of the FSAA and FSAC scans.