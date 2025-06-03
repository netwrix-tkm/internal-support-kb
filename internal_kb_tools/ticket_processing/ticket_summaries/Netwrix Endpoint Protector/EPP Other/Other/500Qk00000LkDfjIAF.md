## Ticket Metadata
- **Ticket ID:** 500Qk00000LkDfjIAF
- **Case Number:** 435420
- **Status:** Closed - Resolved
- **Account/Company:** Solar Atmospheres, Inc.
- **Contact Name:** Lawrence Yeziorski
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Other
- **Version:** 5.9.4.1

## Problem Description
The customer reported that sessions in the web portal were consistently ending in Chrome without notification, requiring a page refresh to regain access. This issue occurred while actively navigating the portal and prevented changes from being saved.

## Environment Details
- The web portal is hosted on-premises.
- The issue was specific to the Chrome browser; Edge was used as a workaround without issues.

## Troubleshooting Steps
1. Conducted a remote session to perform resource optimization procedures.
2. Increased PHP memory from 256MB to 512MB during a subsequent remote session.
3. Gathered details about the server environment to investigate potential causes.

## Root Cause
The root cause of the session expiration issue was identified as insufficient PHP memory allocation, which led to session handling problems in the Chrome browser.

## Solution
The issue was resolved by increasing the PHP memory limit from 256MB to 512MB. After this adjustment, the customer reported that the session expiration issue could no longer be reproduced.

## Notes
- It is advisable to monitor the PHP memory settings in environments where session handling issues are reported.
- If similar issues arise in the future, consider checking browser compatibility and memory allocation settings as initial troubleshooting steps.