## Ticket Metadata
- **Ticket ID:** 500Qk00000FvRdyIAF
- **Case Number:** 421360
- **Status:** Closed - Resolved
- **Account/Company:** Central Bank of Trinidad and Tobago
- **Contact Name:** Keisha Lashley
- **Product:** Netwrix Enterprise Auditor
- **Component:** NEA Web Report Console
- **Feature:** SSL Certificate Management
- **Version:** 11.6

## Problem Description
The customer requested assistance in updating the TLS certificates for their Netwrix products and needed help generating a Certificate Signing Request (CSR) during a remote session.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Collector Code:** StealthAUDIT General
- **Product Version:** 11.6

## Troubleshooting Steps
1. Conducted a remote session to assist with the CSR generation.
2. Reviewed the error message received during the certificate import process:
   - "SSL Certificate add failed, Error: 1312" indicating that the private key was missing.
3. Provided commands to display SSL certificate information, delete the current certificate, and add the new SSL certificate:
   - Display SSL certificate info: 
     ```bash
     netsh http show sslcert
     ```
   - Delete current certificate:
     ```bash
     netsh http del sslcert ipport=0.0.0.0:8082
     ```
   - Add new SSL certificate:
     ```bash
     netsh http add sslcert ipport=0.0.0.0:8082 appid= certhash=
     ```
4. Shared relevant documentation links for updating certificate information.

## Root Cause
The issue was caused by the imported SSL certificate lacking a corresponding private key, which is essential for the certificate to function correctly.

## Solution
The issue was resolved by ensuring that the correct SSL certificate with an associated private key was used. The following steps were taken:
- The customer was guided to generate a CSR through their internal PKI team.
- Once the correct certificate was obtained, the commands provided were executed to delete the old certificate and add the new one, ensuring the private key was included.

## Notes
- It is crucial to ensure that any SSL certificate imported has a corresponding private key to avoid the "Private Key is missing" error.
- Future requests for CSR generation should be directed to the customer's internal PKI team, as Netwrix support does not handle CSR creation directly.