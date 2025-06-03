## Ticket Metadata
- **Ticket ID:** 500Qk00000CzgpuIAB
- **Case Number:** 414882
- **Status:** Closed - Resolved
- **Account/Company:** Securisoft
- **Contact Name:** Ronan Takahashi
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** Allowlist / Denylist
- **Version:** Not specified

## Problem Description
The customer reported that they were unable to send internal emails with a .xlsx attachment, as the emails were being blocked by Cososys. They had already checked the allowlist configurations for their domain but were still facing issues.

## Environment Details
- The issue occurred within the Netwrix Endpoint Protector environment.
- The customer was using a virtual appliance for their EPP server.

## Troubleshooting Steps
1. The customer confirmed that the allowlist configurations were checked.
2. A remote session was scheduled to investigate the issue further.
3. During the troubleshooting process, it was noted that email alerts were not being sent by the EPP server.
4. A reboot of the EPP server was performed.

## Root Cause
The root cause of the issue was not explicitly identified; however, it was noted that the problem was resolved after a reboot of the EPP server. The customer did not change any policies, indicating that the reboot may have reset any temporary issues affecting the email functionality.

## Solution
The issue was resolved by rebooting the EPP server. After the reboot, the internal email sending functionality, including the ability to send .xlsx attachments, was restored without any further changes to the configurations.

## Notes
- It is advisable to consider rebooting the EPP server as a potential first step in troubleshooting similar issues, especially when email alerts or attachment sending functionalities are affected.
- Ensure that all configurations are double-checked before escalating to remote sessions, as some issues may be resolved with simple server reboots.