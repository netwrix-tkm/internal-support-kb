```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000BymbMIAR
- **Case Number:** 412216
- **Status:** Closed - Resolved
- **Account/Company:** The Stars Group Interactive Services / Flutter International
- **Contact Name:** John Leddy
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Access Error
- **Version:** Not specified

## Problem Description
The customer reported an issue where, when connected to GlobalProtect, they were unable to connect to the console and the agent could not connect to the server using the gateway IP addresses 130.41.177.245/32 or 130.41.177.252/32. The customer requested confirmation that these addresses were not blocked on the Netwrix side.

## Environment Details
- The issue occurred on both Windows and Mac operating systems.
- The customer was using GlobalProtect VPN.

## Troubleshooting Steps
1. Confirmed that the gateway addresses were not blocked on the Netwrix side.
2. Suggested checking if the "Stealthy DPI" setting was enabled on the customer's machines.
3. Investigated if the gateway addresses were blacklisted or included in an EPP denylist.
4. Increased the TCP connection limit per IP per second for the customer's server.

## Root Cause
The issue was caused by a TCP connection limit being reached for the customer's server IPs, which prevented successful connections.

## Solution
The TCP connection limit per IP per second was increased on the Netwrix side, which resolved the connectivity issues. The customer confirmed that the changes helped and they were able to connect successfully afterward.

## Notes
- The customer was able to bypass the issue temporarily by not tunneling the EPP client through the VPN.
- It is important to monitor TCP connection limits for servers to prevent similar issues in the future.
- Ensure to check both allowlists and denylists when troubleshooting connectivity issues.
```