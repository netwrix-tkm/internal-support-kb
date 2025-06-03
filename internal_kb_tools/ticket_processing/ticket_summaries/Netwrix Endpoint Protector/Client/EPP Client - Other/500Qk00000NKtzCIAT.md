## Ticket Metadata
- **Ticket ID:** 500Qk00000NKtzCIAT
- **Case Number:** 439975
- **Status:** Closed - Resolved
- **Account/Company:** VicCnS Co.,Ltd.
- **Contact Name:** kwangjae shin
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** EPP Client - Other
- **Version:** NONE

## Problem Description
The customer inquired about a command to manually update the EndpointProtector Client policy on an Ubuntu 24.04 system running through WSL in a Windows environment, as they preferred not to rely on automatic policy updates.

## Environment Details
- **Operating System:** Ubuntu 24.04
- **Environment:** Windows Subsystem for Linux (WSL)

## Troubleshooting Steps
1. Confirmed the existence of a command for manually updating the policy.
2. Suggested restarting the EndpointProtector client service as an alternative method.

## Root Cause
It was determined that there is currently no command available for manually updating the EndpointProtector Client policy via the command line interface (CLI).

## Solution
The support engineer provided the following command to restart the EndpointProtector client service, which would effectively refresh the policy:
```bash
sudo service epp-client-daemon restart
```
This command serves as a workaround to ensure the client retrieves the latest policy from the server.

## Notes
- Customers should be aware that the absence of a CLI command for manual policy updates may limit their control over policy management.
- Restarting the client service is a temporary solution and may not be suitable for all environments; users should consider their operational requirements before implementing this workaround.