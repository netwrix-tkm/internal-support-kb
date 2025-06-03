## Ticket Metadata
- **Ticket ID:** 500Qk00000CgIcjIAF
- **Case Number:** 414115
- **Status:** Closed - Resolved
- **Account/Company:** MindSec
- **Contact Name:** Alex Julio
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Other
- **Version:** Not specified

## Problem Description
The customer, Andbank, reported unexpected behaviors with the Endpoint Protector (EPP), including blocking web pages and digital certificates during system access. Despite these issues, no blocks were indicated in the CAP reports or other logs. Disabling continuous policies did not resolve the issue, leading to the necessity of uninstalling the EPP client.

## Environment Details
- Customer: Andbank
- Product in use: Netwrix Endpoint Protector

## Troubleshooting Steps
1. Reviewed CAP reports and logs for any indications of blocks.
2. Attempted to disable continuous policies within the EPP settings.
3. Uninstalled the EPP client as a last resort to stop the blocking behavior.
4. Scheduled a remote session to gather logs and further investigate the issue.
5. Created a Deep Packet Inspection (DPI) whitelist to allow specific traffic.

## Root Cause
The root cause of the issue was identified as improper handling of certificate validation within the EPP, likely due to conflicts with other installed software (e.g., VPNs, other DLP solutions) that interfered with the EPP's ability to validate certificates correctly.

## Solution
The issue was resolved by creating a DPI whitelist, which allowed the necessary traffic to bypass the blocking rules set by the EPP. This adjustment enabled the customer to access the previously blocked web pages and digital certificates without further issues.

## Notes
- Ensure that any third-party applications (like VPNs or other DLP solutions) are considered when troubleshooting similar issues, as they may interfere with EPP operations.
- For future cases, it is advisable to check the settings related to certificate validation and ensure that all necessary options are configured correctly to avoid similar problems.
- Customers should be instructed on how to create DPI whitelists for any future needs to prevent similar disruptions.