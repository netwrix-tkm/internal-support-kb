## Ticket Metadata
- **Ticket ID:** 500Qk00000NVfPqIAL
- **Case Number:** 440437
- **Status:** Closed - Resolved
- **Account/Company:** BioCatch
- **Contact Name:** Daniel Itenberg
- **Product:** Netwrix Endpoint Protector
- **Component:** SIEM
- **Feature:** SIEM Sync
- **Version:** 3.1

## Problem Description
The customer reported an issue with the SIEM integration where logs stopped flowing once TLS encryption was enabled. They confirmed that the configuration on the Splunk side was functioning correctly and suspected the issue might be related to the TLS configuration on the EPP server.

## Environment Details
- **Integration Tool:** Splunk SC4S
- **Data Source:** Syslog from EPP to Splunk

## Troubleshooting Steps
1. Confirmed with Splunk support that their configuration was correct and functioning as expected.
2. Scheduled a remote session to investigate the TLS configuration on the EPP server.
3. During the remote session, verified that syslog logs were being sent from the EPP server.
4. Checked the encryption settings and confirmed that encrypted files were sent and received correctly.

## Root Cause
The issue was identified as a blockage on the SIEM server side, which was preventing the logs from being processed after TLS encryption was enabled. There was a theory that the EPP was attempting to use TLS 1.1, which was not supported by the customer's environment.

## Solution
The issue was resolved during the remote session by demonstrating that the data was being sent from the EPP server. The logs were confirmed to be blocked by the SIEM server, and once this was identified, the case was closed.

## Notes
- Ensure that the TLS version compatibility is checked between the EPP and the SIEM server to prevent similar issues in the future.
- It is advisable to verify the communication paths and configurations on both ends (EPP and SIEM) when troubleshooting log flow issues after enabling encryption.