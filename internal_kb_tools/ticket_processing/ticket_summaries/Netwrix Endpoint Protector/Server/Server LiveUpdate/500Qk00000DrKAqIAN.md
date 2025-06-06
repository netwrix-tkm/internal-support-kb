```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000DrKAqIAN
- **Case Number:** 416809
- **Status:** Closed - Resolved
- **Account/Company:** Geislinger GmbH
- **Contact Name:** Panagiotis Dragatis
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server LiveUpdate
- **Version:** 5.9.4.0

## Problem Description
The customer reported that backend updates were not applying on their server since May. Attempts to apply updates resulted in no changes, and the admin action log indicated that updates were not being installed.

## Environment Details
- Server Version: 5.9.4.0 (previously 5.9.3.0)
- Operating System: Ubuntu (specific version not mentioned)

## Troubleshooting Steps
1. Confirmed the server version and the issue's duration (several months).
2. Reviewed the admin action log for any indications of failed updates.
3. Attempted to apply backend updates through the admin interface, which resulted in no changes.
4. Scheduled a remote session to investigate the issue further.
5. Identified that the epp server did not reach the `ubunutkeyserver` to receive the apt key.

## Root Cause
The root cause was identified as the epp server's failure to connect to the `ubunutkeyserver`, preventing it from receiving the necessary apt key for updates.

## Solution
The issue was resolved by manually applying the apt key. Additionally, a procedure (referred to as procedure 60) was applied by the development team to ensure proper functionality.

## Notes
- It is important to monitor the server's ability to reach the key server to prevent similar issues in the future.
- Ensure that the apt key is updated manually if automatic updates fail.
- Regular checks on the admin action log can help identify issues early.
```