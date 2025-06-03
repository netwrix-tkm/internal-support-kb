## Ticket Metadata
- **Ticket ID:** 500Qk00000GoslbIAB
- **Case Number:** 423385
- **Status:** Closed - Resolved
- **Account/Company:** DEVCON GmbH
- **Contact Name:** Falko Groebel
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** Allowlist / Denylist
- **Version:** NONE

## Problem Description
The customer, DEVCON GmbH, reported an issue with enabling file uploads to their ticket system after activating Content-Aware Protection (CAP). They were unable to successfully allow uploads to a specific URL, despite creating an allowlist entry.

## Environment Details
- **DPI (Deep Packet Inspection):** Enabled
- **Allowlist Dictionary:** "NameUnseresTicketSystems" created in the DPI Allowlist section.

## Troubleshooting Steps
1. Verified that CAP was activated.
2. Checked the "Content Aware Richtlinien" (Content Aware Policies) for the presence of the allowlist entry.
3. Attempted to re-add the allowlist entry to see if it would persist.
4. Confirmed that the allowlist entry was not visible upon revisiting the policies.

## Root Cause
The issue was identified as a display problem within the CAP policy settings, where the allowlist was not being displayed correctly in the list, leading to confusion about whether the entry was saved.

## Solution
The resolution involved confirming that the allowlist entry was indeed created but not displayed due to a UI issue. The customer was advised that the entry was functional despite not appearing in the list, and they could proceed with their intended uploads.

## Notes
- It is important to monitor the display of allowlist entries in the CAP policy settings, as this may lead to confusion for users.
- Future updates may address the UI issue to ensure that allowlist entries are consistently displayed.