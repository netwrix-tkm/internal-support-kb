## Ticket Metadata
- **Ticket ID:** 500Qk00000JkefUIAR
- **Case Number:** 430472
- **Status:** Closed - Resolved
- **Account/Company:** Niagara County
- **Contact Name:** Jeremy Stauder
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Credentials
- **Version:** 17.1

## Problem Description
The customer reported an issue where they were unable to use Windows login credentials to authenticate to the Netwrix Stealth Audit platform. Instead of logging in, they were prompted for a username and password, which were not accepted. They could log into the AIC but not the main audit web application.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Access Port:** 8082

## Troubleshooting Steps
1. Verified that the user could log into the AIC without issues.
2. Checked if the site was added to the local intranet zones as per the guidance provided in the documentation.
3. Investigated browser settings and cache for any stored credentials.
4. Attempted to clear browser cache and cookies to see if it resolved the login issue.

## Root Cause
The issue was identified as being caused by credentials that were stuck in the browser's cache, preventing successful authentication.

## Solution
To resolve the issue, the Single Sign-On (SSO) configuration was removed through the browser settings in the Netwrix Enterprise Auditor. After this adjustment, the user was able to log in successfully using their Windows credentials. The customer preferred to keep the SSO disabled, so it was left in that state.

## Notes
- Ensure that users clear their browser cache if they encounter similar login issues in the future.
- It may be beneficial to remind users to check their SSO settings and local intranet zone configurations when facing authentication problems.