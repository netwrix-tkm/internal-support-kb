```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000CmXaiIAF
- **Case Number:** 414322
- **Status:** Closed - Resolved
- **Account/Company:** Ernst & Young Global Services LLP
- **Contact Name:** Alif Wahid
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Server
- **Feature:** Other
- **Version:** Not specified

## Problem Description
The customer reported that they were unable to log in and ping both EPP servers, indicating that the servers were down.

## Environment Details
- The issue occurred in a corporate environment managed by Ernst & Young Global Services LLP.
- The servers were configured to use different ports for UI access and Client-Server communication.

## Troubleshooting Steps
1. Initial contact was made by the customer to report the issue.
2. A remote session was scheduled to investigate the problem.
3. During the session, it was identified that the SSL certificate update might have caused issues with the Nginx configuration.
4. The Nginx configuration file was checked and found to have incorrect settings due to the SSL certificate update.
5. The server was restarted, which led to the Nginx config file being automatically updated but incorrectly due to the custom port settings.
6. The support team replaced the SSL certificates and manually updated the Nginx configuration file to resolve the issue.

## Root Cause
The root cause of the issue was identified as a misconfiguration in the Nginx settings following an SSL certificate update. The update broke the Nginx configuration, preventing the Nginx service from starting correctly. The server reboot led to an automatic update of the Nginx config file, which did not account for the custom ports used for UI and Client-Server communication.

## Solution
The issue was resolved by:
- Replacing the SSL certificates.
- Manually updating the Nginx configuration file to ensure it correctly reflected the custom port settings for both UI access and Client-Server communication.

## Notes
- It is crucial to notify the support team prior to any SSL certificate updates to ensure all necessary changes to the Nginx configuration are made to prevent similar issues in the future.
- Customers should be advised to check their Nginx configuration after any certificate updates or server reboots to ensure proper functionality.
```