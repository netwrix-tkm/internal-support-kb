## Ticket Metadata
- **Ticket ID:** 500Qk00000OfHrvIAF
- **Case Number:** 443775
- **Status:** Closed - Resolved
- **Account/Company:** Amphenol Aerospace
- **Contact Name:** Carl Hippenstiel
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Access Error
- **Version:** Not specified

## Problem Description
The customer reported a loss of console access to the Endpoint Protector server after setting the Fully Qualified Domain Name (FQDN) in the Server Certificate Stack. The customer was unable to SSH into the server using the root account and could not access the console via IP or FQDN, receiving a "connection refused" error.

## Environment Details
- The issue occurred on a non-production server.
- The server certificate stack was modified, and a new certificate was generated.

## Troubleshooting Steps
1. The customer set the server certificate stack and regenerated the certificate, which led to the loss of console access.
2. An IP change was made, but it did not regenerate the certificate to the default settings.
3. The support technician reached out to DevOps for assistance.
4. A backup was restored during testing, but it was ultimately unnecessary as the customer had a snapshot available.
5. The customer was advised to restore the appliance to a previous state.

## Root Cause
The root cause of the issue was the modification of the server certificate stack and the regeneration of the certificate, which resulted in the loss of access to the console. The IP change did not trigger a default regeneration of the certificate.

## Solution
The issue was resolved by redeploying the appliance. After the redeployment, the server functioned as intended, restoring access to the console.

## Notes
- It is important to ensure that any changes to the server certificate stack are carefully planned and tested, especially in production environments.
- Always maintain backups and snapshots before making significant changes to server configurations to facilitate quick recovery in case of issues.