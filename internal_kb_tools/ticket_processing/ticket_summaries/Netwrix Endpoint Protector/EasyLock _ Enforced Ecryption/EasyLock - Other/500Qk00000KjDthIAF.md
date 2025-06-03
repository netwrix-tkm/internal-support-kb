## Ticket Metadata
- **Ticket ID:** 500Qk00000KjDthIAF
- **Case Number:** 432536
- **Status:** Closed - Resolved
- **Account/Company:** OHSU - Oregon Health & Science University
- **Contact Name:** Jacques Perrolle
- **Product:** Netwrix Endpoint Protector
- **Component:** EasyLock / Enforced Encryption
- **Feature:** EasyLock - Other
- **Version:** Not specified

## Problem Description
The customer inquired about the specifications and limitations of the Enforced Encryption feature for Windows hosts, as they were considering its deployment. They also sought clarification on how using Enforced Encryption would affect their existing device control settings for Macs, which currently enforce Apple FileVault.

## Environment Details
- The customer is currently using EndPro for device control on Macs.
- Mac permissions are set to "Allow Access if TD level 3+, otherwise read only."
- The customer is transitioning between removable storage device encryption products.

## Troubleshooting Steps
1. Reviewed the customer's inquiry regarding the limitations of Enforced Encryption, including:
   - Single file size
   - Maximum encrypted volume size
   - Total number of files on an encrypted volume
   - Number of files in a folder on an encrypted volume
2. Clarified the implications of changing Trusted Device levels for Macs if Enforced Encryption is implemented.
3. Provided information based on guidance from Team Lead Iosif-Cristian.

## Root Cause
The customer was unable to find detailed specifications and limitations of the Enforced Encryption feature, leading to uncertainty about its compatibility with their existing Mac device control settings.

## Solution
The support team provided the customer with the necessary specifications and limitations of the Enforced Encryption feature. Additionally, they clarified that implementing Enforced Encryption would require changing the Mac permissions to "Allow Access if TD level 1+, otherwise read only," which could impact the enforcement of FileVault on Macs. The customer expressed satisfaction with the provided information and requested to close the ticket.

## Notes
- It is important to ensure that customers are aware of the implications of changing Trusted Device levels when integrating new encryption solutions.
- Future inquiries regarding Enforced Encryption should include a detailed explanation of its limitations and how it interacts with existing device control settings, especially in mixed OS environments.