# Netwrix Support Case Summary

## Ticket Metadata
- **Ticket ID:** 500Qk00000FdRkUIAV
- **Case Number:** 420718
- **Status:** Closed - Resolved
- **Account/Company:** ProtektNET - MX
- **Contact Name:** Juan Gutierrez
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Other
- **Version:** NONE

## Problem Description
The customer reported an issue with the Network Time Protocol (NTP) configuration, stating that the time displayed was out of date despite having the settings correctly configured. The customer provided evidence indicating a discrepancy in the time shown versus the actual time from the NTP server.

## Environment Details
- **NTP Server Used:** mx.pool.ntp.org
- **Time Zone Configuration:** MST (Mountain Standard Time)

## Troubleshooting Steps
1. Verified the NTP configuration settings on the affected system.
2. Checked the time zone settings to ensure they were correctly set to MST.
3. Reviewed the logs for any errors related to NTP synchronization.
4. Confirmed connectivity to the NTP server (mx.pool.ntp.org).
5. Observed the time displayed on the system and compared it with the expected time from the NTP server.

## Root Cause
The root cause of the issue was identified as a misconfiguration of the time zone settings. The NTP was set to MST, which was appropriate, but the displayed time did not reflect the correct synchronization with the NTP server.

## Solution
The issue was resolved by confirming that the NTP settings were indeed correct and ensuring that the system was set to the appropriate time zone (MST). Once verified, the time displayed on the system synchronized correctly with the NTP server, reflecting the accurate time.

## Notes
- Ensure that the time zone settings are correctly configured when troubleshooting NTP issues, as discrepancies can lead to confusion regarding the actual time.
- Regularly verify NTP synchronization and time zone settings to prevent similar issues in the future.