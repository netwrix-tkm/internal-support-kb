## Ticket Metadata
- **Ticket ID:** 500Qk00000NwXeOIAV
- **Case Number:** 441718
- **Status:** Closed - Resolved
- **Account/Company:** Renewbuy
- **Contact Name:** Anil Kumar
- **Product:** Netwrix Endpoint Protector
- **Component:** Client Upgrade
- **Feature:** Client Upgrade
- **Version:** 5941

## Problem Description
The customer requested assistance with upgrading all Windows and Linux (Ubuntu) machines simultaneously as a batch job. They also inquired about the availability of Linux client setups for various Ubuntu versions (12, 20, 21, 22, 23, and 24).

## Environment Details
- Operating Systems: Windows and various versions of Ubuntu (12, 20, 21, 22, 23, 24)
- Product Version: 5941

## Troubleshooting Steps
1. Confirmed that Windows upgrades can be performed directly from the EPP server using the System Configuration -> Client software upgrade.
2. Informed the customer that Linux upgrades are not supported directly through the EPP server and suggested using a third-party deployment tool.
3. Provided links to the required Ubuntu packages for versions 20.04, 22.04, 23.04, and 24.04.
4. Clarified that for Ubuntu versions 12 and 21, further details were needed to confirm support.
5. Suggested third-party tools for mass deployment, such as Chef, SaltStack, Ansible, and Puppet.
6. Addressed follow-up questions regarding user interaction for upgrades and uninstallation processes.

## Root Cause
The inability to perform batch upgrades for Linux machines directly through the EPP server is due to the current limitations of the software, which only supports bulk upgrades for Windows and Mac OS. Linux upgrades require third-party tools for deployment.

## Solution
The issue was resolved by:
- Providing the customer with the necessary links to download the Linux client setups for supported Ubuntu versions.
- Advising the use of third-party deployment tools for mass upgrades of Linux clients.
- Confirming that Windows and Mac OS upgrades can be performed without user interaction directly from the EPP server.

## Notes
- Future customers should be informed that Linux upgrades cannot be performed directly through the EPP server and must utilize third-party tools.
- Ensure to gather specific version details for unsupported Ubuntu versions to provide accurate support.
- It is important to clarify that deleting devices from the EPP server does not uninstall the client from the endpoint; manual uninstallation or a third-party tool is required for Linux clients.