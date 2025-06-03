## Ticket Metadata
- **Ticket ID:** 500Qk00000PKBnKIAX
- **Case Number:** 445544
- **Status:** Closed - Resolved
- **Account/Company:** Kettlitz-Chemie GmbH & Co. KG
- **Contact Name:** Johannes Herrmann
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Install/Uninstall
- **Version:** 19.05

## Problem Description
The customer reported that users were unable to download the Endpoint Protector client software from the web address `***/client.php/software`, as it was not accessible to them. However, the admin console was accessible via HTTPS at the IP address 172.16.16.101.

## Environment Details
- The customer was using version 19.05 of Netwrix Endpoint Protector.

## Troubleshooting Steps
1. Requested additional details from the customer since the initial description lacked specificity.
2. Confirmed that the customer was having trouble accessing the download link for the client software.
3. Inquired about the server version to assist with troubleshooting.
4. Informed the customer that the method they were attempting to use for client installation was deprecated.
5. Recommended downloading the client software directly from the user interface (UI) instead.

## Root Cause
The issue stemmed from the customer attempting to use a deprecated method (`***/client.php/software`) for downloading the client software, which is no longer supported.

## Solution
The issue was resolved by informing the customer that the previous method of downloading the client software was deprecated. The recommended solution was to download the client software directly from the UI. Additionally, manuals for the various deployment types were provided to assist the customer.

## Notes
- It is important to inform customers about deprecated methods of installation to prevent confusion and ensure they use supported methods.
- Always check for the latest documentation and manuals related to deployment types to provide comprehensive support.