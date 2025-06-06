```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000GCmdzIAD
- **Case Number:** 421977
- **Status:** Closed - Resolved
- **Account/Company:** Hillsborough County Clerk of the Court
- **Contact Name:** Bill Stater
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Active Directory
- **Feature:** Inventory
- **Version:** 11.6

## Problem Description
The customer reported that the Active Directory Inventory (ADI) job was erroring out almost immediately with a message indicating that the length of the access control list (ACL) exceeded the allowed maximum.

## Environment Details
- The issue was related to a specific user in Active Directory who had an excessive number of permissions, potentially leading to a large token size.

## Troubleshooting Steps
1. Reviewed the error message: "Length of the access control list exceed the allowed maximum."
2. Investigated the maximum size of an ACL, which is 64 kilobytes (KB) or approximately 1,820 access control entries (ACEs).
3. Gathered logs from the following directories:
   - `Program Files (x86)\StealthAudit\Jobs\GROUP_.Active Directory Inventory\JOB_1-AD_Scan\OUTPUT`
   - `Program Files (x86)\StealthAudit\SA\Database\Logs\Application`
   - `Program Files (x86)\StealthAudit\SA\Database\Logs\SAJobEngine`
4. Executed a PowerShell script to verify the count and size of ACLs for the affected user.
5. Engaged with the customer to discuss potential cleanup of the ACLs.

## Root Cause
The issue was caused by the maximum size limitation of the ACL in Active Directory, which was exceeded due to the excessive number of permissions assigned to a specific user.

## Solution
A hotfix (auditor-enterprise-hotfix-11.6.0.053) was deployed, which modified the exception handling in the ADI job. Instead of terminating the scan upon encountering the ACL size issue, the hotfix allowed the scan to continue while logging a warning for the user that could not be scanned due to the ACL size limitation.

## Notes
- The maximum size of an ACL should be monitored to prevent similar issues in the future.
- It is advisable to clean up excessive permissions in Active Directory to maintain optimal performance and avoid hitting the ACL size limit.
- Future versions of the product should include improved handling of ACL size issues to minimize disruptions during scans.
```