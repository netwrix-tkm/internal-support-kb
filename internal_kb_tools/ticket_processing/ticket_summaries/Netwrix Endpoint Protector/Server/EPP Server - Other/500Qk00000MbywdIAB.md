## Ticket Metadata
- **Ticket ID:** 500Qk00000MbywdIAB
- **Case Number:** 437881
- **Status:** Closed - Resolved
- **Account/Company:** NBC Universal
- **Contact Name:** Easton Lindauer
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** 5.9.4.1

## Problem Description
The customer reported that after upgrading their EPP server to version 5.9.4.1, the HTTP non-encrypted version of the management page, which previously had a download link for clients, is no longer functioning.

## Environment Details
- The customer has been using the HTTP client download page for a long time without issues until the recent upgrade.
- The backend configuration showed a missing file compared to a test server: `/etc/nginx/sites-enabled/epp.http.nginx.conf`.

## Troubleshooting Steps
1. The customer was advised to reboot the EPP server to see if the issue would resolve itself.
2. A remote session was conducted to investigate the issue further.
3. The backend configuration files were checked, and it was noted that the HTTP client download page was not supported anymore.
4. The support team confirmed that the HTTP client download page was functioning on their test servers with the same version.
5. The support team raised the issue with the development team for further investigation.

## Root Cause
The HTTP client download page is no longer supported since the EPP server version 5.9.4.0. This change was part of security improvements implemented in the 5940 Server image. The removal of this feature was intentional, and there are no plans to reinstate it.

## Solution
The customer was informed that:
- The HTTP client download page is deprecated and will be removed completely.
- Clients can still be downloaded securely from the EPP Server.
- Customers are encouraged to upload clients to their own internal HTTP portal for distribution if needed.

## Notes
- The removal of the HTTP download page is a security measure, and users should transition to using HTTPS for secure downloads.
- Future versions of the EPP Server (5950 release) will include a redesigned client upload/download mechanism, which will not restore HTTP availability.