## Ticket Metadata
- **Ticket ID:** 500Qk00000EyWRaIAN
- **Case Number:** 419200
- **Status:** Closed - Resolved
- **Account/Company:** Halodata International Pte Ltd
- **Contact Name:** Halodata Support Tech
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** CAP Exitpoints / Applications
- **Version:** NONE

## Problem Description
The customer, Halodata International Pte Ltd, reported an issue with the application section of the EPP Policy Denylist not effectively blocking WhatsApp Desktop. They were attempting to block the application using specific commands in the denylist but were unsuccessful.

## Environment Details
- The application in question (WhatsApp Desktop) was installed via the Microsoft Store, which saves applications in a hidden WindowsApps folder and applies Windows Security policies.

## Troubleshooting Steps
1. The support technician attempted to replicate the issue in their environment but was unable to do so.
2. It was noted that applications installed from the Microsoft Store are subject to specific security policies that may prevent EPP from blocking them.
3. The technician confirmed that other applications, such as Telegram, were being blocked successfully using the same denylist method.
4. The technician updated the software to versions 5.9.4.0 and 6.2.3.1 to ensure the latest features and fixes were applied.
5. Logs were requested to further investigate the issue.

## Root Cause
The root cause of the issue was identified as the security policies applied to applications installed from the Microsoft Store, which prevented the EPP from accessing the necessary data to block WhatsApp Desktop effectively.

## Solution
The issue was resolved by adding an asterisk (*) in the parameters section of the denylist for applications. This adjustment allowed the denylist to effectively block WhatsApp Desktop.

## Notes
- When dealing with applications installed from the Microsoft Store, be aware that they may have additional security policies that could affect the functionality of the denylist.
- Future cases involving similar applications should consider using wildcard entries in the denylist to enhance blocking capabilities.