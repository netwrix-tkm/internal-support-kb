## Ticket Metadata
- **Ticket ID:** 500Qk00000KvjphIAB
- **Case Number:** 433146
- **Status:** Closed - Resolved
- **Account/Company:** Toyota Boshoku
- **Contact Name:** TBEU ITSupport
- **Product:** Netwrix Enterprise Auditor
- **Component:** Access Information Center
- **Feature:** Configuration
- **Version:** 11.6

## Problem Description
The customer reported that the Netwrix Access Information Center (AIC) was not functioning, and they were unable to log in to the portal after attempting to upgrade to the latest version. The error message displayed was: "Unable to use to the SQL Server Database provided."

## Environment Details
- The issue occurred after an upgrade of the Netwrix Enterprise Auditor.
- The customer was using version 11.6 of the software.

## Troubleshooting Steps
1. Attempted to uninstall and reinstall the Access Information Center (AIC).
2. Checked the SSL certificate for any changes; none were found.
3. Stopped and restarted the AIC service, which resulted in the client being unable to connect to the SQL database.
4. Reviewed previous cases for similar issues and resolutions.

## Root Cause
The issue was determined to be related to SSL certificate bindings for the Access Information Center and the Published Reports Web console. The SSL certificate bindings needed to be reapplied and updated.

## Solution
The issue was resolved by reapplying the SSL certificate bindings using the command prompt with elevated privileges. The following commands were used:

```bash
netsh http show sslcert
netsh http del sslcert ipport=0.0.0.0:8082
netsh http add sslcert ipport=0.0.0.0:8082 appid=<appid> certhash=<certhash>
```

- The `<appid>` and `<certhash>` values were replaced with the appropriate application GUID and certificate thumbprint, respectively.
- Documentation on this process was provided to the customer for future reference: [Securing the Access Information Center](https://helpcenter.netwrix.com/bundle/AIC_11.6/page/Content/Access/InformationCenter/Installation/Secure.htm).

## Notes
- It is important to ensure that SSL certificate bindings are correctly configured after upgrades to prevent similar issues.
- If the AIC continues to experience connectivity issues, further investigation into the SSL certificate bindings may be necessary.