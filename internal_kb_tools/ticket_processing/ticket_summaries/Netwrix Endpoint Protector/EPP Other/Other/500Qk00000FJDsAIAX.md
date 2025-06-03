## Ticket Metadata
- **Ticket ID:** 500Qk00000FJDsAIAX
- **Case Number:** 419960
- **Status:** Closed - Resolved
- **Account/Company:** PT Korelasi Persada Indonesia
- **Contact Name:** Dede Hilmat
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Other
- **Version:** NONE

## Problem Description
The customer, Aladin Bank, reported an issue with upload speeds after installing the Cososys Agent with Deep Packet Inspection (DPI) enabled. Disabling DPI resulted in normal upload speeds.

## Environment Details
- The issue was specifically related to the Cososys Agent with DPI enabled.
- The customer was using the Chrome browser from a different location than the standard application directory.

## Troubleshooting Steps
1. Disabled DPI, which restored normal upload speeds.
2. Investigated logs to determine if the Chrome browser was being monitored by the Cososys Agent.
3. Suggested adding the Chrome helper process to the monitored applications in the backend.

## Root Cause
The root cause of the upload speed issue was identified as the Cososys Agent's DPI feature not monitoring the Chrome helper process, which was causing the upload speed degradation.

## Solution
The issue was resolved by including a fix in the 5941 release of the Endpoint Protector. This fix involved adding the Chrome helper process to the monitored applications in the backend with the following SQL command:

```sql
INSERT INTO cf_application_grouped (cf_application_id, name, code, channel, use_data_exchange_host_process, use_dpi) VALUES (*XXXX*, 'Google Chrome', 'com.google.Chrome.helper', 3, 0, 1);
```

Where *XXXX* was replaced with the appropriate application ID retrieved from the database.

## Notes
- Ensure that any new applications or processes used by customers are monitored by the Cososys Agent to prevent similar issues in the future.
- It is advisable to keep the Endpoint Protector updated to the latest version to benefit from fixes and improvements.