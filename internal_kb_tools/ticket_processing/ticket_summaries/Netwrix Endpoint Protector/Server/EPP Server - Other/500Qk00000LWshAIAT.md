## Ticket Metadata
- **Ticket ID:** 500Qk00000LWshAIAT
- **Case Number:** 434805
- **Status:** Closed - Resolved
- **Account/Company:** Walt Disney Pictures
- **Contact Name:** Guill Espinosa
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** Not specified

## Problem Description
The customer reported an issue with configuring External Storage Settings for SMB access to an external network storage. They received an error message stating, "Could not connect to network share. Please check the credentials and server settings," while attempting to connect from one EPP server, despite using the same credentials and mount point that worked on another EPP server.

## Environment Details
- The EPP server was recently migrated and rebuilt on a new network with a new configuration.
- The SMB path provided by the customer was: `//storage.mando.studio.disney.com/tsedata/EPP/KLSSY6YPfiles`
- Samba and CIFS were verified to be installed on the backend server.

## Troubleshooting Steps
1. Verified that the SMB path was accessible and open.
2. Attempted to connect using both the hostname and IP address of the external storage.
3. Checked the settings and mount point format on the old EPP server.
4. Conducted a telnet test from the EPP server backend to the external storage, which failed.
5. Followed up with the customer regarding the SMB version in use and the configuration of Access Control Lists (ACLs).
6. Scheduled remote sessions to further investigate the issue.

## Root Cause
The issue was identified as a configuration mismatch related to the authentication security settings on the new EPP server. The customer was using NTLM authentication, which was incompatible with the external storage configuration.

## Solution
The connection issue was resolved when the customer changed the Authentication security setting from NTLM to NTLMSSP. This adjustment allowed the same parameters and credentials to successfully connect to the external storage on the new network.

## Notes
- Ensure that authentication settings are compatible with the external storage configuration when migrating or rebuilding servers.
- The customer expressed interest in using NFS as an external storage type for future releases, which may require additional considerations for compatibility and configuration.