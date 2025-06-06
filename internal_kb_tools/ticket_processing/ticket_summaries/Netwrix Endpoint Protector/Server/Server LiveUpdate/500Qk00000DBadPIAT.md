## Ticket Metadata
- **Ticket ID:** 500Qk00000DBadPIAT
- **Case Number:** 415262
- **Status:** Closed - Resolved
- **Account/Company:** Fastco Canada
- **Contact Name:** Don Dee
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server LiveUpdate
- **Version:** NONE

## Problem Description
The customer, Shawn from Fastco Canada, reported that after installing EPP Hotfix #1.1 via the Live Update section of the EPP portal, the update still appeared as available under live updates, despite receiving a message indicating that the patch was successfully installed. Shawn sought clarification on whether this behavior was normal.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Server

## Troubleshooting Steps
1. Confirmed that the hotfix update still appeared in the list of "Available EPP Software Updates" after installation.
2. Assured the customer that the hotfix was successfully applied to the EPP appliance.
3. Informed the customer that no further action was required on their part.
4. Explained that the list of available updates would be cleared after applying the upgrade to version 5.9.4.0.

## Root Cause
The issue was identified as a normal behavior of the EPP system where updates remain listed as available even after successful installation. This is a known characteristic of the software until a subsequent version upgrade is performed.

## Solution
The issue was resolved by confirming to the customer that the hotfix was indeed applied successfully and that they could ignore the continued listing of the update under "Available EPP Software Updates." It was noted that this listing would be removed after the upgrade to version 5.9.4.0.

## Notes
- Customers should be informed that it is normal for updates to remain visible in the available updates list post-installation until a major version upgrade is applied.
- Future communications should reassure customers that successful installation messages are reliable, and they can disregard the available updates list in such scenarios.