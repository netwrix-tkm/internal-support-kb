```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000CJMxBIAX
- **Case Number:** 413045
- **Status:** Closed - Resolved
- **Account/Company:** IBM - Etihad Airways
- **Contact Name:** Praveen Huilgol
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Migration
- **Version:** 11.5

## Problem Description
The customer requested guidance on where to change the password for the Stealth Audit account after a mandatory password reset. They needed to ensure that the new password was updated across all configurations in the Stealth Audit console.

## Environment Details
- The issue occurred in a production environment.
- The customer was using Netwrix Enterprise Auditor version 11.5.

## Troubleshooting Steps
1. Provided the customer with a link to the relevant documentation detailing where to change the password in the Stealth Audit console.
2. Followed up with the customer to confirm if they needed further assistance or clarification.
3. Scheduled a call to discuss the issue in detail after the customer expressed difficulty in understanding the documentation.
4. Confirmed the status of jobs and reports post-password reset.

## Root Cause
The issue arose after the customer reset the password for the service account used by the Stealth Audit tool. After the reset, jobs for Active Directory (AD) and Exchange were not running, and reports were not being generated.

## Solution
The customer was advised to ensure that all configurations in the Stealth Audit console were updated with the new password. They were also encouraged to check the job statuses manually and verify any error messages that appeared in the console. A follow-up meeting was scheduled to assist them further.

## Notes
- It is crucial to ensure that all service accounts and configurations are updated with the new password immediately after a reset to avoid disruptions in job execution and reporting.
- Future cases should emphasize the importance of checking job statuses and error messages in the console after a password change.
- If the customer is unable to resolve the issue through documentation, a direct walkthrough via a call may be necessary.
```