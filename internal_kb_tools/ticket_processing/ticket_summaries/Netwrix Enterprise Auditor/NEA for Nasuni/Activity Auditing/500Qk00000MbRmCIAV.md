## Ticket Metadata
- **Ticket ID:** 500Qk00000MbRmCIAV
- **Case Number:** 437861
- **Status:** Closed - Resolved
- **Account/Company:** Honeywell International
- **Contact Name:** Jesse Doran
- **Product:** Netwrix Enterprise Auditor
- **Component:** NEA for Nasuni
- **Feature:** Activity Auditing
- **Version:** 11.5

## Problem Description
The customer reported that two hidden shares on different Nasuni filers were not appearing in the FSAA/SDD scan results, making it impossible to audit these shares. The issue was identified when specific audit information was requested for these shares.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Product Version:** 11.5
- **Build Number:** 11.5.0.249

## Troubleshooting Steps
1. The customer harvested logs and related information from one of the Nasuni filers and provided it for analysis.
2. Support staff reviewed the configuration settings on the Nasuni side to identify any potential issues.
3. Discussions were held regarding the possibility of hidden shares due to configuration options in the query.

## Root Cause
The issue was determined to be caused by an incorrect configuration setting on the Nasuni side, which prevented the hidden shares from being audited.

## Solution
The customer corrected the configuration setting on the Nasuni side, which resolved the issue and allowed the hidden shares to be included in the FSAA/SDD scan results.

## Notes
- Ensure that configuration settings on Nasuni devices are verified regularly to prevent similar issues in the future.
- It may be beneficial to document any specific configurations that affect auditing to assist in troubleshooting similar cases.