## Ticket Metadata
- **Ticket ID:** 500Qk00000KFpxxIAD
- **Case Number:** 431178
- **Status:** Closed - Resolved
- **Account/Company:** Helo.ai
- **Contact Name:** Sai Nachiappan
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** CAP Policies
- **Version:** NONE

## Problem Description
The customer reported an issue where they were unable to attach PNG files. Specifically, out of ten PNG files attempted for upload, five were successfully uploaded while the other five encountered errors.

## Environment Details
- The issue was observed in a setup utilizing Netwrix Endpoint Protector with specific report policies applied.
- Deep Packet Inspection with "Peer Certificate Validation" was enabled during troubleshooting sessions.

## Troubleshooting Steps
1. Conducted a remote session to observe the issue.
2. Verified that when "Peer Certificate Validation" was turned off, access to the Kaspersky Security Centre was restored.
3. Identified that the Windows policy was not functioning as expected, blocking attachments despite being configured to allow them.
4. Escalated the issue to the R&D team and submitted EPP Client logs for analysis.
5. Enabled append logs during the last remote session to capture further details if the issue reoccurred.
6. Requested the customer to provide append log files, artifacts, screenshots, and timestamps of incidents for further investigation.

## Root Cause
The root cause of the issue was identified as a conflict between the applied Windows policy and the Content-Aware Protection (CAP) settings, which were blocking certain attachments (specifically .png and .jpeg files) despite being allowed in the policy configuration. Additionally, the OCR processing time for images was causing delays, leading to temporary blocks on file transfers.

## Solution
The issue was resolved by:
- Conducting a remote session where the problem could not be reproduced.
- Enabling append logs to capture any future occurrences.
- The R&D team confirmed that a test build was functioning correctly, and it was planned to include the fix in a future release of Endpoint Protector after version 5.9.4.2.

## Notes
- The customer did not provide further updates after the last remote session, leading to the closure of the case.
- It is recommended to monitor for similar issues in future releases and ensure that customers are aware of the need to save images to disk if they encounter blocking issues during the first upload attempt. Subsequent attempts may succeed once the OCR text is available.