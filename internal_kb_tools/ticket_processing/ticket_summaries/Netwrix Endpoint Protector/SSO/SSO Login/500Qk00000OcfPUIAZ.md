```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000OcfPUIAZ
- **Case Number:** 443664
- **Status:** Closed - Resolved
- **Account/Company:** White Rock
- **Contact Name:** Evgeny Zinchenko
- **Product:** Netwrix Endpoint Protector
- **Component:** SSO
- **Feature:** SSO Login
- **Version:** 16.1

## Problem Description
The customer reported being locked out of their system after changing the Single Sign-On (SSO) configuration from the server's IP address to its DNS name. They encountered an error message stating, "There has been an issue with your Single Sign On Process. Please check the Single Sign On Settings." Additionally, the failover link was not saved properly.

## Environment Details
- The EPP server is hosted on the AWS platform.

## Troubleshooting Steps
1. Confirmed the failover URL configuration, which worked but did not resolve the SSO issue.
2. Engaged with the customer to gather more information about the server hosting environment.
3. Advised the customer to revisit their SSO settings.

## Root Cause
The issue was caused by an incorrect configuration of the SSO settings after the transition from using the server's IP address to its DNS name. The failover link was not saved correctly, contributing to the lockout.

## Solution
The customer was guided to complete the SSO configuration correctly. After they revisited and finalized the SSO settings, the issue was resolved, allowing them to regain access.

## Notes
- Ensure that failover links are saved properly during configuration changes to avoid similar lockout issues in the future.
- It is advisable to double-check SSO settings after any changes to the server's address format (IP vs. DNS).
```