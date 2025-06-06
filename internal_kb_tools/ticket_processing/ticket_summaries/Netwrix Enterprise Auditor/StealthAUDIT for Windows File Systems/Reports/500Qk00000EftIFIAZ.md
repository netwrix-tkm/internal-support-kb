## Ticket Metadata
- **Ticket ID:** 500Qk00000EftIFIAZ
- **Case Number:** 418572
- **Status:** Closed - Resolved
- **Account/Company:** Virginia Lottery
- **Contact Name:** James Monteria
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Windows File Systems
- **Feature:** Reports
- **Version:** 11.6.0.49

## Problem Description
The customer reported that the Permission Change scan job in the report section of STEALTHAudit was failing with the error message: “Unexpected exception: Error while publishing report. Exiting with message: Sequence contains more than one matching element.” This issue prevented the customer from viewing any new changes in the Permission Change reports, which only displayed information from September 2021.

## Environment Details
- **Netwrix Enterprise Auditor Version:** 11.6.0.49
- **Collector Code:** StealthAUDIT for Windows File Systems

## Troubleshooting Steps
1. Verified the error message during the execution of the Permission Change scan job.
2. Attempted to reproduce the issue in a lab environment using NEA version 11.6.0.89 with the display type set to chart.
3. Investigated the report element configuration for potential bugs.
4. Changed the display type from chart to grid and saved the configuration.

## Root Cause
A bug was identified within the reports element configuration in NEA version 11.6.0.49. Specifically, if the display type was set to chart, the report element would not save correctly, leading to the failure of the scan job.

## Solution
The issue was resolved by changing the display type from chart to grid and saving the configuration. After this change, the FS_PermissionChanges report was successfully generated without errors. It was also recommended to upgrade from NEA version 11.6.0.49 to a later version to potentially avoid similar issues in the future.

## Notes
- It is advisable for users experiencing similar issues to check the display type settings in their report configurations.
- Upgrading to a later version of NEA may help mitigate bugs present in earlier versions.
- No email communications or additional comments were recorded for this case.