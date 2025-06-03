## Ticket Metadata
- **Ticket ID:** 500Qk00000CgcUzIAJ
- **Case Number:** 414117
- **Status:** Closed - Resolved
- **Account/Company:** Cobo
- **Contact Name:** Kenneth Lee
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** DPI - Other
- **Version:** 3.1

## Problem Description
The customer reported a significant number of 'DPI Bypassed Traffic' events in their environment and sought clarification on the nature of these events, as the user manual did not provide sufficient information.

## Environment Details
- The issue was observed in a Netwrix Endpoint Protector environment, specifically related to the Content-Aware Protection component.

## Troubleshooting Steps
1. The customer reviewed the Endpoint Protector user manual for information regarding 'DPI Bypassed Traffic' but found no relevant details.
2. The support team provided a response explaining the DPI bypass functionality.

## Root Cause
The DPI bypass occurs when the DPI process does not attach to connections deemed irrelevant to the Endpoint Protector client, resulting in bypass logs being generated.

## Solution
The support team clarified that the DPI bypass is a designed feature of the Endpoint Protector. To manage the visibility of these bypass logs, the customer was advised to adjust the settings in the Device Control section under Global Settings.

## Notes
- If the customer wishes to reduce the number of bypass logs, they can modify the settings as suggested.
- It is important for users to understand that bypass logs are a normal part of the DPI functionality and are not indicative of a malfunction.