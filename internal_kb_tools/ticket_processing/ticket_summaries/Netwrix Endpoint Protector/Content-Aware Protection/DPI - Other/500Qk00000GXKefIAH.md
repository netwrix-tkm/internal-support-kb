## Ticket Metadata
- **Ticket ID:** 500Qk00000GXKefIAH
- **Case Number:** 422664
- **Status:** Closed - Resolved
- **Account/Company:** Booking.com
- **Contact Name:** Serhat Demir
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** DPI - Other
- **Version:** Not specified

## Problem Description
The customer, Serhat Demir from Booking.com, requested guidance on how to install Deep Packet Inspection (DPI) CA certificates on Ubuntu endpoints for their Endpoint Protection Platform (EPP) pilot. They noted that while the process for Mac and Windows was clear, they could not find documentation for Linux, specifically Ubuntu.

## Environment Details
- **Operating System:** Ubuntu
- **DPI CA Certificate Setting:** Manually set for auto-refresh

## Troubleshooting Steps
1. Reviewed existing EPP documentation for Linux certificate installation.
2. Confirmed the process for Mac (Keychain store) and Windows (automatic trust).
3. Engaged with the DevOps team to gather information on CA certificate management for Ubuntu.
4. Provided instructions for installing CA certificates on Debian-based systems (like Ubuntu).

## Root Cause
The lack of documentation regarding the installation of DPI CA certificates on Ubuntu endpoints led to confusion for the customer. The existing documentation did not cover the specific steps required for Linux environments.

## Solution
The following steps were provided to the customer for installing the DPI CA certificate on Ubuntu:

```bash
# Download the archived certificates from the EPP server
unzip ClientCerts.zip

# Use cacert.pem from the archive
# For Debian-based systems (like Ubuntu)
sudo cp cacert.pem /usr/local/share/ca-certificates/cacert.crt
# Important: Ensure the file has a .crt extension
sudo update-ca-certificates
```

Additionally, reference links were shared for further guidance:
- [Install a Root CA Certificate in the Trust Store (Ubuntu)](https://ubuntu.com/server/docs/install-a-root-ca-certificate-in-the-trust-store)
- [Configure CA Trust List (Red Hat)](https://www.redhat.com/en/blog/configure-ca-trust-list)
- [CA Certificate Management (Baeldung)](https://www.baeldung.com/linux/ca-certificate-management)

## Notes
- Ensure that any future documentation tasks related to this issue are raised through the Help Center portal.
- The documentation for DPI CA certificate installation on Linux was updated following this case to prevent similar issues in the future.