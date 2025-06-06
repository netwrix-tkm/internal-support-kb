## Ticket Metadata
- **Ticket ID:** 500Qk00000MXLYtIAP
- **Case Number:** 437638
- **Status:** Closed - Resolved
- **Account/Company:** AHS Management Company, Inc.
- **Contact Name:** Nathan Funk
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Active Directory
- **Feature:** Reports
- **Version:** 11.6

## Problem Description
The customer reported discrepancies in the Sensitive Group Membership report generated on Sundays. Specifically, the report indicated that two users were members of the DnsAdmins group, but upon manual verification, these users were not found to be members. After refreshing the report, the users were no longer listed, raising concerns about the reliability of the data.

## Environment Details
- The Active Directory Inventory job runs daily.
- The Sensitive Group Membership report runs weekly on Sundays.
- The Netwrix Threat Prevention (NTP) system is configured to collect group membership changes.

## Troubleshooting Steps
1. Verified the report generated on 03/02/2025 showed users who were removed from the group on 02/24/2025.
2. Confirmed that NTP was successfully collecting events related to group membership changes.
3. Conducted a test by adding a user (Ereyes01) to the MSHDnsAdmins group and then removing them to see if the changes would reflect in the report.
4. Reviewed debug logs from the report runs for any errors or discrepancies.
5. Scheduled a meeting for further investigation and analysis of job configurations.

## Root Cause
The issue was identified as a timing problem between the job that updates the SensitiveSecurityGroups_Membership table and the job that generates the Sensitive Group Membership report. The update job was scheduled to run on Monday mornings, while the report was generated on Sundays, leading to outdated data being reported.

## Solution
To resolve the issue, the job that updates the SensitiveSecurityGroups_Membership table was rescheduled to run on Sundays at 5 AM, prior to the report generation. This adjustment ensures that the report reflects the most current group membership data.

## Notes
- It is crucial to ensure that the timing of data updates aligns with report generation schedules to avoid discrepancies.
- Future configurations should be reviewed to confirm that all relevant jobs are set to run in a logical sequence to maintain data integrity.