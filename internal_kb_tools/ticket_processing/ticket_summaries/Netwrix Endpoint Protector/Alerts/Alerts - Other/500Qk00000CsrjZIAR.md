## Ticket Metadata
- **Ticket ID:** 500Qk00000CsrjZIAR
- **Case Number:** 414616
- **Status:** Closed - Resolved
- **Account/Company:** Outcomes Matter Innovations
- **Contact Name:** George Chiligiris
- **Product:** Netwrix Endpoint Protector
- **Component:** Alerts
- **Feature:** Alerts - Other
- **Version:** 5.9.2.0 (server), 6.2.1.2 (clients)

## Problem Description
The customer reported concerns regarding the security advisory ADV-2024-002 related to remote code execution vulnerabilities in CoSoSys Endpoint Protector and CoSoSys Unify. They wanted to confirm if their hosted server was upgraded to the correct version and if all recent patches were applied. Additionally, they noted discrepancies in the Content Aware Report, where events were incorrectly associating users with computers.

## Environment Details
- Hosted environment running version 5.9.2.0.
- Client systems running version 6.2.1.2.

## Troubleshooting Steps
1. Customer provided a screenshot from the Dashboard showing the current updates.
2. Support requested confirmation of the hotfix version applied (1.0 or 1.1).
3. Support advised the customer to apply the EPP Server Hotfix #1.1 and provided instructions on how to do so.
4. Customer was informed that the 5.9.3.0 server update was not mandatory for applying the hotfix but recommended for security.
5. Customer applied the 5.9.3.0 update and hotfix 1.1 as per support's guidance.
6. Customer sent a follow-up screenshot to confirm that all necessary updates were applied.

## Root Cause
The initial issue stemmed from the server running an outdated version (5.9.2.0) that had not received the latest security patches, leading to potential vulnerabilities. Additionally, the incorrect user/computer associations in reports were likely due to the outdated software and recent hotfix application.

## Solution
The issue was resolved by:
1. Applying the EPP Server update to version 5.9.3.0.
2. Applying the EPP Server Hotfix #1.1.
3. Confirming through screenshots that all necessary security updates were in place.

## Notes
- It is crucial for hosted environments to regularly check for updates and apply them promptly to mitigate security vulnerabilities.
- Customers should be advised to take snapshots of their servers before applying major updates, even in hosted environments, to ensure they can revert if necessary.
- Future inquiries regarding report discrepancies should include checks on the version and recent updates applied to the software.