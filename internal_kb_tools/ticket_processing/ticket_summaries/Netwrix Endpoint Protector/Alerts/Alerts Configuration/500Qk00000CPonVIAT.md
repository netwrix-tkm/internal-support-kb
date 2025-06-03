## Ticket Metadata
- **Ticket ID:** 500Qk00000CPonVIAT
- **Case Number:** 413371
- **Status:** Closed - Resolved
- **Account/Company:** Fourth Partner Energy
- **Contact Name:** Narender Pal
- **Product:** Netwrix Endpoint Protector
- **Component:** Alerts
- **Feature:** Alerts Configuration
- **Version:** Not specified

## Problem Description
The customer reported an issue where they were unable to receive SMTP alerts from the Netwrix Endpoint Protector system.

## Environment Details
- The SMTP settings were configured to work with Outlook in a legacy mode.

## Troubleshooting Steps
1. The support engineer, Andrei Pop, requested confirmation from the customer regarding the SMTP settings and whether they could receive a test email.
2. The customer provided their SMTP settings but indicated they had not received any test emails.
3. The support engineer suggested turning off the "Use TLS 1.3" option if the legacy option was being used.
4. The customer confirmed that the suggested changes worked, and they were able to receive the test email.

## Root Cause
The issue was caused by the SMTP settings being incompatible with the current configuration, specifically related to the use of TLS 1.3 when the legacy option was enabled.

## Solution
The resolution involved adjusting the SMTP settings to ensure compatibility with the legacy mode by disabling the "Use TLS 1.3" option. Once this change was made, the customer was able to receive alerts successfully.

## Notes
- When configuring SMTP settings for legacy systems, ensure that TLS 1.3 is disabled to avoid compatibility issues.
- Always confirm the SMTP settings with the customer and test the configuration after making changes to ensure alerts are being received.