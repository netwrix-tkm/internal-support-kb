## Ticket Metadata
- **Ticket ID:** 500Qk00000IFayTIAT
- **Case Number:** 426892
- **Status:** Closed - Resolved
- **Account/Company:** Payglocal Technologies private limited
- **Contact Name:** Yajat Gupta
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device Settings
- **Version:** NONE

## Problem Description
The customer requested assistance in creating rules to block access to personal email accounts from endpoints and prevent all types of file uploads, while allowing a whitelist of specific domains.

## Environment Details
- The customer is using Netwrix Endpoint Protector.
- The specific feature in question is related to Device Control and Content Aware Protection.

## Troubleshooting Steps
1. Provided guidance on configuring the "Allowed domains for Google Business accounts" under "Content Aware Protection > Deep Packet Inspection".
2. Suggested setting up a Content Aware Protection (CAP) policy to block file uploads while allowing access to certain URLs or domains.
3. Clarified that allowing attachments on web emails based on domain would not function as intended.
4. Engaged in email communications to confirm understanding and gather additional requirements.
5. Scheduled a remote session to provide further assistance and clarification on the deployment of the DPI feature, which requires certificate installation.

## Root Cause
The issue stemmed from a lack of clarity on how to configure the Netwrix Endpoint Protector to meet the specific requirements of blocking personal email access while allowing certain domains. The customer needed detailed guidance on the configuration process.

## Solution
The issue was resolved by:
- Providing detailed instructions on how to set up the necessary rules within the Netwrix Endpoint Protector.
- Conducting a remote session to walk the customer through the configuration process, ensuring they understood how to implement the DPI feature and the associated certificate requirements.

## Notes
- It is important to note that while the CAP policy can block file uploads, it does not support allowing attachments on web emails based on domain.
- Future users should be aware of the need for certificates when deploying Deep Packet Inspection features, as this may require additional setup steps.