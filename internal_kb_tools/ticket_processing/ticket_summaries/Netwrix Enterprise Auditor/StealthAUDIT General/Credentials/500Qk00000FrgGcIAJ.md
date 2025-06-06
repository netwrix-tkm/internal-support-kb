```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000FrgGcIAJ
- **Case Number:** 421221
- **Status:** Closed - Resolved
- **Account/Company:** Keystone Bank
- **Contact Name:** Emmanuel Eze
- **Product:** Netwrix Enterprise Auditor
- **Component:** Credentials
- **Feature:** Credentials
- **Version:** 11.6

## Problem Description
The customer reported an issue where they were unable to save scheduled job settings in the Netwrix Enterprise Auditor application. An unspecified error was returned when attempting to save the settings.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Collector Code:** StealthAUDIT General

## Troubleshooting Steps
1. Verified the configuration of the scheduled jobs in the Netwrix Enterprise Auditor.
2. Checked the permissions of the Active Directory (AD) service account used for running the scheduled tasks.
3. Attempted to replicate the error by creating new scheduled jobs with different settings.
4. Reviewed the application logs for any error messages related to the job scheduling process.

## Root Cause
The issue was caused by the AD service account not having the necessary permissions to run scheduled tasks due to the absence of an assigned role in the Netwrix Enterprise Auditor console.

## Solution
The problem was resolved by assigning the "Administrator" role to the AD service account. Once this role was assigned, the scheduled tasks were able to kick off successfully without any errors.

## Notes
- Ensure that all service accounts used for scheduled tasks in Netwrix Enterprise Auditor have the appropriate roles assigned to avoid similar issues in the future.
- Regularly review permissions and roles for service accounts to maintain proper functionality.
```