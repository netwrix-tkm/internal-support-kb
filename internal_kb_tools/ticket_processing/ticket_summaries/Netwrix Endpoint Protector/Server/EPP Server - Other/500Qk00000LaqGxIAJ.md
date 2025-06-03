```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000LaqGxIAJ
- **Case Number:** 435029
- **Status:** Closed - Resolved
- **Account/Company:** Regina Maria
- **Contact Name:** Cristian Voicu
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Server - Other
- **Feature:** Other
- **Version:** 5.9.4.1 (Server), 6.2.4.2 (Client)

## Problem Description
The customer reported that they were unable to delete Shadow files through the File Maintenance section of the Netwrix Endpoint Protector web interface. The interface would freeze, and no files were deleted, regardless of whether the deletion was attempted in bulk or individually.

## Environment Details
- Server Version: 5.9.4.1
- Client Version: 6.2.3.1006 (previous), 6.2.4.2 (new)
- Files stored locally on the server
- No load balancer or proxy server in use

## Troubleshooting Steps
1. Attempted to delete Shadow files both in bulk and one by one.
2. Observed that the web interface froze during these attempts.
3. Uninstalled the previous EPP client version (6.2.3.1006) and restarted the system.
4. Installed the new EPP client version (6.2.4.2).
5. Used the setserver IP tool to manually set the EPP Server IP address and hostname.
6. Re-registered the endpoint client.
7. Collected diagnostics from the EPP Server UI.

## Root Cause
The issue was identified as being related to missing Global Sign certificates on the user's machine, which affected the functionality of the EPP client notifier.

## Solution
The issue was resolved by installing the missing Global Sign certificates on the user's machine. After the installation, the EPP client notifier began functioning correctly, allowing the customer to manage their Shadow files as intended.

## Notes
- Ensure that all necessary certificates are installed on client machines to prevent similar issues in the future.
- Regularly check for updates and compatibility between the EPP client and server versions to maintain optimal functionality.
```