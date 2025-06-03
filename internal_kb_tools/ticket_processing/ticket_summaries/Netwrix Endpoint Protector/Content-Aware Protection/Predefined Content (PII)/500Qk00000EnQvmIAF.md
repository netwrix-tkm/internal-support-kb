## Ticket Metadata
- **Ticket ID:** 500Qk00000EnQvmIAF
- **Case Number:** 418863
- **Status:** Closed - Resolved
- **Account/Company:** Aviva Brasil
- **Contact Name:** Giovani Paganini
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** Predefined Content (PII)
- **Version:** Not specified

## Problem Description
The customer reported experiencing numerous false positives where number sequences were incorrectly identified as ID/BR (identification numbers), which adversely affected their production policies. Specifically, small number sequences were sometimes flagged, and the customer sought clarification on how predefined content detection works, particularly regarding the Brazilian CPF format.

## Environment Details
- The issue was related to the detection of predefined content (PII) within the Netwrix Endpoint Protector platform.
- The Brazilian CPF format (e.g., 123.456.789-10) can vary in punctuation and has a mathematical verification process.

## Troubleshooting Steps
1. Reviewed the predefined content detection settings within the Netwrix Endpoint Protector.
2. Analyzed the patterns of false positives to identify common characteristics.
3. Investigated the allow list configuration for the customer's domain to ensure proper functionality.
4. Enabled the "Ignore Trust" option to address HSTS warnings.

## Root Cause
The false positives were primarily due to the predefined content detection algorithm misidentifying certain number sequences as ID/BR. The evolving nature of Deep Packet Inspection (DPI) technology contributed to the inconsistencies in detection.

## Solution
Enabling the "Ignore Trust" option resolved the HSTS warnings and allowed the system to function without validating certificate trust against the Root certificate. This adjustment helped mitigate the negative impacts of the DPI functionality, reducing the occurrence of false positives.

## Notes
- The "Ignore Trust" option should be used with caution, as it bypasses standard certificate validation processes.
- Future configurations should consider the unique formats of identification numbers in different regions to minimize false positives.
- Regular reviews of predefined content settings may be necessary to adapt to changes in data patterns and regulatory requirements.