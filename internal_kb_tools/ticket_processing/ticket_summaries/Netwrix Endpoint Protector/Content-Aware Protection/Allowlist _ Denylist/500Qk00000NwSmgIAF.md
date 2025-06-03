## Ticket Metadata
- **Ticket ID:** 500Qk00000NwSmgIAF
- **Case Number:** 441704
- **Status:** Closed - Resolved
- **Account/Company:** Bright Life Care Limited
- **Contact Name:** Vikas Kataria
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** Allowlist / Denylist
- **Version:** NONE

## Problem Description
The customer reported that file blocking for Excel (.xlsx) and Word (.docx) documents in the WhatsApp application was not functioning as expected. While the blocking of executable (.exe) files was working correctly, the specified document types were not being blocked despite the policy settings being configured properly.

## Environment Details
- The issue occurred on the WhatsApp desktop application.
- The CAP (Content-Aware Protection) policy was set to block specific file types, including Excel and Word documents.

## Troubleshooting Steps
1. Connected remotely with the customer, Vikas, to investigate the issue.
2. Verified that the CAP policy was correctly configured to block .xlsx and .docx file types.
3. Confirmed that both WhatsApp exit points were selected in the policy settings.
4. Checked the entity selection to ensure the policy was applied to the correct computer.
5. Conducted tests to attempt to replicate the issue.
6. Identified that MTP (Media Transfer Protocol) scanning was disabled.

## Root Cause
The root cause of the issue was identified as the MTP scanning feature being disabled, which prevented the blocking of the specified file types in the WhatsApp application.

## Solution
The issue was resolved by enabling the MTP scanning feature. After enabling this feature, the customer tested the file blocking again, and the .xlsx and .docx files were successfully blocked as intended.

## Notes
- Ensure that MTP scanning is enabled when configuring file blocking policies for applications that utilize this protocol.
- It is advisable to verify all relevant settings in the CAP policy before concluding that the issue lies elsewhere.