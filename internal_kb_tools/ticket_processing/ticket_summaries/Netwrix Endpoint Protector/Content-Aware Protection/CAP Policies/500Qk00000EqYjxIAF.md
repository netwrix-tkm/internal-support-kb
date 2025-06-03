## Ticket Metadata
- **Ticket ID:** 500Qk00000EqYjxIAF
- **Case Number:** 418982
- **Status:** Closed - Resolved
- **Account/Company:** Ushur Technologies Private Limited
- **Contact Name:** Prasanth Ganesan
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** CAP Policies
- **Version:** NONE

## Problem Description
The customer reported that after applying the Content-Aware Protection (CAP) policy (Block & Report) for Windows and MacOS devices, file uploads were being blocked as expected; however, the reports were not being generated.

## Environment Details
- CAP policy applied to Windows and MacOS devices.
- No specific product version was mentioned, indicating the possibility of using an outdated version.

## Troubleshooting Steps
1. Remote session was initiated to investigate the issue.
2. SQL queries were provided to check the CAP logs:
   ```sql
   SELECT count(*) from cf_log;
   ```
3. Additional SQL commands were suggested to inspect the database structure:
   ```sql
   desc cf_log;
   desc olog;
   desc cf_log_details;
   ```
4. The team confirmed that the SQL tables appeared as expected.
5. A recommendation was made to upgrade the appliance to version 5940 to resolve the issue with missing event logs for Content-Aware Protection.

## Root Cause
The issue was identified as being related to the version of the software in use. The hotfix for the problem was only applicable to version 5910, and the customer was advised to upgrade to version 5940 to ensure proper functionality of the reporting feature.

## Solution
The customer was informed about the necessity of upgrading to version 5940 to resolve the issue with report generation. However, the customer decided not to pursue the Proof of Concept (POC) further, leading to the closure of the case.

## Notes
- It is important to ensure that customers are using the latest version of the software to avoid similar issues in the future.
- If a customer is unwilling to upgrade, alternative solutions or workarounds should be discussed to address their concerns.