## Ticket Metadata
- **Ticket ID:** 500Qk00000JYFZpIAP
- **Case Number:** 429961
- **Status:** Closed - Resolved
- **Account/Company:** The Pidcock Company
- **Contact Name:** Mark Gnall
- **Product:** Netwrix Endpoint Protector
- **Component:** Alerts
- **Feature:** Alerts - Other
- **Version:** Not specified

## Problem Description
The customer requested confirmation that the email address `jspidcock@pidcockcompany.com` would no longer receive email alerts from Endpoint Protector. Despite removing this account from the administrators, the customer reported that alert emails were still being received.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Alerts

## Troubleshooting Steps
1. Confirmed that the administrator account had been removed from the system.
2. Advised the customer to delete the existing alerts and recreate them.
3. Awaited customer feedback on whether the issue persisted after the above steps.

## Root Cause
The issue was caused by the administrator account not being fully removed from the database, which allowed the email alerts to continue being sent to the associated email address.

## Solution
The issue was resolved by executing the following SQL commands to ensure complete removal of the administrator account from the database:
```sql
SELECT id FROM sf_guard_user WHERE username = 'jspidcock@pidcockcompany.com';
DELETE FROM sf_guard_user_profile WHERE user_id = prev_user_id;
DELETE FROM sf_guard_user WHERE id = ...;  -- Replace with the actual ID obtained from the first query
```
After these steps were completed, the customer confirmed that they no longer received alert emails.

## Notes
- Ensure that when removing an administrator, all associated database entries are also cleared to prevent similar issues in the future.
- If errors occur during deletion, check for multiple database relationships that may prevent the removal of the user and address them accordingly.