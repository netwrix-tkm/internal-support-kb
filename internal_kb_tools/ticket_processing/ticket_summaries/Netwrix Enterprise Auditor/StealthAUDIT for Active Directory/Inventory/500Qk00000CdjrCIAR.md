## Ticket Metadata
- **Ticket ID:** 500Qk00000CdjrCIAR
- **Case Number:** 413994
- **Status:** Closed - Resolved
- **Account/Company:** Minnwest Bank Group
- **Contact Name:** Zeke Town
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Active Directory
- **Feature:** Inventory
- **Version:** 11.5

## Problem Description
The customer reported an issue after upgrading from an old version of StealthAudit to Enterprise Auditor. They encountered errors when attempting to run the Active Directory Inventory (ADI) scan, specifically warnings related to missing custom attributes in the Active Directory schema.

## Environment Details
- New MSSQL 2019 instance was set up.
- The upgrade to version 11.5 was performed using the GUI.
- Updated connection profiles and SQL connections were established.

## Troubleshooting Steps
1. Reviewed error logs and warnings generated during the ADI scan.
2. Identified specific warnings related to custom Active Directory attributes not being set.
3. Suggested checking the configuration of the service account permissions.
4. Provided a support article link for further guidance on the warnings.
5. Advised the customer to share a screenshot of the messages table for the AD scan job for deeper analysis.

## Root Cause
The root cause of the issue was identified as the AD inventory scan job searching for common Active Directory schema attributes that were not implemented in the customer's environment. The warnings were generated because the job was looking for attributes that were not set in the domain.

## Solution
The customer resolved the issue by removing the unused custom attributes from the query settings in the ADI scan configuration. After making these adjustments, the scan completed successfully without generating warnings.

## Notes
- It is important to ensure that the Active Directory schema is configured correctly and that any custom attributes required by the Netwrix product are set up in the environment.
- Future users should be aware that warnings related to custom attributes do not necessarily prevent the scan from running but may indicate configuration discrepancies that should be addressed for optimal performance.