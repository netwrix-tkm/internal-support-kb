## Ticket Metadata
- **Ticket ID:** 500Qk00000KbwXlIAJ
- **Case Number:** 432068
- **Status:** Closed - Resolved
- **Account/Company:** Excellus Health Plan, Inc.
- **Contact Name:** Gary Bender
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Windows File Systems
- **Feature:** Activity Auditing
- **Version:** 11.6

## Problem Description
The customer reported an issue after adding a CEE device in the Netwrix Activity Monitor (NAM). Upon configuring the device, a separate host was created, and attempts to import data resulted in an error indicating that the INI section for the NAS device did not exist in the specified INI file.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Collector Code:** StealthAUDIT for Windows File Systems

## Troubleshooting Steps
1. Reviewed the configuration of the NAM agent used to audit the NAS device.
2. Verified that NAM was configured correctly and was successfully collecting events.
3. Attempted to add the output file to the server path but could not retrieve data.
4. Investigated the FSAC System Scan job configuration in Netwrix Enterprise Auditor.

## Root Cause
The issue was identified as an incorrect configuration of the FSAC System Scan job in Netwrix Enterprise Auditor. The job was mistakenly targeting the agent server instead of the NAS server.

## Solution
To resolve the issue, the host list used by the FSAC System Scan job was corrected to target the NAS server. After making this adjustment, the job successfully collected FSAC data from the NAS device. A subsequent test with the File Deletions job confirmed that it returned valid data as well.

## Notes
- Ensure that the FSAC System Scan job is correctly configured to target the appropriate server to avoid similar issues in the future.
- Regularly review configurations after adding new devices to ensure that all settings are correctly aligned with the intended targets.