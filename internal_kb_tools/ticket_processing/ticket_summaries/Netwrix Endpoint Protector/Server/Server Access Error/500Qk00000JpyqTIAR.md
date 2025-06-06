## Ticket Metadata
- **Ticket ID:** 500Qk00000JpyqTIAR
- **Case Number:** 430613
- **Status:** Closed - Resolved
- **Account/Company:** Brightidea
- **Contact Name:** Michael Corridon
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Access Error
- **Version:** 4.1

## Problem Description
The customer reported that they could no longer access their Endpoint Protector (EPP) site to retrieve the server ID. They referenced a previous Netwrix Support Ticket (#00414675) for additional context.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Age of the Issue:** 4.1

## Troubleshooting Steps
1. Verified the customer's access to the EPP site.
2. Checked the SSL protocol settings in the configuration file.
3. Reviewed the referenced support ticket (#00414675) for related issues and resolutions.

## Root Cause
The issue was caused by the use of an unsupported SSL protocol version (TLSv1), which prevented access to the EPP site.

## Solution
The resolution involved changing the SSL protocol version from TLSv1 to TLSv1.2 in the configuration file. This update allowed the customer to regain access to the EPP site successfully.

## Notes
- Ensure that all future configurations use TLSv1.2 or higher to avoid similar access issues.
- Regularly review and update SSL protocol settings as part of system maintenance to ensure compatibility with security standards.