## Ticket Metadata
- **Ticket ID:** 500Qk00000HBZwlIAH
- **Case Number:** 424349
- **Status:** Closed - Resolved
- **Account/Company:** Arista Networks, Inc.
- **Contact Name:** Bharani M
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** Not specified

## Problem Description
The customer, Bharani M, reported that after migrating the DNS of their server (`Epp.aristanetworks.com`) from an older server to a newer one, clients were not reporting to the new server. Bharani inquired whether a reboot of both the old and new servers was necessary to resolve the issue.

## Environment Details
- **DNS:** `Epp.aristanetworks.com`
- **Old Server:** Previously assigned DNS
- **New Server:** Newly assigned DNS

## Troubleshooting Steps
1. Confirmed the DNS migration was completed successfully.
2. Checked client configurations to ensure they were pointing to the new server.
3. Suggested a reboot of both the old and new servers to refresh connections.

## Root Cause
The issue was likely due to the clients not recognizing the new server immediately after the DNS change, which can occur if the DNS records are cached or if the clients have not updated their configurations to point to the new server.

## Solution
The issue was resolved by performing a reboot of the new server. This action allowed the server to refresh its connections and recognize the clients, enabling them to report correctly.

## Notes
- It is advisable to reboot servers after significant changes such as DNS migrations to ensure all services and connections are properly refreshed.
- Monitor client connections after DNS changes to confirm they are reporting to the correct server.