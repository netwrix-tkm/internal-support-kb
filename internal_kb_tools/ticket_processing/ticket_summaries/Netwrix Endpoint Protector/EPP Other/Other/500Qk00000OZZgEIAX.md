## Ticket Metadata
- **Ticket ID:** 500Qk00000OZZgEIAX
- **Case Number:** 443487
- **Status:** Closed - Resolved
- **Account/Company:** Satcom Infotech
- **Contact Name:** Thanu shree
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Other
- **Version:** NONE

## Problem Description
The client reported an issue where they were unable to block custom content and Social Security Numbers (SSN) using the Content Aware Protection (CAP) policy.

## Environment Details
- The client was using Netwrix Endpoint Protector.
- The specific configuration settings for the CAP policy were initially misconfigured.

## Troubleshooting Steps
1. Conducted a remote session with the client to review the CAP policy settings.
2. Identified that the Global Threshold was misconfigured.
3. Recommended using content rule detection for more granular control and setting up thresholds individually.
4. Demonstrated the "block and remediate" option to allow clients to bypass the CAP policy if needed.
5. Scheduled follow-up remote sessions for further testing and adjustments.
6. Assisted in creating a new CAP policy to restrict PII/CreditCard content.
7. Tested the new policy with files containing sensitive and non-sensitive information.
8. Adjusted the Optical Character Recognition (OCR) settings to block images with sensitive data while allowing non-sensitive screenshots.

## Root Cause
The issue was primarily due to the misconfiguration of the Global Threshold in the CAP policy, which prevented the effective blocking of custom content and SSN numbers.

## Solution
The issue was resolved by:
- Correcting the Global Threshold settings.
- Implementing content rule detection for more precise control over what content was blocked.
- Successfully creating and testing a new CAP policy that effectively restricted sensitive information, including SSN numbers and PII/CreditCard content.
- Adjusting OCR settings to ensure only images with sensitive data were blocked.

## Notes
- Ensure that the Global Threshold is correctly configured in future CAP policies to avoid similar issues.
- Consider using content rule detection for more granular control when dealing with sensitive information.
- Always test new policies with both sensitive and non-sensitive files to confirm the desired behavior.