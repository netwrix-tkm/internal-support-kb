## Ticket Metadata
- **Ticket ID:** 500Qk00000KiLmfIAF
- **Case Number:** 432514
- **Status:** Closed - Resolved
- **Account/Company:** American Express
- **Contact Name:** Alex Parsa
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Credentials
- **Version:** 11.5

## Problem Description
The customer inquired about the necessary steps to update the password for the service account used in Stealth Enterprise, specifically asking where within the console or activity monitor the password needs to be changed.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Product Version:** 11.5

## Troubleshooting Steps
1. Identified the need to update the service account password across various components of the Netwrix Enterprise Auditor.
2. Reviewed the following areas for potential password updates:
   - **Netwrix Enterprise Auditor Global Settings:**
     - Connection Profiles
     - Notifications
     - Schedule
     - Storage
   - **NEA Environment:**
     - Netwrix Services (Web Server, AIC, Vault)
     - FSAA Proxy (if not using LocalSystem)
   - **Netwrix Activity Monitor:**
     - Agent settings (select agent and click Edit to update the password under the connection tab)
     - Monitored Hosts (for NAS devices, select the Host and click Edit to update the user's password under the Auditing tab)

## Root Cause
The issue stemmed from the customer's need to ensure that all instances of the service account password were updated in the relevant configurations to maintain connectivity and functionality of the Netwrix Enterprise Auditor.

## Solution
The resolution involved providing the customer with a comprehensive list of locations where the service account password needed to be updated:
- **Netwrix Enterprise Auditor:**
  - Global Settings (Connection Profiles, Notifications, Schedule, Storage)
- **NEA Environment:**
  - Netwrix Services (Web Server, AIC, Vault)
  - FSAA Proxy (if applicable)
- **Netwrix Activity Monitor:**
  - Update agent settings and monitored hosts as necessary.

The customer was advised to follow these steps to ensure a smooth transition during the password change.

## Notes
- It is crucial to document all instances where service account passwords are used to prevent service disruptions.
- Future password changes should be planned with adequate time to update all necessary configurations to avoid downtime.