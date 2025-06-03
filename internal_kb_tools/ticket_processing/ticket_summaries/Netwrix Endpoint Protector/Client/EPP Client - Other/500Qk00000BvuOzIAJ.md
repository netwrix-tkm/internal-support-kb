```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000BvuOzIAJ
- **Case Number:** 412108
- **Status:** Closed - Resolved
- **Account/Company:** Deloitte LLP (UK)
- **Contact Name:** Sanjay Amlani
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** EPP Client - Other
- **Version:** None

## Problem Description
The customer reported an issue where logs for file transfers from encrypted USB devices were not being retrieved when using the latest client on macOS Sonoma. However, logs were available when the client agent was offline using OTP.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Build Number:** 5940
- **Operating System:** macOS Sonoma

## Troubleshooting Steps
1. Confirmed the issue with the customer regarding the absence of logs for encrypted USB devices.
2. Attempted to collect logs from the client agent while it was online and offline.
3. Engaged in remote sessions with the customer to reproduce the problem.
4. Collected log files from the client agent for analysis.
5. Provided instructions for log collection to the customer.
6. Tested a new build of the client to see if it resolved the logging issue.

## Root Cause
The issue was identified as being caused by the EPP agent not detecting the encrypted partition of the USB device due to the volume appearing after the USB was connected. The agent was not configured to handle this scenario, leading to the absence of file tracing logs.

## Solution
The problem was resolved by deploying a test build of the client, specifically version `EPPMac3.0.4.0002.Notarized`, which addressed the file tracing issue for the Courier Integral USB devices. The customer confirmed that this build successfully captured the necessary logs.

## Notes
- Ensure that the EPP agent is configured to recognize and handle encrypted partitions on USB devices.
- Future testing should include scenarios where the encrypted volume appears after the device connection to verify logging functionality.
- Always confirm the reachability of the EPP server during tests to ensure proper logging and communication.
```