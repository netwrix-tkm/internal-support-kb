## Ticket Metadata
- **Ticket ID:** 500Qk00000ILOUqIAP
- **Case Number:** 427179
- **Status:** Closed - Resolved
- **Account/Company:** City of Pueblo, CO
- **Contact Name:** Craig Gritz
- **Product:** Netwrix Enterprise Auditor
- **Component:** Custom Reports
- **Feature:** AD Lockouts Reporting
- **Version:** 11.6

## Problem Description
The customer requested assistance in generating a report that shows Active Directory (AD) lockouts for a specific individual during a defined time period.

## Environment Details
- **Netwrix Enterprise Auditor Version:** 11.6
- **Collector Code:** StealthAUDIT General

## Troubleshooting Steps
1. Confirmed the existence of an out-of-the-box (OOTB) "Lockouts" report in NEA 11.6.
2. Provided guidance on how to create a custom report for AD lockouts:
   - Selected the table `SA_AD_AccountLockouts_Details`.
   - Used the Filter Editor to set "Days since Event" to "Is less than or equal to" 30.
   - Navigated to "Active Directory" > "Hourly" > "5.Lockouts".
   - Executed the report by right-clicking and selecting "Run Group".
3. Addressed customer concerns regarding missing data prior to 30 days and differences in their interface compared to examples provided.

## Root Cause
The issue stemmed from the customer's unfamiliarity with the reporting interface and the specific steps required to filter and generate the desired report. Additionally, the customer was unaware that data older than 30 days may not be retained based on their configuration.

## Solution
The issue was resolved by guiding the customer through the report creation process during a scheduled call. The following steps were confirmed:
1. Use the table `SA_AD_AccountLockouts_Details`.
2. Apply the filter for "Days since Event" to be "Is less than or equal to" 30.
3. Access the report through "Active Directory" > "Hourly" > "5.Lockouts".
4. Execute the report using the "Run Group" option.

The customer was also informed about the scheduling options for the report to run daily, every three days, or weekly.

## Notes
- It is important for users to be aware that data retention policies may affect the availability of historical data, particularly for events older than 30 days.
- Future users should ensure they are familiar with the reporting interface and the specific steps required to create and filter reports to avoid similar issues.