```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000BlZiMIAV
- **Case Number:** 411787
- **Status:** Closed - Resolved
- **Account/Company:** WellSpan Health
- **Contact Name:** John Masgalas
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Initial setup
- **Version:** 11.5

## Problem Description
The customer reported that the access times displayed in the Activity Details section of the Netwrix Auditor Interface (AIC) appeared to be in Eastern Standard Time (EST), but the exported times were consistently 6 hours ahead, leading to confusion regarding the time zone being used.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Collector Code:** StealthAUDIT General
- **Product Version:** 11.5

## Troubleshooting Steps
1. Reviewed the screenshots provided by the customer to understand the discrepancy in time formats.
2. Confirmed that both XLSX and CSV exports exhibited the same issue.
3. Explained to the customer that the access time is derived from the server being scanned.

## Root Cause
The access times displayed in the AIC are based on the server's local time, which is in Coordinated Universal Time (UTC). The confusion arose because the customer expected the times to be in EST, leading to a misunderstanding of the time zone conversion.

## Solution
The issue was resolved by clarifying to the customer that the access times are reported in UTC from the server's local time. This explanation helped the customer understand the time zone differences and the reason for the 6-hour discrepancy.

## Notes
- It is important for users to be aware that access times are reported in UTC based on the server's local time. Future inquiries regarding time discrepancies should include this clarification to prevent confusion.
- Encourage users to check the server's time zone settings if they experience similar issues with time reporting.
```