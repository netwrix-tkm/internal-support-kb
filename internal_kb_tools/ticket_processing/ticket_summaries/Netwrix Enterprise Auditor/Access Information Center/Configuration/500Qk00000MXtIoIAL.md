## Ticket Metadata
- **Ticket ID:** 500Qk00000MXtIoIAL
- **Case Number:** 437674
- **Status:** Closed - Resolved
- **Account/Company:** GroupM
- **Contact Name:** Vinay Singh
- **Product:** Netwrix Enterprise Auditor
- **Component:** NEA Web Console
- **Feature:** Configuration
- **Version:** 11.6

## Problem Description
The customer requested assistance with updating the site certificates for the Netwrix Enterprise Auditor (NEA) Web Console before the deadline of March 12, 2025.

## Environment Details
- **Server:** NEA server
- **Certificate Store:** LocalMachineMy
- **Port:** 443

## Troubleshooting Steps
1. The customer received the renewed certificate and scheduled a call with support to proceed with the update.
2. The support team provided guidance based on the article from the Netwrix Help Center: [Securing the Web Console](https://helpcenter.netwrix.com/bundle/EnterpriseAuditor_11.6/page/Content/EnterpriseAuditor/Install/Application/Reports/Secure.htm).
3. The new certificate was imported into the LocalMachineMy store on the NEA server.
4. The certificate binding for port 443 on the NEA server was updated accordingly.
5. The customer was advised to test the NEA Web Console for a few days to ensure functionality.

## Root Cause
The issue stemmed from the need to update the NEA Web Console certificates to maintain secure connections, as the existing certificates were nearing expiration.

## Solution
The issue was resolved by successfully importing the renewed certificate into the LocalMachineMy store on the NEA server and updating the certificate binding for port 443. The customer confirmed that the update was completed successfully and requested to close the ticket.

## Notes
- Ensure that certificate updates are scheduled well in advance of expiration dates to avoid service interruptions.
- Always refer to the official Netwrix Help Center documentation for the most accurate and detailed instructions regarding certificate management and updates.