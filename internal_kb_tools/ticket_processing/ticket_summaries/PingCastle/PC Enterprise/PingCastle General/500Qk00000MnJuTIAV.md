## Ticket Metadata
- **Ticket ID:** 500Qk00000MnJuTIAV
- **Case Number:** 438367
- **Status:** Closed - Resolved
- **Account/Company:** Würth IT GmbH
- **Contact Name:** Corvin Schmid
- **Product:** PingCastle
- **Component:** PC Enterprise
- **Feature:** PingCastle General
- **Version:** 3.3

## Problem Description
The customer was configuring SAML authentication for their PingCastle Enterprise instance using Ping Identity as the Identity Provider (IdP). They required clarification on supported attributes and the process for creating the Service Provider (SP) Metadata XML file, as the official documentation was insufficient.

## Environment Details
- **Identity Provider:** Ping Identity
- **Application:** PingCastle Enterprise
- **Authentication Method:** SAML

## Troubleshooting Steps
1. Attempted to configure PingCastle Enterprise for SAML authentication.
2. Checked available attributes that PingCastle can utilize (Username, Email, Group Membership).
3. Searched for an option in PingCastle to automatically generate an SP Metadata XML file.
4. Manually configured SAML authentication by editing `appsettings.Production.json` with the provided Ping Identity metadata URL.
5. Restarted PingCastle services or performed an IISRESET.
6. Attempted a test login via SAML and checked for authentication failures.
7. Inspected browser developer tools and server logs for potential errors.

## Root Cause
The issue stemmed from a lack of clarity in the documentation regarding the required attribute mappings and the manual configuration needed for the SP Metadata XML file. Additionally, the IdPMetadata URL was not initially accessible from the PingCastle server, which contributed to authentication failures.

## Solution
SAML authentication for PingCastle Enterprise was successfully implemented by:
- Correctly mapping the necessary attributes (Username, Email, Group Membership) in Ping Identity.
- Manually configuring the `appsettings.Production.json` file with the correct IdP metadata URL.
- Ensuring the IdPMetadata URL was accessible from the PingCastle server.
- Restarting the PingCastle services, which allowed for successful authentication testing.

## Notes
- PingCastle does not automatically generate an SP Metadata XML file; manual configuration is required.
- Claims sent from Ping Identity must match the expected attributes for successful authentication.
- Debugging should include checking logs and browser developer tools to ensure correct claim mapping.
- Future users should ensure that the IdPMetadata URL is reachable from the PingCastle server to avoid similar issues.