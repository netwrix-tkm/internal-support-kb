## Ticket Metadata
- **Ticket ID:** 500Qk00000ICLvzIAH
- **Case Number:** 426765
- **Status:** Closed - Resolved
- **Account/Company:** QUALITY ASSISTANCE S.A.
- **Contact Name:** Guillaume Mainil
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** CAP Policies
- **Version:** NONE

## Problem Description
The customer reported an issue with the new Outlook client where their policy to limit Teams attachments was not functioning as expected. The issue did not occur with the previous version of the Outlook client.

## Environment Details
- The customer was using the new Outlook client.
- The policy in question was related to limiting uploads through Microsoft Teams.

## Troubleshooting Steps
1. The customer provided initial details about the issue, indicating that the new Outlook client was not recognizing attachments correctly.
2. Netwrix Support suggested enabling DPI (Deep Packet Inspection) for a test machine to see if it would resolve the issue.
3. A remote session was proposed to further investigate the problem.

## Root Cause
The new Outlook client was not recognized by the Netwrix Endpoint Protector as an Outlook application but was instead identified as an Edge browser. This misidentification caused the content policy to block attachments that were actually intended for Outlook.

## Solution
The customer resolved the issue by implementing a DPI bypass for `outlook.office.com`. This adjustment allowed the new Outlook client to function correctly with the existing content policies.

## Notes
- It is important to note that the new Outlook client may not be recognized as a standard Outlook application by the Endpoint Protector, which could lead to similar issues in the future.
- Customers should be advised to check the recognition of applications by Endpoint Protector when deploying new software versions to avoid disruptions in policy enforcement.