## Ticket Metadata
- **Ticket ID:** 500Qk00000JrbbCIAR
- **Case Number:** 430651
- **Status:** Closed - Resolved
- **Account/Company:** Shakta Technologies Pvt Ltd
- **Contact Name:** Andrei Pop
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** Allowlist / Denylist
- **Version:** NONE

## Problem Description
The customer reported an issue regarding the application denylist functionality in the Netwrix Endpoint Protector, specifically related to how to add applications to the denylist.

## Environment Details
- The customer was using version 5940 of the server.

## Troubleshooting Steps
1. The customer added the denylist application as per the instructions.
2. Support escalated the ticket for further investigation.
3. Engineers checked the logs for application blocking rules.
4. Recommendations were made to ensure the correct syntax was used when adding applications to the denylist.
5. The customer was advised to resend the settings and redo tests to confirm functionality.

## Root Cause
The issue was identified as a potential misconfiguration in the denylist settings, where only one application (Anydesk) was added to the denylist instead of the expected applications (e.g., WinWord). There were also indications of issues with the server version 5940, where allowlists and denylist settings were not being saved or applied properly.

## Solution
The issue was resolved by confirming that the application denylist functionality was working as intended after the customer reconfigured the denylist settings correctly. The customer was instructed to ensure that the wildcard character "*" was included in the parameters when adding applications to the denylist.

## Notes
- Ensure that when adding applications to the denylist, the correct syntax is followed, including the use of wildcard characters where necessary.
- Be aware of potential issues with older server versions (like 5940) that may affect the application of allowlists and denylists. Upgrading to a newer version may resolve these issues.