## Ticket Metadata
- **Ticket ID:** 500Qk00000OOzyzIAD
- **Case Number:** 443051
- **Status:** Closed - Resolved
- **Account/Company:** MISO Energy
- **Contact Name:** Michael Stephenson
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Active Directory
- **Feature:** Credentials
- **Version:** 11.6

## Problem Description
The customer reported issues with domain controller host discovery in a production environment. They created a new discovery query for a non-primary domain, which successfully connected. However, this caused the service account used for collecting data from the primary domain to lock out, necessitating the deletion of the new job to unlock the account.

## Environment Details
- **Production Environment:** The domain being connected to cannot be accessed from lower environments.
- **Service Account:** Used for collecting data across multiple domains.

## Troubleshooting Steps
1. Confirmed the exact time and location of the account lockout.
2. Clarified whether the issue was related to the Active Directory Inventory (ADI) job or a host discovery job.
3. Investigated the use of a connection profile with multiple credentials.
4. Discussed the importance of properly scoping the discovery to avoid account lockouts.

## Root Cause
The root cause of the account lockout was not definitively identified. However, it was suggested that improper scoping of the discovery query may have contributed to the issue, potentially causing the service account to attempt unauthorized access.

## Solution
The issue was resolved by successfully running the host discovery for both `MI_DOMAIN_CONTROLLER_CPROD` and `MI_DOMAIN_CONTROLLERS` during a support call. The new discovery query was deleted to unlock the service account, allowing the original query to function again without further issues.

## Notes
- It is crucial to ensure that discovery queries are properly scoped to prevent unintended account lockouts in production environments.
- Future attempts to connect to multiple domains should be carefully managed, especially in production settings, to avoid similar issues.
- Always enable DEBUG logging when running jobs to capture detailed logs that may assist in troubleshooting.