```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000CEnlDIAT
- **Case Number:** 412847
- **Status:** Closed - Resolved
- **Account/Company:** The Fresh Market
- **Contact Name:** Robert Parsons
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** NEA Web Report Console
- **Version:** 11.6.0.79

## Problem Description
The customer reported that after installing the Netwrix Enterprise Auditor (NEA), they were unable to access the published reports page, receiving a message indicating that the page could not be reached.

## Environment Details
- The installation was a new deployment of Netwrix Enterprise Auditor (NEA) version 11.6.0.79.
- The service was configured to run under a service account.

## Troubleshooting Steps
1. Verified that the service was running.
2. Added local firewall rules for port 8082.
3. Changed the web server service to run as a service account and restarted the service.
4. Attempted to generate a self-signed certificate and set up SSL, followed by restarting the web server.
5. Checked the listening ports to confirm that port 8082 was not active.
6. Suggested changing the port to 8084 in the web configuration as a temporary workaround.

## Root Cause
The issue was identified as being caused by the service account not having local administrator privileges, which resulted in an "Access Denied" error when attempting to start the service.

## Solution
The resolution involved granting local administrator rights to the service account. Once this was corrected, the published reports page was accessible without issue.

## Notes
- Ensure that service accounts have the necessary permissions, especially local admin rights, to avoid similar access issues in the future.
- For future deployments, verify firewall settings and service account permissions before installation to prevent access issues.
- Consider moving to HTTPS for enhanced security, following the provided instructions for SSL certificate configuration.
```