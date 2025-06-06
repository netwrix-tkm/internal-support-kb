```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000PcBdaIAF
- **Case Number:** 446276
- **Status:** Closed - Resolved
- **Account/Company:** LDS Infotech Pvt. Ltd
- **Contact Name:** Jitendra Gupta
- **Product:** Netwrix Endpoint Protector
- **Component:** System & Log Backups
- **Feature:** External Storage - FTP/Samba
- **Version:** Not specified

## Problem Description
The customer reported daily authentication failures (over 1200 logs) between their on-premise FTP server and the AWS EPP server, despite successful file transfers.

## Environment Details
- On-premise FTP server configured with shadow file server.
- EPP server hosted on AWS Cloud.
- SIEM integration configured, potentially contributing to authentication failures.

## Troubleshooting Steps
1. Reviewed the File Shadowing configuration and confirmed it was correct.
2. Analyzed FTP server logs to identify authentication failure sources.
3. Proposed a remote session to investigate the issue in real-time.
4. Identified that the File Shadows Repository configuration was not displaying expected indicators, suggesting a misconfiguration.
5. Investigated the possibility of authentication failures originating from the SIEM integration.
6. Suggested network connectivity tests (telnet, tcpdump) and log reviews (/var/eppfiles/syslog).
7. Recommended disabling SIEM integration, External Storage, and File Shadow Repository one at a time to isolate the source of failures.
8. Conducted a remote session to review configurations and logs in detail.

## Root Cause
The authentication failures were traced to a misconfiguration or outdated credentials in one of the integrations (likely related to the SIEM integration).

## Solution
The issue was resolved by reviewing and updating the configurations of the relevant integrations (File Shadow Repository, SIEM, and External Storage) in the EPP console. After making the necessary changes, the customer confirmed that authentication failure logs were no longer being generated on the FTP server.

## Notes
- Ensure that all credentials stored and used by the EPP server are correct and up to date.
- Check for any automated tasks, scripts, or legacy configurations that might be attempting to authenticate with outdated or incorrect credentials.
- Future cases should consider the impact of SIEM integrations on authentication processes.
```