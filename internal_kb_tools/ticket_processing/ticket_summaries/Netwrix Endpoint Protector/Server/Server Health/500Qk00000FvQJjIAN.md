## Ticket Metadata
- **Ticket ID:** 500Qk00000FvQJjIAN
- **Case Number:** 421370
- **Status:** Closed - Resolved
- **Account/Company:** ServiceNow
- **Contact Name:** Arpitha Shetty
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Health
- **Version:** Not specified

## Problem Description
The customer reported that the server certificate in the Bastions Environment had expired and requested assistance in updating the certificate by generating a Certificate Signing Request (CSR).

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Environment Type:** Bastions Environment

## Troubleshooting Steps
1. Verified the expiration status of the server certificate.
2. Assisted the customer in generating a Certificate Signing Request (CSR).
3. Imported the new SSL certificate once it was issued.

## Root Cause
The issue was caused by the expiration of the existing server certificate, which required renewal to maintain secure communications.

## Solution
The SSL certificate was successfully imported after generating the CSR. This resolved the issue of the expired certificate, restoring secure access to the Bastions Environment.

## Notes
- Ensure to monitor certificate expiration dates proactively to avoid similar issues in the future.
- Consider implementing automated alerts for certificate renewals to streamline the process.