## Ticket Metadata
- **Ticket ID:** 500Qk00000BPtKlIAL
- **Case Number:** 410904
- **Status:** Closed - Resolved
- **Account/Company:** Adarsh Co-operative Bank Ltd.
- **Contact Name:** Kundan Solanki
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device Rights
- **Version:** Client Version: 6.2.2.1, Server Version: 5.9.3.0

## Problem Description
The customer reported an issue with accessing a Kodak scanner on a system protected by Netwrix's Data Loss Prevention (DLP) software. The scanner was accessible when the DLP software was uninstalled, indicating that the DLP settings were blocking access.

## Environment Details
- **System Name:** PC_240_029
- **IP Address:** 172.21.240.29

## Troubleshooting Steps
1. The customer was asked to provide details about the server and client versions.
2. The customer confirmed that the operation being blocked was the use of a new USB scanner (Kodak i2400).
3. The support team advised checking the Reports and Analysis page for logs related to the blocked operation.
4. The customer was instructed to manage device rights under Device Control and ensure that the scanner was allowed.
5. The support team suggested checking Global Rights for printers to ensure they were set to allow access.
6. The customer confirmed that the scanner was still inaccessible despite following the above steps.
7. The support team recommended disabling the MTP (Media Transfer Protocol) feature on the individual computer to see if that resolved the issue.

## Root Cause
The issue was caused by the MTP feature being enabled in the DLP settings, which interfered with the operation of the Kodak scanner.

## Solution
The problem was resolved by disabling the MTP feature on the specific computer where the scanner was connected. This allowed the scanner to be accessed without needing to uninstall the DLP software. The settings were adjusted for the individual system rather than changing global settings.

## Notes
- It is important to check device-specific settings in the DLP software when users report issues with device access.
- Disabling MTP should be considered a viable troubleshooting step for similar issues involving USB devices that are being blocked by DLP software.
- Ensure that any changes made to DLP settings are documented to avoid confusion in future support cases.