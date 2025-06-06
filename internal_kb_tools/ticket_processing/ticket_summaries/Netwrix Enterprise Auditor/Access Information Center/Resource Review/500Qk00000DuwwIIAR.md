## Ticket Metadata
- **Ticket ID:** 500Qk00000DuwwIIAR
- **Case Number:** 416908
- **Status:** Closed - Resolved
- **Account/Company:** RKW SE Zweigniederlassung Wasserburg
- **Contact Name:** Support Appeal
- **Product:** Netwrix Enterprise Auditor
- **Component:** Access Information Center
- **Feature:** Resource Review
- **Version:** 11.6

## Problem Description
The RKW Group reported an issue in the AIC portal where users encountered an HTTP 500 error when attempting to view the results of a Permissions Review. Despite upgrading to the latest version of AIC, the issue persisted.

## Environment Details
- **Product Version:** 11.6
- **Build Number:** 11.6.0.21

## Troubleshooting Steps
1. Verified the upgrade to the latest version of AIC.
2. Reviewed logs and screenshots provided by the customer.
3. Attempted to reproduce the error in a controlled environment.
4. Engaged with the development team to analyze the error message:
   - Error Message: `System.InvalidOperationException: The null value cannot be assigned to a member with type System.Boolean which is a non-nullable value type.`
5. Conducted SQL queries to check the integrity of the data related to the Permissions Review.

## Root Cause
The issue was identified as a bug in the AIC portal, specifically related to the handling of null values in the database, which caused the application to throw an `InvalidOperationException`.

## Solution
A fix for the identified bug was implemented and included in the cumulative update (CU) released on **August 16, 2024**. After applying the update, the issue was resolved, and users were able to view the results of the Permissions Review without encountering errors.

## Notes
- Ensure that all future updates to the AIC portal are tested for similar null value handling issues.
- Monitor for any related issues that may arise from database interactions, particularly with non-nullable value types.
- Encourage users to report any anomalies immediately after updates to facilitate quicker resolutions.