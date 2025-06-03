## Ticket Metadata
- **Ticket ID:** 500Qk00000FoOrJIAV
- **Case Number:** 421094
- **Status:** Closed - Resolved
- **Account/Company:** QUALITY ASSISTANCE S.A.
- **Contact Name:** Guillaume Mainil
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** Upload Not Blocked
- **Version:** NONE

## Problem Description
The customer reported that their Content Aware Protection rules, which were previously effective in preventing uploads via Microsoft Teams, were no longer functioning as intended.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Feature Affected:** Upload Not Blocked

## Troubleshooting Steps
1. Verified the configuration of the Content Aware Protection rules.
2. Checked for any recent changes in the environment that could affect the rules.
3. Enabled Deep Packet Inspection (DPI) and Stealthy DPI settings to enhance monitoring and blocking capabilities.

## Root Cause
The issue was identified as a lack of effective monitoring and blocking due to the DPI settings being disabled, which prevented the Content Aware Protection rules from functioning correctly.

## Solution
The issue was resolved by enabling the Deep Packet Inspection (DPI) and Stealthy DPI features within the Netwrix Endpoint Protector. After these settings were activated, the file uploads were successfully blocked as intended.

## Notes
- Ensure that DPI settings are enabled for Content Aware Protection rules to function effectively.
- Regularly review and test the configuration of protection rules to ensure they remain effective against potential changes in user behavior or application updates.