## Ticket Metadata
- **Ticket ID:** 500Qk00000HgOoyIAF
- **Case Number:** 425583
- **Status:** Closed - Resolved
- **Account/Company:** W. L. Gore & Associates, Inc.
- **Contact Name:** Connie Liang
- **Product:** Netwrix Enterprise Auditor
- **Component:** Access Information Center
- **Feature:** Resource Audit
- **Version:** 11.6

## Problem Description
The customer reported that their `aic.log` was overwhelmed with errors related to expiring access to specific shares. The issue arose because the user associated with the access had already separated from the company, resulting in their Active Directory (AD) account being deleted and preventing the removal of their access from the shares.

## Environment Details
- The logs indicated that the Access Information Center (AIC) was attempting to remove permissions for users whose accounts no longer existed in AD.
- The errors were logged every 5 minutes, indicating a continuous failure to process expired access requests.

## Troubleshooting Steps
1. Reviewed the logs to identify the specific errors related to expired access requests.
2. Confirmed that the user accounts associated with the errors had been deleted from AD.
3. Attempted to reproduce the issue in a lab environment.
4. Investigated the AD inventory jobs to ensure they were running successfully.
5. Set the `ExpirationState` to 2 in the `SA_AIC_ResourceAccessRequests` table for each affected SID.
6. Monitored the logs for 10 minutes to check if the issue persisted.

## Root Cause
The issue was caused by the deletion of user accounts that had been granted temporary permissions. When the permissions expired, the AIC attempted to remove the access but could not find the corresponding user information, leading to repeated errors in the logs.

## Solution
The resolution involved setting the `ExpirationState` to 2 in the `SA_AIC_ResourceAccessRequests` table for each SID that was encountering the issue. This action marked the permission state as complete, effectively stopping the AIC from attempting to remove access for non-existent users.

## Notes
- It is important to monitor the AD inventory jobs regularly to ensure they are functioning correctly, as failures in these jobs can lead to similar issues.
- The logs in the AIC rotate quickly, making it challenging to troubleshoot issues that may not be reported immediately. Consider increasing the log retention period if possible.
- This case can be re-opened if any related issues arise in the future.