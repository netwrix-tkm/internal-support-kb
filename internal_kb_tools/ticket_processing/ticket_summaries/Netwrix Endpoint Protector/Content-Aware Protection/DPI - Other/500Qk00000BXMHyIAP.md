## Ticket Metadata
- **Ticket ID:** 500Qk00000BXMHyIAP
- **Case Number:** 411272
- **Status:** Closed - Resolved
- **Account/Company:** OneMain Holdings Inc.
- **Contact Name:** Imran Khan
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** DPI - Other
- **Version:** 3.0.4.1000

## Problem Description
The customer reported that Deep Packet Inspection (DPI) was not functioning correctly for Mac users. Specifically, when users entered sensitive information into certain web applications using Chrome, no alerts were generated, and the system did not block the input. However, file uploads containing sensitive information were correctly blocked and reported.

## Environment Details
- The issue was observed on multiple Mac machines using the Netwrix Endpoint Protector.
- The DPI feature was enabled, but there were inconsistencies in alert generation and blocking behavior.

## Troubleshooting Steps
1. Verified the DPI settings for the affected users.
2. Tested the functionality with the latest version of the EPP agent (3.0.4.1000).
3. Conducted tests with both file uploads and text inputs to identify discrepancies in alert generation.
4. Checked for any misconfigurations in the URL categories and DPI settings.
5. Gathered logs during testing to analyze the behavior of the EPP agent.

## Root Cause
The root cause was identified as a misconfiguration in the URL category names, which contained trailing spaces. This caused the DPI feature to malfunction, leading to the failure in blocking sensitive text inputs while allowing file uploads to be processed correctly.

## Solution
The issue was resolved by removing the trailing spaces from the URL category names in the EPP configuration. After making this adjustment, the DPI functionality was tested again, and it successfully blocked sensitive text inputs and generated alerts as expected.

## Notes
- Ensure that URL category names do not contain trailing spaces to avoid similar issues in the future.
- Regularly verify the configuration settings for DPI and URL categories to maintain proper functionality.
- If issues persist, gather logs and consult with engineering for further analysis.