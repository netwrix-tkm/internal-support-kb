## Ticket Metadata
- **Ticket ID:** 500Qk00000LqJViIAN
- **Case Number:** 435746
- **Status:** Closed - Resolved
- **Account/Company:** ENGIE Information et Technologies, SA
- **Contact Name:** Jean-Christophe Perez-galiano
- **Product:** PingCastle
- **Component:** PC Enterprise
- **Feature:** PingCastle General
- **Version:** 3.3

## Problem Description
The customer needed a more efficient method to assign roles to multiple users across one or more domains when managing a new Active Directory domain, as the current process required assigning roles individually.

## Environment Details
- Active Directory domain management
- Claims-based authentication and API usage were considered for role assignment.

## Troubleshooting Steps
1. Discussed the current manual process of assigning roles one by one.
2. Recommended using claims-based authentication to streamline user role management.
3. Suggested creating a group in Active Directory or an identity provider for SAML/OpenID Connect.
4. Provided instructions for API usage, including:
   - Creating users via the API.
   - Retrieving all domains users need access to.
   - Granting authorization for those domains via the API.
5. Followed up with the customer multiple times to check on progress and offer further assistance.

## Root Cause
The inefficiency stemmed from the manual assignment of roles to users, which was time-consuming and prone to errors when managing multiple users across domains.

## Solution
The issue was resolved by recommending the use of claims-based authentication, which allows for:
- Creating a group in Active Directory or an identity provider.
- Adding users to the group and granting access through the console.
- For API users, ensuring that users are created first, retrieving necessary domains, and granting authorization efficiently.

## Notes
- Future implementations should consider developing an API that allows for bulk role assignments to improve efficiency.
- It is important to ensure that permissions are set at the entity level and that domains are assigned correctly to avoid access issues.
- Customers should be informed about the potential inefficiencies of using the API for authorization if not properly configured.