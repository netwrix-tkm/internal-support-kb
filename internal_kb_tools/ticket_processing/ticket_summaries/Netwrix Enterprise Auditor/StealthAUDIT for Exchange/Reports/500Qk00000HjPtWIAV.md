## Ticket Metadata
- **Ticket ID:** 500Qk00000HjPtWIAV
- **Case Number:** 425734
- **Status:** Closed - Resolved
- **Account/Company:** The Baupost Group
- **Contact Name:** Charlie Davidson
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Exchange
- **Feature:** Reports
- **Version:** 11.6.0.112

## Problem Description
After upgrading to version 11.6.0.112 to address an issue with the "AIC Import - PF Entitlements" analysis task, a new error occurred during the execution of the PF_Entitlements job. The error message indicated that a specific data type could not be found, leading to a failure in the analysis task.

## Environment Details
- The customer was using Netwrix Enterprise Auditor with the latest AIC version 11.6.0.25, which was required for the hotfix.
- The error was related to the PF_Entitlements job, specifically during the AIC Import - PF Entitlements analysis task.

## Troubleshooting Steps
1. Attempted to reproduce the error in a lab environment but was unsuccessful.
2. Set up the PF_EntitlementScans job in the lab, as it had not been run previously.
3. Checked the lab database for the existence of the [dbo.SA_AIC_FlexibleResourceTypesImport] reference in tables, views, stored procedures, or functions, but it was not found.
4. Reviewed job logs for additional clarification, but they did not provide useful information.

## Root Cause
The issue was determined to be related to the "PF_EntitlementsScan" job not being executed prior to the "PF_Entitlements" job. This sequence was necessary for the tables to be properly correlated, a requirement that was not documented in the hotfix notes.

## Solution
To resolve the issue, it was recommended that the customer run the "PF_EntitlementsScan" job successfully before executing the updated "PF_Entitlements" job. This ensured that all necessary data types and correlations were established, preventing the error from occurring.

## Notes
- It is important to ensure that the "PF_EntitlementsScan" job is run prior to the "PF_Entitlements" job to avoid similar issues in the future.
- Consider creating a knowledge base article to document this dependency, as it was not mentioned in the hotfix notes.
- Monitor for any recurrence of the error after applying the hotfix and running the jobs in the correct order.