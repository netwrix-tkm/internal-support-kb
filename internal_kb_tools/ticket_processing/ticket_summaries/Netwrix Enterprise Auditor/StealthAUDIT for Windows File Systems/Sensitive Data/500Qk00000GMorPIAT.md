## Ticket Metadata
- **Ticket ID:** 500Qk00000GMorPIAT
- **Case Number:** 422386
- **Status:** Closed - Resolved
- **Account/Company:** Inland Empire Health Plan
- **Contact Name:** Justin Cahill
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Windows File Systems
- **Feature:** Sensitive Data
- **Version:** 11.6

## Problem Description
The customer, IEHP, reported an issue where the Sensitive Data Discovery (SDD) job would run but then stop unexpectedly with a duration of 0 seconds. This stoppage prevented subsequent jobs in the queue, such as the bulk import, from starting. The logs indicated a timeout error related to the job execution.

## Environment Details
- **Server Software Versions:**
  - Netwrix Enterprise Auditor V11.6 (11.6.0.72)
  - Netwrix Access Information Center (11.6.0.13)
  - Netwrix Activity Monitor Agent 64-bit (7.0.3099)
  - Netwrix Activity Monitor (7.0.3099)
  - Netwrix Sensitive Data Discovery Add-On V11.6 (11.6.0.11)
  - Netwrix Enterprise Auditor File System Scanning Proxy (11.6.0.21)

## Troubleshooting Steps
1. Reviewed the applet logs for error messages.
2. Noted the specific error: 
   ```
   2024-09-26 23:19:59.4911|ERROR|  9|Stealthbits.StealthAUDIT.DataCollectors.FSAA.Applet.Host.Program|Timed out waiting for command, exiting process
   ```
3. Confirmed that the scheduled task exited with code 0, which aligned with the observed behavior of subsequent jobs not triggering.
4. Investigated similar issues reported by other customers regarding SQL scan job failures.
5. Escalated the issue to development for further analysis.

## Root Cause
The issue was identified as a bug in the version of Netwrix Enterprise Auditor being used (11.6). This bug caused the SDD job to time out and exit prematurely, preventing the execution of subsequent jobs in the queue.

## Solution
The development team recommended upgrading to a newer version of Netwrix Enterprise Auditor, which included fixes for the identified bug. The customer was advised to perform the upgrade and monitor the system. If the issue persisted after the upgrade, they were instructed to reopen the ticket and provide additional logs for further investigation.

## Notes
- The customer indicated that the upgrade may take a few weeks.
- It is important to ensure that customers are running the latest version of the software to avoid similar issues in the future.
- If issues persist post-upgrade, collecting detailed job logs and application logs will be crucial for troubleshooting.