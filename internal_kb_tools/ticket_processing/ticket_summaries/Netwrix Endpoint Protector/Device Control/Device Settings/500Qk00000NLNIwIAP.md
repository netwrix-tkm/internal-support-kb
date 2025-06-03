## Ticket Metadata
- **Ticket ID:** 500Qk00000NLNIwIAP
- **Case Number:** 440001
- **Status:** Closed - Resolved
- **Account/Company:** Publica Group Ltd.
- **Contact Name:** Harry Chew
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device Settings
- **Version:** 5.9.4.1 (latest official release at the time of resolution)

## Problem Description
The customer reported that printer devices were being added as duplicate entries over 10,000 times, overcrowding the console and making it difficult to manage.

## Environment Details
- The issue was observed in the Netwrix Endpoint Protector environment.
- The customer was using version 5.9.4.1 of the software.

## Troubleshooting Steps
1. Connected remotely with the customer to review the device entries.
2. Noted that the number of duplicate entries had increased to approximately 693,000.
3. Deleted up to 43,000 duplicate entries during the remote session.
4. Monitored the situation over the following days to check for further increases in device entries.
5. Conducted additional remote sessions to investigate the issue further.
6. Identified that entries showing "noUser" were generated when the EppClient service started without a user logged in.

## Root Cause
The root cause of the duplicate entries was identified as events being generated when the EppClient service started without any user logged in. This resulted in events being logged under "noUser," leading to the appearance of duplicate device entries.

## Solution
The issue was resolved by:
- Removing the duplicate entries that had accumulated in the system.
- Educating the customer on the behavior of the EppClient service and how it logs events when no user is logged in.
- Advising the customer to monitor the situation and check for updates to the software, specifically the upgrade to version 5.9.4.2, which addresses security advisories.

## Notes
- It is important for users to be aware that events logged under "noUser" can lead to confusion regarding device entries.
- Customers should be encouraged to keep their software updated to the latest version to mitigate potential issues and security vulnerabilities.
- A snapshot of the Endpoint Protector appliance should be prepared before any remote troubleshooting sessions to ensure a quick recovery in case of unintended changes.