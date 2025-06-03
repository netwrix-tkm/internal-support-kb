## Ticket Metadata
- **Ticket ID:** 500Qk00000BizhOIAR
- **Case Number:** 411663
- **Status:** Closed - Resolved
- **Account/Company:** Diamond Environmental Services
- **Contact Name:** Curt Jaquish
- **Product:** Netwrix Endpoint Protector
- **Component:** Alerts
- **Feature:** Alerts - Other
- **Version:** Not specified

## Problem Description
The customer reported that they were not receiving email notifications due to issues with their SMTP setup.

## Environment Details
- The customer was using an SMTP server for email notifications.
- The issue was specifically related to email alerts configured in the Netwrix Endpoint Protector.

## Troubleshooting Steps
1. Updated the email server settings and provided documentation for Office 365 setup.
2. Enabled file tracing and made minor adjustments to global settings.
3. Configured two CAP (Content Aware Protection) policies.
4. Configured the alerts within the system.
5. Attempted to use a Google account for email notifications.

## Root Cause
The root cause of the issue was not explicitly identified in the case. However, it was indicated that the original email setup was not functioning correctly, leading to the failure in receiving alerts.

## Solution
The issue was resolved when the customer switched to using a new Gmail account for email notifications. The alerts began functioning correctly with this new configuration.

## Notes
- It is important to ensure that the SMTP settings are correctly configured for the specific email service being used (e.g., Office 365, Gmail).
- Future cases should consider testing with different email accounts if issues persist with the initial setup.
- Documentation for setting up SMTP with various email providers should be readily available to assist customers in configuring their systems correctly.