## Ticket Metadata
- **Ticket ID:** 500Qk00000KOeLmIAL
- **Case Number:** 431539
- **Status:** Closed - Resolved
- **Account/Company:** Great Eastern Life Assurance (Malaysia) Berhad
- **Contact Name:** MOHD HASBUL HAFIZ MAT HASSAN
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** NEA Web Report Console
- **Version:** 11.0

## Problem Description
The customer requested the replacement of an SSL certificate for the Netwrix Enterprise Auditor (StealthAUDIT) server, which was previously inaccessible.

## Environment Details
- **Server URL:** [https://PWDADAPG-884.ap.lifeisgreat.net:8082](https://PWDADAPG-884.ap.lifeisgreat.net:8082)
- **Product Version:** 11.0
- **Build Number:** 11.0.1221.1018

## Troubleshooting Steps
1. Confirmed the need for SSL certificate replacement due to server inaccessibility.
2. Reviewed relevant documentation for SSL certificate installation and replacement.
   - [Securing the Web Console](https://helpcenter.netwrix.com/bundle/EnterpriseAuditor_11.6/page/Content/EnterpriseAuditor/Install/Application/Reports/Secure.htm)
   - [Add a new certificate for the StealthAUDIT web reports port](https://helpcenter.netwrix.com/bundle/z-kb-articles-salesforce/page/kA04u0000000ITtCAM.html)
3. Conducted a meeting to discuss the SSL certificate replacement process.

## Root Cause
The server was initially inaccessible due to an expired or improperly configured SSL certificate, necessitating a replacement.

## Solution
The issue was resolved by following the guidelines provided in the knowledge base article for replacing the SSL certificate. The customer successfully installed the new SSL certificate, restoring access to the server.

## Notes
- Ensure that SSL certificates are regularly monitored and renewed to prevent server inaccessibility.
- Refer to the provided knowledge base articles for detailed steps on SSL certificate management in the future.