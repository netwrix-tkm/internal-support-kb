## Ticket Metadata
- **Ticket ID:** 500Qk00000LApBgIAL
- **Case Number:** 433878
- **Status:** Closed - Resolved
- **Account/Company:** Prince George's County, Maryland
- **Contact Name:** William Addis
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Custom Reports
- **Version:** 11.5

## Problem Description
The customer reported that the CDSA (Credential and Data Security Assessment) presentation did not display password information, specifically in the AD_WeakPasswords report.

## Environment Details
- The issue occurred within the Netwrix Enterprise Auditor platform, specifically while generating reports related to Active Directory weak passwords.

## Troubleshooting Steps
1. Verified the status of the Active Directory Inventory Job ("1-AD_Scan") to ensure it was running successfully.
2. Checked the status of the "Active Directory" > "2.Users" > AD_WeakPasswords job to confirm it was functioning correctly.
3. Attempted to reproduce the issue by navigating to:
   - NEA > Jobs > 'Active Directory' > 'AD weekly reports' > 2.Users > AD_WeakPasswords
4. Observed that the job connection profile was not available, leading to the failure in displaying password information.
5. Conducted a meeting with the customer to further investigate the issue based on the provided screenshots.

## Root Cause
The root cause of the issue was identified as an incorrect configuration of the job connection profile for the AD_WeakPasswords report. Specifically, no user-defined profile was selected, which prevented the job from processing the necessary data.

## Solution
1. Accessed the AD_WeakPasswords job properties and navigated to the Connection tab.
2. Selected 'SBServiceAccount' from the drop-down menu for user-defined profiles.
3. After making this selection, the AD_WeakPasswords job successfully processed over 21,000 Active Directory accounts.
4. Ran the CDSA report, which executed all weak password queries correctly, and confirmed that the results in 'AD_WeakPasswords_Details' were populated.
5. Ensured that no other jobs were running that could lock tables, then executed the CDSA Job Group, which completed in under 7 minutes, successfully populating the relevant slides in the presentation.

## Notes
- It is crucial to ensure that the correct job connection profile is selected for any report to function properly.
- Future users should verify that no other jobs are running concurrently that may lock tables, as this can affect report generation.
- Regular checks on job configurations can prevent similar issues from arising in the future.