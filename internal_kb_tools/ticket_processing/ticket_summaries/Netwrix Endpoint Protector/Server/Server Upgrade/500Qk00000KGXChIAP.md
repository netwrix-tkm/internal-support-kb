## Ticket Metadata
- **Ticket ID:** 500Qk00000KGXChIAP
- **Case Number:** 431226
- **Status:** Closed - Resolved
- **Account/Company:** South Carolina Federal Credit Union
- **Contact Name:** Dave Haertel
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Upgrade
- **Version:** 5.9.4.1

## Problem Description
The customer reported an error message encountered during an attempt to upgrade to version 5.9.4.1 of the Netwrix Endpoint Protector. The error message indicated that the maximum number of retries for the update had been reached, resulting in the update being skipped.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Server

## Troubleshooting Steps
1. The support team received the error message from the client: 
   ```
   "Some problems occurred during installation. Please Contact Support. (ERROR: 2 - Number of maximum retries for this update reached, skipping this update...)"
   ```
2. An email was sent to the client advising them to reattempt the upgrade to version 5.9.4.1.
3. The client scheduled a patch window for January 10, 2025, to retry the upgrade.

## Root Cause
The root cause of the issue was identified as the maximum retry limit being reached during the installation process of the upgrade to version 5.9.4.1. This typically occurs due to underlying issues with the installation environment or conflicts that prevent the update from completing successfully.

## Solution
The customer successfully applied the EPP update to version 5.9.4.1 during the scheduled patch window. Following the successful upgrade, the customer confirmed that the issue was resolved, and the support ticket was closed.

## Notes
- It is important to ensure that the environment is prepared for upgrades, including checking for any potential conflicts or prerequisites that may affect the installation process.
- Future upgrade attempts should be monitored closely to avoid reaching the maximum retry limit, which can lead to skipped updates and additional troubleshooting.