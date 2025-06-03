## Ticket Metadata
- **Ticket ID:** 500Qk00000CMvdSIAT
- **Case Number:** 413215
- **Status:** Closed - Resolved
- **Account/Company:** Sony India Software Centre
- **Contact Name:** Sathiyapprakaash Kesavaram
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Client - Other
- **Feature:** EPP Client - Other
- **Version:** NONE

## Problem Description
The customer reported that when Data Loss Prevention (DPI) is enabled, sensitive files are blocked but not shadowed. This issue was encountered during a Proof of Concept (POC) with Sony, which was critical for a potential deal worth $156k.

## Environment Details
- The issue was observed on a Windows environment where DPI and file shadowing were both enabled.
- The customer noted that the background discovery thread did not activate until after the file block event was sent to the server.

## Troubleshooting Steps
1. Reviewed logs to confirm the sequence of events during file blocking and shadowing.
2. Verified that the DPI settings were correctly configured.
3. Attempted to replicate the issue in a controlled environment.
4. Engaged with the sales team to gather additional context on the frequency of the issue.
5. Opened an ADO case for further investigation and improvement requests.

## Root Cause
The root cause of the issue was identified as a timing problem where the background discovery thread was not starting until after the file block event was processed. This resulted in the shadowing not occurring as expected when DPI was enabled.

## Solution
The issue was acknowledged as a limitation of the current implementation. It was noted that the background discovery thread should ideally start before the file gets blocked to allow for proper shadowing. The support team provided recommendations for future POCs, including:
- Avoiding the use of dlptest.com for testing.
- Using websites where file uploads require a manual submission (e.g., hitting a "Submit" button) to give the system time to process the file.

The case was closed with the understanding that this behavior may be improved in future updates.

## Notes
- It is important to inform users that this issue may only occur during the first attempt to upload from a specific folder. Subsequent attempts may succeed in shadowing.
- Future testing should consider the specifications of the machine, as performance may vary.
- The customer was added as a watcher on the ADO ticket for ongoing updates regarding potential improvements.