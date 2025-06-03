## Ticket Metadata
- **Ticket ID:** 500Qk00000BjxSDIAZ
- **Case Number:** 411692
- **Status:** Closed - Resolved
- **Account/Company:** Chronus
- **Contact Name:** Nagaganeshwar Anand
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Server
- **Feature:** EPP Server - Other
- **Version:** 5.9.3.0

## Problem Description
The customer requested remote support to enable HTTPS on their Endpoint Protector console due to previous issues with certificate management.

## Environment Details
- **Server Version:** 5.9.3.0
- **Previous Certificate Expiration Date:** February 18, 2024

## Troubleshooting Steps
1. Scheduled multiple remote sessions with the customer to assist with HTTPS configuration.
2. Verified the presence of the required SSL certificates (.crt and .key files).
3. Guided the customer to navigate to the EPP UI > Appliance > Server Maintenance to upload the certificates.
4. Attempted to refresh the console after certificate upload to check for HTTPS activation.
5. Discussed the need for a valid certificate and the importance of including BEGIN and END directives in the certificate content.
6. Requested screenshots of the console and any error messages displayed after the refresh.

## Root Cause
The initial issue was due to the use of an expired certificate. The customer had previously experienced issues with certificate management, leading to their request for assistance.

## Solution
- The customer successfully uploaded the correct certificates (.pem format) during the remote session.
- After refreshing the console, the HTTPS connection was established, resolving the issue.

## Notes
- Ensure that all certificates are valid and not expired before attempting to enable HTTPS.
- Always include the BEGIN and END directives when uploading certificates to avoid configuration issues.
- For future cases, verify the certificate expiration date and prompt the customer to generate new certificates if necessary.