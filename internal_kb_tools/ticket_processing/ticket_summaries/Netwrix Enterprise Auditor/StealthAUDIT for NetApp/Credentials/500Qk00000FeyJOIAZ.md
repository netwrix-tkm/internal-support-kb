## Ticket Metadata
- **Ticket ID:** 500Qk00000FeyJOIAZ
- **Case Number:** 420767
- **Status:** Closed - Resolved
- **Account/Company:** Thales Group Australia
- **Contact Name:** Matthew Heaton-Harris
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for NetApp
- **Feature:** Credentials
- **Version:** 11.6

## Problem Description
The customer reported that scheduled tasks within the Netwrix Enterprise Auditor were failing to execute. The Task Scheduler indicated launch failures with Event IDs 203 and 101.

## Environment Details
- **Operating System:** Not specified, but relevant folders include `C:\Windows\Tasks` and `C:\Windows\System32\Tasks`.
- **User Account:** The service account was confirmed to be part of the Administrators group and had the necessary permissions.

## Troubleshooting Steps
1. Verified permissions as per the Netwrix knowledge base article.
2. Confirmed that the service account had "Log On As Batch Job" rights in Local Security Policy.
3. Checked folder permissions for:
   - `C:\Windows\Tasks` (folder was empty)
   - `C:\Windows\System32\Tasks` (folder contained scheduled jobs)
4. Reviewed application logs which indicated "Login failed for user".

## Root Cause
The issue was identified as a permissions problem related to the database access for the service account. Despite having the necessary local permissions, the account lacked appropriate database permissions.

## Solution
Permissions were granted on the database for the service account, which resolved the issue and allowed the scheduled tasks to execute successfully.

## Notes
- Ensure that service accounts have the necessary database permissions in addition to local system permissions to avoid similar issues in the future.
- Regularly review and audit permissions for service accounts to maintain operational integrity.