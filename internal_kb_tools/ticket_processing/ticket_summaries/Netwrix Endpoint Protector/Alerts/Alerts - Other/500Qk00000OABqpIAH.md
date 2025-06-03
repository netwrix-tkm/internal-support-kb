## Ticket Metadata
- **Ticket ID:** 500Qk00000OABqpIAH
- **Case Number:** 442445
- **Status:** Closed - Resolved
- **Account/Company:** Umpqua Bank
- **Contact Name:** Tyler Gamble
- **Product:** Netwrix Endpoint Protector
- **Component:** Alerts
- **Feature:** Alerts - Other
- **Version:** Not specified

## Problem Description
The customer imported new licenses for Netwrix Endpoint Protector on April 17, 2025, but continued to receive email alerts regarding license renewal, despite the new expiration date being correctly displayed in the web interface as April 19, 2028.

## Environment Details
- Previous license expiration date: April 19, 2025
- New license expiration date: April 19, 2028
- EPP Appliance was rebooted after the license import.

## Troubleshooting Steps
1. Joined a remote session and sent a Zoom link to the customer, but the customer did not join.
2. Waited 15 minutes before ending the remote session and followed up with the customer via email.
3. Informed the customer that the cron job responsible for resetting licenses may not have run yet and requested screenshots of the licensing page before and after the reboot.
4. Customer rebooted the EPP Appliance and reported continued receipt of renewal emails.
5. Consulted with the solutions channel for advice on stopping the renewal emails.
6. Scheduled a remote session for April 25, 2025, to verify configuration and ensure proper operation.

## Root Cause
The issue was likely related to a cron job that had not executed to update the licensing status after the new licenses were imported. This resulted in the system continuing to send renewal notifications despite the correct license information being displayed.

## Solution
The customer confirmed that the renewal emails stopped after April 21, 2025, and the licensing page correctly displayed the expiration date of 2028. As the issue resolved itself and no further emails were received, the case was closed without the need for additional remote sessions.

## Notes
- The customer was informed of a 30-day grace period for license activation, which provided reassurance during the troubleshooting process.
- Future remote sessions should be scheduled according to the customer's time zone (PST) to avoid scheduling conflicts.
- If similar issues arise, ensure to check the status of cron jobs and confirm that the licensing information is correctly updated in the system.