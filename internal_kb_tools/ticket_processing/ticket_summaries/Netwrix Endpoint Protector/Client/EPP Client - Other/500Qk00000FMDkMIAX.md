```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000FMDkMIAX
- **Case Number:** 420107
- **Status:** Closed - Resolved
- **Account/Company:** HQLAx
- **Contact Name:** Yacine BOUMEKIK
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** EPP Client - Other
- **Version:** 3.0.4.1003

## Problem Description
A specific user (S/N: LRLY71T09K) reported an issue where they could not browse any websites using any browser (Safari, Firefox, Chrome). The pages would continuously load but ultimately return an error. The issue was linked to the Endpoint Protector certificate status, which was marked as "NO" for both "Available" and "Trusted" in the client application, while the server side showed the certificate as "Trusted."

## Environment Details
- User's device: MacBook Air
- Global policy applied uniformly across users in the organization.

## Troubleshooting Steps
1. Verified browsing capabilities using terminal commands (CURL, PING, TRACEROUTE) which returned successful results.
2. Checked the certificate status in both the client application and server.
3. Restarted the user's MacBook, which temporarily resolved the issue.
4. Removed the Endpoint Protector transparent proxy, which restored web browsing functionality.
5. Investigated logs for error messages, particularly "connection not found in NAT state table."

## Root Cause
The issue was identified as being related to the Endpoint Protector transparent proxy configuration, which caused the certificate status to incorrectly reflect as "NO" in the client application. This misconfiguration led to the inability to browse websites.

## Solution
The issue was resolved by updating the Endpoint Protector client to version 3.0.4.1003, which included fixes for the identified problems. The customer confirmed that this version resolved the issue after testing on one computer, with plans to monitor other devices for similar occurrences.

## Notes
- The issue appeared intermittently, typically once a week, suggesting that monitoring is necessary to ensure the fix is effective across all devices.
- Future users experiencing similar symptoms should check the certificate status in both the client and server applications and consider updating to the latest version of the Endpoint Protector client.
- The error message "connection not found in NAT state table" should be investigated as it may indicate underlying network issues that could affect connectivity.
```