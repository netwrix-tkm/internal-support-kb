```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000OOoaYIAT
- **Case Number:** 443032
- **Status:** Closed - Resolved
- **Account/Company:** Rstack Solutions Private Solutions
- **Contact Name:** Devendra Reddy
- **Product:** Netwrix Endpoint Protector
- **Component:** Active Directory Sync
- **Feature:** AD Sync Error
- **Version:** NONE

## Problem Description
The customer reported an issue with Active Directory synchronization after moving their DLP VM to a VNET with a Site-to-Site tunnel setup to their on-premises domain controller. They were unable to establish a connection for AD sync with the EPP server.

## Environment Details
- The DLP server is hosted on Azure.
- A Site-to-Site tunnel is established between the Azure environment and the on-premises domain controller.
- The customer attempted to connect via Directory Services -> Microsoft Active Directory.

## Troubleshooting Steps
1. Verified connectivity from the DLP appliance to the domain controller using SSH and telnet commands.
2. Checked firewall settings to ensure port 3389 was allowed for the domain controller's internal IP.
3. Followed instructions from the Netwrix help center regarding Active Directory synchronization.
4. Attempted to set up the connection multiple times, encountering errors such as "Invalid Credentials" and "Can't contact LDAP Server."
5. Conducted a remote session with the client to gather more details and troubleshoot further.

## Root Cause
The issue was primarily due to incorrect configuration settings in the Active Directory synchronization setup, including potential permission issues and incorrect Organizational Unit (OU) details.

## Solution
The issue was resolved by:
- Enabling and configuring the Active Directory settings correctly.
- Ensuring the client had the necessary permissions to perform synchronization tasks.
- Correctly specifying the OU in the format: `DC=rstacksolutions,DC=com,OU=RSTACK-USERS`.

After these adjustments, the AD was successfully synchronized with the EPP server.

## Notes
- Ensure that the client has the appropriate permissions for synchronization tasks in future cases.
- Verify that the correct ports are open and that the OU details are formatted correctly.
- Allow sufficient time (minimum of 6 hours) for synchronization processes to complete after configuration changes.
```