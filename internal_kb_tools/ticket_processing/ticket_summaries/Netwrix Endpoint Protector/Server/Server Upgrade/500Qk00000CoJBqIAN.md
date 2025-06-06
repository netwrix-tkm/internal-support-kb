## Ticket Metadata
- **Ticket ID:** 500Qk00000CoJBqIAN
- **Case Number:** 414385
- **Status:** Closed - Resolved
- **Account/Company:** Uniphore
- **Contact Name:** Walt McClelland
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Upgrade
- **Version:** 1.0

## Problem Description
The customer reported that the EPP Server Hotfix #1.1, which includes important security updates, was unable to install properly. Although the console indicated that the patch was 100% installed, refreshing the screen showed that the same hotfix still needed to be applied. The customer attempted to reboot the server and reinstall the patch, but the issue persisted.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Server

## Troubleshooting Steps
1. The customer applied the hotfix through the console, which reported a 100% installation.
2. The customer refreshed the console to check for additional patches, only to find the same hotfix listed as needing installation.
3. The customer rebooted the server and attempted to reinstall the hotfix.
4. Technical support engaged with the customer to assess the situation and scheduled a remote session.

## Root Cause
The root cause of the issue was identified as the nature of the hotfix itself. Unlike other patches, EPP Server Hotfix #1.1 is not a versioned patch or upgrade, meaning it can be applied across different EPP server versions. As a result, the system continued to indicate that the hotfix needed to be installed even after it had been applied.

## Solution
During a remote session, it was confirmed that the hotfix had indeed been applied successfully, as evidenced by the logs on the EPP server. The technical support engineer advised the customer to disregard the persistent installation prompt for the hotfix, as it would be resolved in the next EPP server release or upgrade. The ticket was subsequently closed after confirming the successful application of the hotfix.

## Notes
- Customers should be aware that certain hotfixes may not behave like traditional versioned patches and may continue to appear as needing installation even after successful application.
- It is recommended to monitor for updates in future EPP server releases that may address this behavior.