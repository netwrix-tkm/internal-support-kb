```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000GHaAkIAL
- **Case Number:** 422167
- **Status:** Closed - Resolved
- **Account/Company:** QUALITY ASSISTANCE S.A.
- **Contact Name:** Guillaume Mainil
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Other
- **Version:** NONE

## Problem Description
The customer reported an issue with exporting a complete list of computers from the Netwrix Endpoint Protector. When attempting to export all entries to a CSV file, the export was limited to 200 computers, preventing a full export for validation against their Active Directory.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** EPP Other

## Troubleshooting Steps
1. Verified the export functionality from the computer menu.
2. Attempted to select all entries for export to CSV.
3. Checked for any settings or configurations that might limit the export size.
4. Reviewed documentation for any known limitations regarding the export feature.

## Root Cause
The limitation on the number of computers exported in a single CSV file was identified as a built-in restriction within the Netwrix Endpoint Protector software.

## Solution
The issue was resolved by informing the customer that the export functionality is limited to 200 entries per export. To obtain a complete list, the customer can perform multiple exports, each containing a different subset of computers, and then combine them manually into a single CSV file.

## Notes
- Customers should be aware of the 200-entry limit when exporting computer lists.
- It may be beneficial to suggest alternative methods for exporting larger datasets, such as using scripts or API calls if available in future versions.
```