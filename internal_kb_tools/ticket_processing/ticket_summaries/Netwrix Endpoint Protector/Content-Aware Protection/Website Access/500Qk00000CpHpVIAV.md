```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000CpHpVIAV
- **Case Number:** 414442
- **Status:** Closed - Resolved
- **Account/Company:** TM System Pvt Ltd
- **Contact Name:** Satish Kalola
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** Website Access
- **Version:** 6.2.2.1006

## Problem Description
The customer reported an issue with website access for certain clients after enabling the content awareness policy in Netwrix Endpoint Protector.

## Environment Details
- Client IP Address: 172.21.26.26
- The issue arose after the implementation of a content awareness policy.

## Troubleshooting Steps
1. The support team reached out to the customer to schedule a remote session via Zoom for further investigation.
2. The customer was advised to have Putty installed for SSH access to the server.
3. A remote session was conducted to analyze the issue.
4. The client version was checked, and it was noted that an upgrade was necessary.
5. The client version was upgraded to 6.2.2.1006, and the same DPI settings were retained.
6. Post-upgrade, the threat was reported in the Content-Aware Protection (CAP) reports.

## Root Cause
The issue was caused by the outdated client version of the Netwrix Endpoint Protector, which did not properly handle the content awareness policy settings.

## Solution
The issue was resolved by upgrading the client version to 6.2.2.1006. After the upgrade, the settings were verified, and the website access issue was resolved, allowing the client to access the necessary sites without further problems.

## Notes
- Ensure that all clients are running the latest version of Netwrix Endpoint Protector to avoid similar issues in the future.
- Regularly check and update DPI settings after any policy changes to ensure compliance and functionality.
```