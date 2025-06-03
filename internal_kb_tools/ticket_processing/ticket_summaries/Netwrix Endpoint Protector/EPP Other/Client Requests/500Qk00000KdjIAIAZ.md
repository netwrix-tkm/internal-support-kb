## Ticket Metadata
- **Ticket ID:** 500Qk00000KdjIAIAZ
- **Case Number:** 432215
- **Status:** Closed - Resolved
- **Account/Company:** IPRO SIA
- **Contact Name:** Elena Revzina
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Client Requests
- **Version:** None

## Problem Description
A customer reported an issue with the DPI (Data Loss Prevention) and DPI Allowlist for certain corporate web servers. When attempting to access a webpage from the DPI Allowlist, no certificate selection pop-ups appeared, preventing access. The webpage was using a Cososys Certificate that was not functioning, leading the customer to disable the DPI feature, which compromised their security policy.

## Environment Details
- The customer was using Netwrix Endpoint Protector (EPP).
- The issue arose despite no changes being made to the Netwrix EPP configuration.
- The customer had 24 Content Aware Protection (CAP) policies enforced on their endpoints.

## Troubleshooting Steps
1. Conducted a remote session with the customer to investigate the issue.
2. Noted that the DPI Allowlist was not selected in any of the 24 CAP policies.
3. Added the DPI Allowlist to one test CAP policy during the session.
4. Upgraded one user's Windows EPP client from version 6.2.3.1 to version 6.2.4.2.

## Root Cause
The root cause of the issue was identified as the DPI Allowlist not being selected in any of the enforced Content Aware Protection policies, which resulted in the absence of the certificate selection pop-up when accessing the allowed web pages.

## Solution
The issue was resolved by adding the DPI Allowlist to at least one Content Aware Protection policy. This change allowed the certificate selection pop-up to appear correctly, enabling access to the web pages from the Allowlist. The customer was advised to apply the Allowlist to other relevant CAP policies to ensure consistent functionality across all users.

## Notes
- The customer needs to ensure that the DPI Allowlist is included in at least one CAP policy that applies to all users to prevent similar issues in the future.
- It is important to monitor any changes in the configuration that may affect the functionality of the DPI feature and the associated policies.