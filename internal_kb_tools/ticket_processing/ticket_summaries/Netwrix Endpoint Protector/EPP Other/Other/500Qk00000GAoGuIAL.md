## Ticket Metadata
- **Ticket ID:** 500Qk00000GAoGuIAL
- **Case Number:** 421891
- **Status:** Closed - Resolved
- **Account/Company:** Tradebyte Software GmbH
- **Contact Name:** Mesut Gungor
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Other
- **Version:** NONE

## Problem Description
The customer reported encountering an SSL error while visiting the Netwrix support webpage. Upon checking the SSL certificate, it displayed an unexpected Common Name (CN) field pointing to `slack-vrt.bugcrowd.net`, raising concerns about potential misconfiguration or vulnerabilities in the server's certificate handling.

## Environment Details
- The issue was observed on the Netwrix support webpage.
- The customer was using a DPI (Deep Packet Inspection) client, which may have contributed to the problem.

## Troubleshooting Steps
1. The customer was advised to restart their browser after enabling the DPI client.
2. The support team requested confirmation on whether the issue occurred consistently across different browsers.
3. The customer was asked to provide logs and a recording of the issue if it persisted after the browser restart.
4. The support team monitored the situation and escalated the ticket for further investigation.

## Root Cause
The issue was identified as a caching problem within the browser. The incorrect certificate was displayed due to the browser not refreshing its cache properly after the DPI client was enabled.

## Solution
The issue was resolved by advising the customer to restart their browser, which cleared the cache and allowed the correct SSL certificate to be displayed. The customer confirmed that the problem did not reproduce after the restart.

## Notes
- Ensure that users are aware of the importance of restarting their browsers after making changes to DPI settings or similar configurations.
- Monitor for any similar reports to determine if this is a recurring issue that may require further investigation or a more permanent fix.