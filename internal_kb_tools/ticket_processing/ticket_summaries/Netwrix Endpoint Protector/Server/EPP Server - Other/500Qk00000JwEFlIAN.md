## Ticket Metadata
- **Ticket ID:** 500Qk00000JwEFlIAN
- **Case Number:** 430786
- **Status:** Closed - Resolved
- **Account/Company:** Canal Insurance
- **Contact Name:** Brian Illner
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** Not specified

## Problem Description
The customer inquired whether Google Authenticator was the only supported two-factor authentication (2FA) app for administrators, and if other options like Microsoft Authenticator or third-party applications such as DUO were also compatible.

## Environment Details
- The 2FA mechanism implemented in Netwrix Endpoint Protector (EPP) relies on the standard format for Time-Based One-Time Password (TOTP) systems.

## Troubleshooting Steps
1. Reviewed the 2FA implementation details in EPP.
2. Confirmed that the generated QR code is compatible with any mobile app that supports TOTP-based two-factor authentication.
3. Communicated findings to the customer regarding the compatibility of various authenticator apps.

## Root Cause
The initial confusion stemmed from the customer's assumption that only Google Authenticator was supported. However, the TOTP standard allows for compatibility with multiple authenticator applications.

## Solution
The issue was resolved by clarifying to the customer that they could use any TOTP-compatible authenticator app, not just Google Authenticator. The customer successfully used an alternative authenticator app.

## Notes
- It is important to inform customers that the TOTP standard allows for flexibility in choosing authenticator apps.
- Future inquiries regarding 2FA compatibility should emphasize the TOTP standard's broad support for various applications.