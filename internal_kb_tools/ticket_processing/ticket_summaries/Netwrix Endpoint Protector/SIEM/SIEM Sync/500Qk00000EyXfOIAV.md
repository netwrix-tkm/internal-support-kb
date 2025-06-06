## Ticket Metadata
- **Ticket ID:** 500Qk00000EyXfOIAV
- **Case Number:** 419209
- **Status:** Closed - Resolved
- **Account/Company:** TrustingSocial
- **Contact Name:** Linh Hoang
- **Product:** Netwrix Endpoint Protector
- **Component:** SIEM
- **Feature:** SIEM Sync
- **Version:** Not specified

## Problem Description
The customer requested assistance in configuring the Netwrix Endpoint Protector (NEP) to ship logs to an ELK stack for easier log analysis, as they found the log analysis on the NEP portal to be challenging. They inquired about the necessity of installing a filebeat agent or configuring rsyslog for this purpose and whether SIEM integration with ELK is supported.

## Environment Details
- **Log Analysis Tool:** ELK Stack
- **Current Log Analysis Method:** NEP Portal

## Troubleshooting Steps
1. Reviewed the customer's request for shipping NEP logs to ELK.
2. Confirmed the compatibility of NEP with ELK for SIEM integration.
3. Provided guidance on the installation of the filebeat agent and configuration of rsyslog as potential solutions for log shipping.
4. Verified the configuration settings for SIEM integration with ELK.

## Root Cause
The issue stemmed from the customer's difficulty in analyzing logs directly through the NEP portal, prompting the need for an alternative solution to facilitate log analysis using the ELK stack.

## Solution
The issue was resolved by confirming that SIEM integration with ELK is supported. The customer was advised to proceed with the installation of the filebeat agent to ship logs to the ELK stack, along with the necessary configuration of rsyslog if required. This setup would enable efficient log analysis through the ELK stack.

## Notes
- Ensure that the customer is aware of the prerequisites for installing the filebeat agent and configuring rsyslog.
- Recommend testing the log shipping configuration in a staging environment before deploying it in production to avoid disruptions.
- Document any specific configurations used for future reference in similar cases.