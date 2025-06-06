## Ticket Metadata
- **Ticket ID:** 500Qk00000GJcoMIAT
- **Case Number:** 422259
- **Status:** Closed - Resolved
- **Account/Company:** ConocoPhillips Company
- **Contact Name:** Frank McNickle
- **Product:** Netwrix Enterprise Auditor
- **Component:** Access Information Center
- **Feature:** Resource Audit
- **Version:** 11.5

## Problem Description
The customer requested assistance with their Access Information Center (AIC) to ensure that scans were being properly incorporated. They were experiencing issues with the AIC query taking too long, resulting in connection timeouts.

## Environment Details
- **StealthAUDIT Version:** 11.5.0.265
- **AIC Version:** 11.5.0.137

## Troubleshooting Steps
1. Reviewed the AIC query performance and connection settings.
2. Noted that the AIC query was processing data from 85 hosts, including partially removed systems.
3. Checked the default session timeout settings for the AIC.
4. Adjusted the AuthSessionTimeout parameter to increase the timeout duration.

## Root Cause
The issue was caused by the AIC query taking longer than the default session timeout allowed for the web console, which prevented users from viewing the necessary details.

## Solution
The resolution involved adjusting the AuthSessionTimeout for the AIC from the default of 20 minutes to 90 minutes. This change allowed the AIC to maintain an active connection long enough for the queries to complete successfully.

### Reference for Configuration
- **Documentation Link:** [Netwrix Access Information Center 11.5 - Timeout Parameter](https://helpcenter.netwrix.com/bundle/AIC_11.5/page/Content/Access/InformationCenter/Admin/AdditionalConfig/Timeout_Parameter.htm)

## Notes
- It is important to monitor the performance of AIC queries, especially when dealing with a large number of hosts.
- Future adjustments to timeout settings should be documented and reviewed periodically to ensure optimal performance without compromising security.