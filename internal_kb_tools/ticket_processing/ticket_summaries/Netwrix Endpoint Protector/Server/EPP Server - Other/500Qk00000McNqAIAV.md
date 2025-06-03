## Ticket Metadata
- **Ticket ID:** 500Qk00000McNqAIAV
- **Case Number:** 437888
- **Status:** Closed - Resolved
- **Account/Company:** PeopleStrong
- **Contact Name:** Rohit Nawani
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** NONE

## Problem Description
All administrators were unable to access the EPP portal after entering the Multi-Factor Authentication (MFA) credentials, receiving an error indicating incorrect MFA.

## Environment Details
- The server time was found to be incorrect, which is critical for the proper functioning of MFA.

## Troubleshooting Steps
1. Verified the MFA credentials entered by the administrators.
2. Checked server settings and logs for any anomalies.
3. Identified that the server time was not synchronized correctly.
4. Attempted to adjust the server time settings.

## Root Cause
The issue was caused by the server time being incorrect, which led to discrepancies in the MFA validation process.

## Solution
The server time was manually adjusted to the correct time, and the Network Time Protocol (NTP) settings were saved again to ensure proper synchronization moving forward.

## Notes
- Ensure that server time is regularly synchronized with an NTP server to prevent similar issues in the future.
- Monitor MFA functionality after any server time adjustments to confirm that access issues do not recur.