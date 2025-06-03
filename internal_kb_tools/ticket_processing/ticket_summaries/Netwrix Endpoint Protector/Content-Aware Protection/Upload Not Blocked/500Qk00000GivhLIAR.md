## Ticket Metadata
- **Ticket ID:** 500Qk00000GivhLIAR
- **Case Number:** 423099
- **Status:** Closed - Resolved
- **Account/Company:** PeopleStrong
- **Contact Name:** Rohit Nawani
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** Upload Not Blocked
- **Version:** Endpoint Protector Server v5.9.1.0 with Endpoint Protector client v6.1.0.600

## Problem Description
The customer requested an update to their Data Loss Prevention (DLP) policies to restrict data uploads to all external domains, except for the domain peoplestrong.com. They required that uploads to this domain be allowed while blocking all other domains.

## Environment Details
- The customer was using an older version of the Endpoint Protector product:
  - **Server Version:** 5.9.1.0
  - **Client Version:** 6.1.0.600
- Browsers tested included Chrome, Edge, and Firefox.

## Troubleshooting Steps
1. Verified the SSL certificate of Endpoint Protector was not imported into the web browsers.
2. Checked the configuration of the Content Aware Protection policy.
3. Confirmed that Deep Packet Inspection and Stealthy DPI Driver were enabled.
4. Discussed the absence of a proxy server in the customer's environment.
5. Recommended upgrading the Endpoint Protector Server and Client to the latest versions:
   - **Server Upgrade:** From 5.9.1.0 to 5.9.4.0
   - **Client Upgrade:** From 6.1.0.600 to 6.2.3.1010
6. Suggested performing a snapshot of the current state of the EPP appliance before applying updates.

## Root Cause
The issue was caused by the SSL certificate of Endpoint Protector not being imported into the web browsers, which prevented the whitelisted domain from being recognized and allowed for uploads. This was compounded by the use of an outdated version of the Endpoint Protector software.

## Solution
The issue was resolved by upgrading the Endpoint Protector Server and Client to the recommended versions. After the upgrade, the customer was able to successfully implement the DLP policy that allowed uploads to peoplestrong.com while blocking all other domains.

## Notes
- It is crucial to perform a snapshot of the EPP appliance before applying any updates to ensure a quick rollback if necessary.
- Future cases should verify SSL certificate importation in browsers when similar upload restrictions are requested.
- Always recommend customers to keep their software updated to avoid compatibility issues.