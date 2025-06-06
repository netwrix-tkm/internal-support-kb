## Ticket Metadata
- **Ticket ID:** 500Qk00000KjmBSIAZ
- **Case Number:** 432599
- **Status:** Closed - Resolved
- **Account/Company:** Glatfelter Insurance Group
- **Contact Name:** Bryan Gustin
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Exchange
- **Feature:** Configuration
- **Version:** 11.6

## Problem Description
The customer reported that the Exchange Online EWS was not successfully collecting data despite verifying the settings and host configurations.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Collector Code:** StealthAUDIT for Exchange

## Troubleshooting Steps
1. Verified the settings for Exchange Online EWS.
2. Checked the host configurations to ensure they were correct.
3. Attempted to collect data multiple times without success.

## Root Cause
The issue was identified as a problem with the Autodiscover service, which was not properly configured.

## Solution
The resolution involved fixing the Autodiscover settings, which allowed the Exchange Online EWS to successfully collect data thereafter.

## Notes
- Ensure that Autodiscover is correctly configured in future setups to avoid similar issues.
- Regularly verify settings and host configurations as part of routine maintenance to preemptively catch potential issues.