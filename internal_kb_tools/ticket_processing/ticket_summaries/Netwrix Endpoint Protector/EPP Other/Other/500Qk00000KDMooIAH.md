## Ticket Metadata
- **Ticket ID:** 500Qk00000KDMooIAH
- **Case Number:** 431162
- **Status:** Closed - Resolved
- **Account/Company:** Sound and Vision Studios
- **Contact Name:** Ayaz Ahmad Ansari
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Other
- **Version:** 13.3

## Problem Description
The customer reported that web browsing suddenly stopped working on Mac systems. They requested a remote session to investigate the issue further.

## Environment Details
- **Operating System:** MacOS
- **Browser:** Google Chrome
- **Application:** Outlook Webmail

## Troubleshooting Steps
1. Conducted a remote session to diagnose the issue.
2. Verified the configuration of the Content Aware Protection (CAP) policy.
3. Attempted to attach a file type from the deny list to Outlook via Chrome, which resulted in a block.
4. Discussed the customer's understanding of CAP policy configuration.

## Root Cause
The issue was caused by a misconfiguration of the CAP policy, which was blocking certain file types from being attached in Outlook when using the Chrome browser.

## Solution
- Explained the functionality of the CAP policy to the customer.
- Assisted the customer in configuring the CAP policy to align with their requirements.
- Deselecting the Chrome browser from the exit points in the CAP policy allowed the customer to successfully upload the requested file in Outlook Webmail.

## Notes
- Ensure that customers are aware of how to configure CAP policies to prevent similar issues in the future.
- Recommend documenting the specific configurations made to the CAP policy for future reference.