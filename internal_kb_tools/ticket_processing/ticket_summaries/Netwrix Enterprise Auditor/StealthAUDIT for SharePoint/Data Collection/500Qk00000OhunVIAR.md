## Ticket Metadata
- **Ticket ID:** 500Qk00000OhunVIAR
- **Case Number:** 443880
- **Status:** Closed - Resolved
- **Account/Company:** Liberty Bank
- **Contact Name:** Ziyaad Rasool
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for SharePoint
- **Feature:** Data Collection
- **Version:** 11.6

## Problem Description
The customer reported an issue with SharePoint activity not importing correctly, resulting in an error during a bulk import job. The specific error message indicated an exception thrown by the target of an invocation.

## Environment Details
- **Error Message:** 
  ```
  [C:24] Unable to perform bulk import Error: Exception has been thrown by the target of an invocation.
  System.InvalidOperationException: This implementation is not part of the Windows Platform FIPS validated cryptographic algorithms.
  ```
- **Platform:** Netwrix Enterprise Auditor
- **Collector Code:** StealthAUDIT for SharePoint

## Troubleshooting Steps
1. Reviewed the error message provided by the customer.
2. Identified that the issue was related to FIPS (Federal Information Processing Standards) compliance.
3. Suggested potential fixes related to FIPS settings.
4. Awaited further information from the customer to confirm the environment and settings.

## Root Cause
The root cause of the issue was identified as a conflict with FIPS compliance settings on the Windows platform. The implementation being used for the bulk import was not part of the FIPS validated cryptographic algorithms, leading to the failure of the import process.

## Solution
The issue was resolved by adjusting the FIPS compliance settings on the server. This involved ensuring that the cryptographic algorithms used in the application were compliant with FIPS standards, allowing the bulk import job to complete successfully.

## Notes
- Ensure that any future implementations involving cryptographic algorithms are compliant with FIPS if the environment requires it.
- It may be beneficial to document FIPS-related configurations and their implications for similar cases to expedite troubleshooting in the future.