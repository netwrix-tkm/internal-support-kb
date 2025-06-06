## Ticket Metadata
- **Ticket ID:** 500Qk00000PGErpIAH
- **Case Number:** 445461
- **Status:** Closed - Resolved
- **Account/Company:** Royal Bank of Canada (RBC)
- **Contact Name:** Justin Olson
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Windows File Systems
- **Feature:** Access Auditing
- **Version:** 11.6

## Problem Description
The customer reported that the process for implementing self-signed certificates for FSAA scans was not functioning as expected. The issue was escalated for further investigation.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Build Number:** 11.6.0.368

## Troubleshooting Steps
1. Export the CA's root certificate and any required intermediate CA certificates to .cer files.
2. Import the exported certificates into the FSAA Certificate Authority store on the NEA console and each proxy.
3. Create a client Certificate Signing Request (CSR) on the NEA console using the FSAACertificateManager.exe tool.
4. Sign the CSR with the desired CA to create a signed client certificate and copy it to the NEA console.
5. Import the signed client certificate into the certificate store on the NEA console.
6. Create a server CSR on each proxy using the FSAACertificateManager.exe tool.
7. Sign the proxy's CSR with the desired CA to create a signed server certificate and copy it to the proxy.
8. Import the signed server certificate into the FSAA managed certificate store on the proxy.
9. Remove all generated files (e.g., PFX, CER, and Key files) from their output destinations.
10. Update FSAA queries to use the Manual certificate exchange option in the FSAA job configuration UI.

## Root Cause
The issue was caused by an incorrect configuration where the certificate was stored in the general Certificate Authority store instead of the FSAA Certificate Authority store, which is required for the FSAA setup process. This absence of the certificate in the correct store prevented the FSAA scans from functioning correctly.

## Solution
The resolution involved the following steps:
1. Manually exported the correct certificate from the general Certificate Authority.
2. Imported the certificate into the FSAA Certificate Authority store on the NEA console and each proxy.
3. Ensured all steps were performed using the appropriate user accounts for the NEA console and proxy scanner service.
4. Followed the documented process using the FSAACertificateManager.exe tool to maintain consistency and avoid unforeseen behavior.

## Notes
- It is critical to ensure that certificates are stored in the correct FSAA Certificate Authority store to avoid similar issues in the future.
- The use of the FSAACertificateManager.exe tool is essential for maintaining consistency with the documented process.
- No additional updates to the documentation were deemed necessary, but the resolution steps have been documented to prevent recurrence of the initial configuration error.