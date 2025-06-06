## Ticket Metadata
- **Ticket ID:** 500Qk00000EzZbzIAF
- **Case Number:** 419290
- **Status:** Closed - Resolved
- **Account/Company:** Regions Bank
- **Contact Name:** Jim Callison
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Initial setup
- **Version:** 11.6

## Problem Description
The customer reported an "Access Denied" error when attempting to set a profile connection using a Group Managed Service Account (gMSA). The gMSA account was already configured to run SQL services on the server, but the connection profile setup was failing due to permissions issues.

## Environment Details
- **Product Version:** 11.6
- **Collector Code:** StealthAUDIT General
- **Age:** 10.2

## Troubleshooting Steps
1. Verified that the gMSA account was correctly configured at the server level.
2. Checked permissions on the StealthAUDIT folders to ensure the gMSA account had full control.
3. Investigated the permissions of the account used to run the Netwrix Enterprise Auditor (NEA) service.
4. Reviewed documentation related to gMSA configuration for any overlooked steps.

## Root Cause
The root cause of the issue was identified as the account used to run the NEA service lacking the necessary permissions to read the gMSA password. This prevented the successful addition of the gMSA to the connection profile.

## Solution
To resolve the issue, the following command was executed to grant the NEA service account the required permissions to retrieve the gMSA password:

```powershell
Set-ADServiceAccount -Identity %GMSA% -DNSHostName %GMSA.DOMAIN% -PrincipalsAllowedToRetrieveManagedPassword %NEA SERVER%$, %ADMIN ACCOUNT%
```

After executing this command, the permissions were correctly set, allowing the NEA service account to access the gMSA password and successfully add the gMSA to the connection profile.

## Notes
- Ensure that the account running the NEA service has the appropriate permissions to access the gMSA password in future setups.
- Refer to the official documentation for gMSA configuration for detailed steps and best practices: [Netwrix Help Center - gMSA Configuration](https://helpcenter.netwrix.com/bundle/StealthAUDIT_11.5/page/Content/StealthAUDIT/Chapters/03.Global_Settings/Custom_Credentials/gMSA_Configuration.htm).