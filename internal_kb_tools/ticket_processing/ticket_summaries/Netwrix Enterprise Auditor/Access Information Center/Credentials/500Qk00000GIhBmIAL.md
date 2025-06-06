## Ticket Metadata
- **Ticket ID:** 500Qk00000GIhBmIAL
- **Case Number:** 422225
- **Status:** Closed - Resolved
- **Account/Company:** Alpine Bank
- **Contact Name:** Luke Brackin
- **Product:** Netwrix Enterprise Auditor
- **Component:** Access Information Center
- **Feature:** Credentials
- **Version:** 11.6

## Problem Description
The customer reported an error when attempting to access the Access Information Center (AIC). Initially, the error indicated a failure to connect to Active Directory (AD), and subsequently, it changed to "An unknown error has occurred while logging in." The issue coincided with recent password updates for two service accounts.

## Environment Details
- **Netwrix Enterprise Auditor (NEA) Version:** 11.6.0.58
- **NEA Access Information (AIC) Version:** 11.6.0.9
- **SQL Server and Application Server** are part of the environment.

## Troubleshooting Steps
1. Reviewed the error messages and confirmed the recent password updates for service accounts.
2. Consulted relevant knowledge base articles regarding updating credential passwords and Active Directory service account passwords.
3. Attempted to re-enable the built-in AIC Admin account via SQL Server.
4. Executed SQL queries to check the status of the AIC Admin account and update its status if necessary.
5. Updated the AD connection account and confirmed the Admin Group functionality.

## Root Cause
The issue was caused by the recent password updates for the service accounts used to connect to Active Directory. The AIC was unable to authenticate due to the outdated credentials.

## Solution
The resolution involved:
- Re-enabling the built-in AIC Admin account using SQL Server commands.
- Updating the Active Directory service account password in the AIC configuration.
- Confirming that the Admin Group was functioning correctly after the updates.

The following SQL command was used to re-enable the AIC built-in Admin account:
```sql
UPDATE SA_AIC_Authentication
SET IsEnabled = 1
WHERE TrusteeSID = 'X-1-1-0'
```

## Notes
- It is important to update the service account credentials in both the AIC and the Netwrix Enterprise Auditor whenever passwords are changed.
- Future password updates may require similar steps to ensure connectivity to Active Directory.
- Always refer to the relevant knowledge base articles for guidance on updating credentials and troubleshooting access issues.