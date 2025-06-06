## Ticket Metadata
- **Ticket ID:** 500Qk00000KBxCcIAL
- **Case Number:** 431127
- **Status:** Closed - Resolved
- **Account/Company:** Bank of America Corporation
- **Contact Name:** Greg Dieter
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Windows File Systems
- **Feature:** Access Auditing
- **Version:** 11.5

## Problem Description
The customer requested guidance on how to configure a Linux server to allow StealthAudit v11.5 FSAA scanning.

## Environment Details
- The specific version of Linux running on the endpoints was not initially provided by the customer, which is critical for providing accurate configuration guidance.

## Troubleshooting Steps
1. Requested the customer to specify which version(s) of Linux they were using on their endpoints.
2. Inquired if there was a Linux Administrator available in the organization who could assist with the configuration.
3. Provided a list of specific questions that needed to be answered to proceed with the configuration:
   - How to verify if a Linux host is running NFSv3 or older?
   - Whether all Unix hosts have firewalls.
   - How to set the `no_root_squash` flag on an export policy.

## Root Cause
The issue stemmed from a lack of specific information regarding the Linux version in use, which is essential for providing tailored configuration instructions for StealthAudit scanning.

## Solution
The issue was resolved by emphasizing the need for the customer to provide the version of Linux they were using. Once this information was obtained, the support team could offer precise guidance on configuring the Linux server for FSAA scanning.

## Notes
- It is crucial to obtain detailed information about the operating system version when dealing with Linux configurations, as solutions can vary significantly between different distributions and versions.
- Future inquiries should include a prompt for the customer to confirm the presence of a Linux Administrator who can assist with technical configurations.