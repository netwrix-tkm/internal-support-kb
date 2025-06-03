## Ticket Metadata
- **Ticket ID:** 500Qk00000DHTuBIAX
- **Case Number:** 415485
- **Status:** Closed - Resolved
- **Account/Company:** CoreWin Distributor
- **Contact Name:** Danylo Didenko
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** Predefined Content (PII)
- **Version:** NONE

## Problem Description
The customer, Asia Bank, reported that after implementing a Content Aware Protection (CAP) policy with a "Block and Remediate" action, the expected event type "Content Remediation Session Active" did not appear in the CAP reports. Instead, the events were logged as "Content Threat Blocked."

## Environment Details
- The issue was tested on a single PC with only one CAP policy enabled.
- The customer had not yet upgraded their clients at the time of the report.

## Troubleshooting Steps
1. Verified the configuration of the CAP policy to ensure it was set to "Block and Remediate."
2. Conducted internal tests to reproduce the issue in a controlled environment.
3. Confirmed with the customer that they followed the remediation process correctly.
4. Reviewed logs provided by the customer for any discrepancies.
5. Suggested a sequence of actions to the customer to test if the event would appear after a successful file transfer post-remediation.
6. Scheduled a remote session to further investigate the issue.

## Root Cause
The root cause was identified as a misunderstanding of the event logging behavior. The "Content Remediation Session Active" log is only generated after a successful transfer of a file that was previously intercepted and remediated. It does not log immediately after the remediation approval.

## Solution
The issue was resolved by clarifying the expected behavior of the logging system:
- The customer was instructed to follow these steps:
  1. Transfer a file that violates the CAP policy.
  2. Allow the policy to intercept the file transfer.
  3. Click "Authorize" for the transfer.
  4. Attempt to transfer the same file again.
  5. The event "Content Remediation Session Active" should now appear in the reports after the successful transfer.

After following these steps, the customer confirmed that the logs appeared as expected.

## Notes
- Ensure that customers understand the sequence of actions required for the logging to function as intended.
- Advise customers to upgrade their clients to the latest version to avoid potential discrepancies in functionality.
- Document any similar cases for future reference to streamline troubleshooting processes.