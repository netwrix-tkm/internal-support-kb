## Ticket Metadata
- **Ticket ID:** 500Qk00000HZjBnIAL
- **Case Number:** 425276
- **Status:** Closed - Resolved
- **Account/Company:** Ernst & Young USA
- **Contact Name:** Doug Russell
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** Not specified

## Problem Description
The customer reported an issue with generating reports for write and copy activities across all users for the past 3 and 6 months. Upon selecting the desired date range and applying the filter, the output did not reflect the expected data for the specified time frames.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Server

## Troubleshooting Steps
1. The customer attempted to run reports on both servers for the specified date ranges (3 months and 6 months).
2. The customer selected the date range and clicked "apply" but did not receive the expected output.
3. The customer reached out for assistance to gather logs related to the reporting issue.

## Root Cause
The root cause of the issue was not explicitly identified in the case. However, it was determined that the data required for the reports was not available through the Netwrix Endpoint Protector reporting feature.

## Solution
The issue was resolved by gathering the necessary data from Splunk instead of relying on the Netwrix Endpoint Protector reporting functionality. The customer was able to obtain the required logs through this alternative method.

## Notes
- It is important to consider alternative data sources, such as Splunk, when the reporting features of Netwrix Endpoint Protector do not yield the expected results.
- Future users experiencing similar reporting issues should verify the availability of data in the system and consider using external logging tools if necessary.