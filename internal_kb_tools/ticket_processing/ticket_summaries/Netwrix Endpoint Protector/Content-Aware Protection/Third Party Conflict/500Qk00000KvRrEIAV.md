## Ticket Metadata
- **Ticket ID:** 500Qk00000KvRrEIAV
- **Case Number:** 433129
- **Status:** Closed - Resolved
- **Account/Company:** CoreWin Distributor
- **Contact Name:** Danylo Didenko
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** Third Party Conflict
- **Version:** Not specified

## Problem Description
PrivatBank reported an issue where the Cisco VPN connection drops intermittently due to conflicts with the Endpoint Protection Platform (EPP) client. After rebooting the PC, the VPN connection would work for 10-15 minutes before failing again, resulting in browser pages not loading. 

## Environment Details
- **VPN Client:** Cisco Secure Client
- **Symptoms:** 
  - Initially, all checkmarks in Cisco Secure Client are green.
  - Upon failure, the ISE Posture indicator turns gray, and the Secure Endpoint module shows a yellow mark.
  
## Troubleshooting Steps
1. Verified the initial problem description with the customer.
2. Observed the behavior of the Cisco Secure Client during the issue.
3. Terminated the EPP client, which resolved the connectivity issue temporarily.
4. Opened an ADO (Application Development Order) to investigate the issue further.
5. Awaited updates from R&D regarding the conflict.

## Root Cause
The root cause of the issue was identified as a conflict between the Cisco VPN client and the EPP client, which caused the VPN connection to drop and browser pages to stop loading.

## Solution
The issue was resolved by providing the customer with new builds of the EPP client that addressed the compatibility issues with the Cisco VPN client. This update eliminated the connection drops and restored normal functionality.

## Notes
- It is important to monitor the compatibility of third-party applications with the VPN client to prevent similar issues in the future.
- Ensure that customers are informed about potential conflicts with EPP clients when using Cisco VPN solutions.