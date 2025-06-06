## Ticket Metadata
- **Ticket ID:** 500Qk00000EXczJIAT
- **Case Number:** 418377
- **Status:** Closed - Resolved
- **Account/Company:** Optiv
- **Contact Name:** Robert Parsons
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** NEA Web Report Console
- **Version:** 11.6

## Problem Description
The customer, The Fresh Market, reported an issue where a user was shown to have "full control" permissions over Domain Admins in the Access Information Center's Object Permissions report, despite not having those permissions in Active Directory Users and Computers (ADUC).

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Product Version:** 11.6

## Troubleshooting Steps
1. Reviewed the Object Permissions report in the Access Information Center.
2. Cross-checked the reported permissions against the Active Directory Users and Computers (ADUC) for the user in question.
3. Investigated the discrepancies between the report and ADUC to identify potential causes.
4. Postponed the ticket to allow the customer time to complete a feature request form.

## Root Cause
The root cause of the issue was not explicitly identified during the troubleshooting process. The discrepancy between the Object Permissions report and ADUC may have been due to a synchronization issue or a reporting error within the Netwrix Enterprise Auditor.

## Solution
The issue was resolved by closing the ticket at the customer's request, as they were unable to complete the feature request form. No specific corrective action was taken regarding the permissions discrepancy.

## Notes
- It is important to verify the synchronization between the Netwrix Enterprise Auditor and Active Directory to prevent similar discrepancies in the future.
- Customers should be advised to regularly check permissions and reports for accuracy, especially when discrepancies are noted.
- Future cases involving permission discrepancies should include a thorough investigation of synchronization settings and report generation processes.