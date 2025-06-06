## Ticket Metadata
- **Ticket ID:** 500Qk00000EkndeIAB
- **Case Number:** 418770
- **Status:** Closed - Resolved
- **Account/Company:** CRH Americas Materials
- **Contact Name:** Frank Babcock
- **Product:** Netwrix Enterprise Auditor
- **Component:** Custom Reports
- **Feature:** Alerting for Schedule Job Errors
- **Version:** 11.5

## Problem Description
The customer requested assistance in configuring Netwrix Auditor to notify administrators when scheduled jobs do not run as expected or encounter errors. Given the large number of jobs, it was inefficient for administrators to manually check the status of each job.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Collector Code:** StealthAUDIT General

## Troubleshooting Steps
1. Reviewed the existing job configurations and reporting capabilities within Netwrix Enterprise Auditor.
2. Sent a mock job to examine the `SA_JobTaskStatsTbl` for job execution statistics.
3. Built a custom report named `Job_Issues_report` to filter and display jobs with errors that ended the previous day.
4. Explored the Report Configuration Wizard for email notifications regarding job statuses.

## Root Cause
The issue stemmed from the lack of built-in alerting functionality for job errors in the existing version of Netwrix Enterprise Auditor (11.5). The customer needed a more efficient way to monitor job statuses without manual checks.

## Solution
The issue was resolved by creating a custom report (`Job_Issues_report`) that specifically queries the `SA_JobTaskStatsTbl` to list only jobs that encountered errors and ended the previous day. Additionally, the following steps were recommended for individual report configurations:
- Navigate to **Netwrix Enterprise Auditor v11.6 > Administration > Reporting > Report Configuration Wizard > E-mail Page** for setting up email notifications.
- Utilize the **Instant Job Wizard** for creating jobs that track execution statistics.

## Notes
- It is advisable for administrators to regularly review and update their reporting configurations to ensure they are receiving timely notifications about job statuses.
- Future versions of Netwrix Enterprise Auditor may include enhanced alerting features, so staying updated with product releases is recommended.