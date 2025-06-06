```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000BoZqfIAF
- **Case Number:** 411907
- **Status:** Closed - Resolved
- **Account/Company:** Bank of America Corporation
- **Contact Name:** Gregory Meyer
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Initial setup
- **Version:** 11.5

## Problem Description
The customer reported a UI error stating "root element is missing" when attempting to access host lists at the group level after upgrading from version 11.0 to 11.5.

## Environment Details
- The issue occurred specifically when selecting host lists in the settings of any job.
- The error did not appear at the job or global level.

## Troubleshooting Steps
1. Confirmed the issue occurs when accessing host lists at the group level.
2. Attempted a repair on StealthAUDIT, which did not resolve the issue.
3. Collected application logs and SQL scripts related to host name updates.
4. Reviewed the logs and SQL scripts for any errors or anomalies.
5. Suggested checking if the installer was blocked via File Properties.
6. Discussed the possibility of a blocked install affecting the upgrade process.

## Root Cause
The root cause of the issue was not definitively identified. However, it was suspected that the upgrade process may have encountered a problem, potentially due to a blocked installation.

## Solution
The customer resolved the issue by rolling back to the previous version (11.0) and then re-upgrading to version 11.5. This process corrected the error, allowing access to the host lists without encountering the "root element is missing" message.

## Notes
- Ensure that any upgrade processes are monitored for potential installation blocks.
- It may be beneficial to run a stock job from instant solutions to verify if the issue persists across different configurations.
- Collecting detailed logs during upgrades can help in diagnosing similar issues in the future.
```