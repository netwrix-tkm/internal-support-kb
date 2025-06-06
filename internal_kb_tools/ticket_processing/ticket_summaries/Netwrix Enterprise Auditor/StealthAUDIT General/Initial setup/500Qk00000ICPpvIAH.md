# Ticket Summary

## Ticket Metadata
- **Ticket ID:** 500Qk00000ICPpvIAH
- **Case Number:** 426778
- **Status:** Closed - Resolved
- **Account/Company:** International Motors, LLC
- **Contact Name:** William Dammeier
- **Product:** Netwrix Enterprise Auditor
- **Component:** Temporary Database Size
- **Feature:** Initial Setup
- **Version:** 11.6

## Problem Description
The customer reported that a drive on the server hosting the database was filling up with temporary files, reaching a size of 461 GB. They were concerned whether this was expected behavior, as they were informed that the temporary files being generated were as large as the database itself.

## Environment Details
- The customer is using Netwrix Enterprise Auditor version 11.6.
- The issue pertains to the temporary database (tempDB) size during job executions.

## Troubleshooting Steps
1. The customer was asked to provide details about the impact of the issue on their business and who was affected.
2. The customer was requested to outline any troubleshooting steps they had already taken.
3. The customer was asked to confirm if this was a new configuration or if any changes had been made since the last successful operation.
4. The customer was instructed to run a PowerShell command to gather information about installed software related to Netwrix products.
5. Documentation regarding tempDB sizing and requirements was provided to the customer.

## Root Cause
The size of the tempDB (461 GB) was determined to be within the expected range for the operations being performed by the Netwrix Enterprise Auditor. The customer was reassured that the tempDB size could vary based on the modules and services being utilized.

## Solution
The issue was resolved by providing the customer with documentation on tempDB sizing and requirements, which clarified that the current size was not abnormal. The customer was advised to adjust the tempDB size based on the documentation provided.

## Notes
- The customer was informed that if they experience performance issues related to the database in the future, they should open a new ticket to keep issues separated.
- The documentation link provided for tempDB sizing is crucial for understanding how to manage database resources effectively: [Netwrix Enterprise Auditor Requirements](https://helpcenter.netwrix.com/bundle/EnterpriseAuditor_11.6/page/Content/EnterpriseAuditor/Requirements/Overview.htm).