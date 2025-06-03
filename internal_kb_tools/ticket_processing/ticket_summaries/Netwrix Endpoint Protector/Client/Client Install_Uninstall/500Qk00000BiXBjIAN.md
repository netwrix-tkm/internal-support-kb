```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000BiXBjIAN
- **Case Number:** 411649
- **Status:** Closed - Resolved
- **Account/Company:** Service-now.com
- **Contact Name:** Samuel Seitz
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Install/Uninstall
- **Version:** 2.4.2

## Problem Description
The customer reported issues deploying version 2.4.2 of the Netwrix Endpoint Protector to RHEL 8 machines. The Puppet team indicated they were unable to set an environment variable at runtime, which resulted in the EPP agent not checking in properly. The `options.ini` file was not being populated correctly and was being wiped out upon daemon restarts.

## Environment Details
- Operating System: RHEL 8
- EPP Version: 2.4.2

## Troubleshooting Steps
1. Requested the `set_epp_client_server.sh` script referenced in the documentation.
2. Inquired if it was possible to install and point the client at a server without setting the environment variable.
3. Provided instructions on configuring the `options.sh` script to set the necessary parameters for the EPP client.

## Root Cause
The issue was identified as a misconfiguration related to the environment variables required for the EPP client to function correctly. The `options.sh` script needed to be properly edited to include the server details.

## Solution
The support engineer provided the following steps to resolve the issue:
1. Instructed the customer to edit the `options.sh` script after downloading and extracting the client:
   - Remove the `#` from the lines for `EPPCLIENT_WS_SERVER`, `EPPCLIENT_WS_PORT`, and `EPPCLIENT_DEPARTMENT_CODE`.
   - Replace the placeholder "set.this.to.the.endpointprotector.server.com" with the actual EPP server IP.
2. Advised to save the changes and install the EPP client using the `install.sh` file.
3. Clarified that the `set_epp_client_server.sh` script was not necessary, as the `options.sh` script contained all required configurations.

## Notes
- Ensure that the `options.sh` script is correctly configured before installation to avoid similar issues in the future.
- If using a FAT client, the installation process remains the same, but it is essential to follow the README.txt for any specific commands related to that version.
- Be aware that email security tools may strip attachments; consider alternative methods for sharing files if necessary.
```