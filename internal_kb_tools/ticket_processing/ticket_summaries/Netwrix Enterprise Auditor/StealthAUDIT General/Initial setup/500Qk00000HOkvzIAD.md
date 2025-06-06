## Ticket Metadata
- **Ticket ID:** 500Qk00000HOkvzIAD
- **Case Number:** 424885
- **Status:** Closed - Resolved
- **Account/Company:** John Deere Company
- **Contact Name:** Scott Prigge
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Initial setup
- **Version:** 11.6

## Problem Description
The customer requested assistance with two main issues: 
1. Guidance on replacing an expiring SSL certificate for the Published Reports and AIC interface.
2. Verification of File Permissions data from a host to ensure reliability for an upcoming financial audit.

## Environment Details
- The customer is using Netwrix Enterprise Auditor version 11.6.
- The AIC interface was displaying stale data, including shared folders that no longer existed.

## Troubleshooting Steps
1. Discussed the process for replacing the SSL certificate and provided a PowerShell script for the update.
2. Identified that the AIC was showing stale data, leading to concerns about the reliability of the NEA database.
3. Proposed dropping the entire FS tables and rebuilding them to refresh the data.
4. Steps outlined for the customer:
   - Add the job `File SystemFS_DropTables`.
   - Enable applicable analyses based on the tables to drop (at least FSAA 1 & 5).
   - Run the job.
   - Run the `File System0-CreateSchema` job.
   - Verify FSAA job configuration and run it from scheduled tasks.

## Root Cause
The AIC was displaying outdated information due to the presence of stale data in the NEA database, which was not updated even after rescanning. The SSL certificate issue arose from an incorrect format of the certificate being imported.

## Solution
1. The customer was guided on how to drop the FS tables and rescan the file systems to obtain fresh data.
2. For the SSL certificate update, the customer resolved the issue independently by ensuring the certificate was created with Microsoft certificate utilities and included the private key. The customer successfully imported the certificate and restarted the service to apply the changes.

## Notes
- Ensure that SSL certificates are created using the appropriate utilities to avoid import issues.
- When dealing with stale data in AIC, consider dropping and recreating the relevant tables to refresh the data.
- Always verify the configuration of jobs and analyses after making changes to ensure they align with customer requirements.