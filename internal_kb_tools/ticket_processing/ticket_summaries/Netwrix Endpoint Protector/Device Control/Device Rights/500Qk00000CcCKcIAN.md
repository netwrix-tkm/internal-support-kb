## Ticket Metadata
- **Ticket ID:** 500Qk00000CcCKcIAN
- **Case Number:** 413888
- **Status:** Closed - Resolved
- **Account/Company:** The Emirates Centre for Strategic Studies & Research
- **Contact Name:** Mohamed Fairose
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device Rights
- **Version:** Not specified

## Problem Description
The customer requested assistance in generating a report from the Netwrix Endpoint Protector (EPP) console to identify which users and computers have granular permissions for device access. Specifically, they wanted to audit permissions that do not adhere to the "Preserve Global Settings" rule or have specific overrides.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Feature in Use:** Device Rights

## Troubleshooting Steps
1. Initial inquiry was made by the customer regarding the report generation capabilities of EPP.
2. Technical support provided a preliminary response indicating that a report might be possible.
3. A follow-up call was scheduled to discuss the reporting requirements in detail.
4. During the call, it was identified that the Effective Rights report might display incorrect permissions (e.g., users shown as having access when they do not).
5. The support engineer confirmed that a fix for this issue was planned for the next version release.

## Root Cause
The root cause of the issue was identified as a bug in the Effective Rights report functionality, which incorrectly displayed user permissions. This led to confusion regarding the actual access rights of users.

## Solution
The issue was acknowledged, and the support engineer informed the customer that a fix would be included in the upcoming version 5.9.4.0 of the software. The case was left open for further updates after the release of the patch, allowing the customer to retest the scenario once the fix was applied.

## Notes
- The customer should be aware that the Effective Rights report may not accurately reflect user permissions until the fix is applied in the next version.
- It is recommended to monitor for updates regarding the version release and to retest the reporting functionality after applying the patch.