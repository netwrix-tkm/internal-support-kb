## Ticket Metadata
- **Ticket ID:** 500Qk00000MDfTkIAL
- **Case Number:** 436699
- **Status:** Closed - Resolved
- **Account/Company:** Arista Networks, Inc.
- **Contact Name:** Bharani M
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** 5941

## Problem Description
The customer set up a new GCP image of the EPP server in a staging environment and was unable to access the UI via DNS, although access was successful using the server's IP address.

## Environment Details
- Staging server upgraded from version 5810 to 5941.
- Migration performed from the production server to the new staging server using System Backup V2.

## Troubleshooting Steps
1. Attempted to access the EPP server using the IP address, which was successful.
2. Identified that the issue likely stemmed from DNS configuration, as access via DNS was not functioning.
3. Confirmed that the staging server appeared to be operational and correctly configured.

## Root Cause
The issue was determined to be related to DNS configuration, which prevented access to the EPP server via its DNS name.

## Solution
The problem was resolved by confirming the DNS settings and ensuring that the necessary certificates (body and .key) were uploaded in the Appliance -> Server Maintenance section. The staging server was confirmed to be functioning correctly after these adjustments.

## Notes
- Ensure that DNS settings are correctly configured when setting up new servers to avoid similar access issues.
- Remember to upload the required certificates for proper server maintenance and functionality.
- Always verify access via both IP and DNS to diagnose connectivity issues effectively.