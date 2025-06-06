## Ticket Metadata
- **Ticket ID:** 500Qk00000JPZqsIAH
- **Case Number:** 429648
- **Status:** Closed - Resolved
- **Account/Company:** Great Eastern Life Assurance (Malaysia) Berhad
- **Contact Name:** MOHD HASBUL HAFIZ MAT HASSAN
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** NEA Web Report Console
- **Version:** 11.0

## Problem Description
The IDM Team was unable to log in to the StealthAUDIT system using the local username `PCDAAIDMR01`, which was created to reset and maintain user access. The issue arose because this username existed only in the Local Active Directory (AD) and not within the StealthAUDIT system.

## Environment Details
- Local user account created in Local AD.
- Attempted access to the StealthAUDIT Reporting Module and StealthDefend.

## Troubleshooting Steps
1. Created a local user account `PCDAAIDMR01`.
2. Added the user to the Local Administrators group.
3. Attempted to log in to the Web console of the NTM and NEA Reports module.
4. Discussed access issues in meetings with the IDM team and attempted to troubleshoot connectivity issues.
5. Identified that internal connectivity issues and CyberArk problems were preventing access to the server.

## Root Cause
The root cause of the issue was identified as a configuration error: local accounts are not authorized to log in to the StealthAUDIT web portals. Only Active Directory user accounts with the required roles can access these systems.

## Solution
The resolution involved informing the customer that they needed to provision an Active Directory user account to gain access to the reporting module. The local user account `PCDAAIDMR01` was not sufficient for login. The customer was advised to create an AD account and verify functionality thereafter.

## Notes
- Local user accounts cannot be used to log in to the StealthAUDIT Reporting Module or StealthDefend.
- Ensure that any user requiring access to these systems is provisioned with an Active Directory account and assigned the necessary roles.
- Future troubleshooting should include verifying user account types and their permissions in relation to the systems being accessed.