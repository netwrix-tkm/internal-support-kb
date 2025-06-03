## Ticket Metadata
- **Ticket ID:** 500Qk00000BhcIFIAZ
- **Case Number:** 411606
- **Status:** Closed - Resolved
- **Account/Company:** Deloitte LLP (UK)
- **Contact Name:** Sanjay Amlani
- **Product:** Netwrix Endpoint Protector
- **Component:** Alerts
- **Feature:** Alerts Configuration
- **Version:** EPP server 5.9.3.0, Client version 3.0.2.1

## Problem Description
The customer reported experiencing unwanted alerts when users plugged in devices during User Acceptance Testing (UAT). The intention was to receive alerts only for prohibited actions, such as attempting to upload files to USB devices that are blocked by the Endpoint Protection Policy (EPP).

## Environment Details
- **EPP Server Version:** 5.9.3.0
- **EPP Client Version:** 3.0.2.1
- **Operating System:** Not specified

## Troubleshooting Steps
1. Requested details about the EPP server version, client version, and OS type from the customer.
2. Provided guidance on configuring custom notifications through the server UI under System Parameters - Device Types and Notifications.
3. Suggested disabling user notifications within content-aware policies if they were not needed.
4. Clarified the customer's requirements for alerts related to specific actions, such as file copying and device control.

## Root Cause
The unwanted alerts were due to the default notification settings in the Netwrix Endpoint Protector, which were not customized to meet the specific needs of the customer during UAT.

## Solution
The issue was resolved by advising the customer on how to configure custom notifications for both Device Control (DC) and Content-Aware Protection (CAP) modules. This allowed them to tailor alerts to only trigger for specific actions, such as when a user attempts to perform a forbidden activity (e.g., writing to a USB device).

## Notes
- Ensure that customers are aware of the ability to customize alert settings to avoid unnecessary notifications.
- It may be beneficial to conduct a follow-up session with customers to review their alert configurations, especially during UAT phases, to ensure they align with their operational requirements.