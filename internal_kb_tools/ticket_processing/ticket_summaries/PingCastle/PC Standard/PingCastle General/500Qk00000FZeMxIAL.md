## Ticket Metadata
- **Ticket ID:** 500Qk00000FZeMxIAL
- **Case Number:** 420566
- **Status:** Closed - Resolved
- **Account/Company:** T-Systems México
- **Contact Name:** Karina Torres-Rodriguez
- **Product:** PingCastle
- **Component:** PC Standard
- **Feature:** PingCastle General
- **Version:** 3.2.0.1

## Problem Description
The customer reported an issue with the detection of the S-PwdLastSet-45 vulnerability, indicating that the tool was providing a detection date that was ahead of schedule (October of the current year). They requested assistance in verifying if any parameters were missing for validation.

## Environment Details
- **Platform:** PingCastle
- **Collector Code:** PC Standard
- **Product Version:** 3.2.0.1

## Troubleshooting Steps
1. Reviewed the Last Logon Dates of affected computers, specifically the LastLogonTimestamp from the Domain Controller.
2. Suggested verifying LastLogonTimestamp using:
   - Active Directory Users and Computers (with advanced features enabled).
   - PowerShell commands to check LastLogonDate and LastLogonTimestamp.
3. Provided links to relevant code sections in the PingCastle GitHub repository for further investigation.
4. Recommended checking the server time settings due to a known Windows bug that could cause future dates.
5. Suggested clearing or resetting LastLogonTimestamp values and logging in again to update them.

## Root Cause
The issue was identified as a bug in Windows that could set LastLogonTimestamp values to future dates, skewing the calculations for the S-PwdLastSet-45 vulnerability detection. There was no specific vulnerability present; rather, it was a misconfiguration due to the incorrect timestamp.

## Solution
The customer was provided with several options to verify and correct the LastLogonTimestamp values. Ultimately, they resolved the issue independently by following the suggested steps, which included checking server time settings and potentially resetting LastLogonTimestamp values.

## Notes
- It is important to ensure that server time settings are accurate to prevent similar issues with LastLogonTimestamp in the future.
- Customers should be made aware of the potential for Windows bugs affecting timestamps and the need for regular checks on Active Directory attributes.