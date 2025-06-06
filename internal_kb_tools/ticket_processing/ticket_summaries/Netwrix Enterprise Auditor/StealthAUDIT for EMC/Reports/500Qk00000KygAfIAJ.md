## Ticket Metadata
- **Ticket ID:** 500Qk00000KygAfIAJ
- **Case Number:** 433311
- **Status:** Closed - Resolved
- **Account/Company:** Advent Health System
- **Contact Name:** Paul Williams
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for EMC
- **Feature:** Reports
- **Version:** 11.6

## Problem Description
The customer reported that the Open Access report was displaying incorrect data, specifically that a share would reappear every other scan even after it had been removed.

## Environment Details
- **Affected Servers:**
  - ADCVUTLPACMS100: Previously showed entire C & D drives shared, but currently has no shares.
  - CARVSQLRDSMS003: Had a share in January that was remediated on 1/28, but still appeared in the last scan on 2/28 despite no shares existing on the server.

## Troubleshooting Steps
1. Ran the Open Access report to verify the presence of shares that should not be open.
2. Reviewed the FSAA_Exceptions job for the affected servers and found it had not been run consistently.
3. Conducted a meeting to discuss the issue with the customer and reviewed the Open Access report findings.
4. Successfully kicked off the FSAA_Exceptions job for CARVSQLRDSMS003, which had been disabled.

## Root Cause
The issue was caused by the FSAA_Exceptions job not being run consistently prior to generating the Open Access report. This led to stale data being displayed in the report, showing shares that had already been remediated.

## Solution
The problem was resolved by ensuring that the FSAA_Exceptions job was run successfully for the affected servers. After running the job, the customer was instructed to rerun the Open Access report, which confirmed that the previously remediated share on CARVSQLRDSMS003 no longer appeared. The customer later confirmed that the issue was resolved.

## Notes
- It is crucial to run the FSAA_Exceptions job consistently before generating reports to ensure accurate data.
- If similar issues arise, verify the status of the FSAA_Exceptions job and ensure it is enabled and scheduled correctly.