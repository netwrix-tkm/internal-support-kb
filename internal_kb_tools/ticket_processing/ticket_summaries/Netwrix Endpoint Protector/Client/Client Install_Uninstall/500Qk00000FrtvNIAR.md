## Ticket Metadata
- **Ticket ID:** 500Qk00000FrtvNIAR
- **Case Number:** 421233
- **Status:** Closed - Resolved
- **Account/Company:** St. Vinzenz Klinik Pfronten
- **Contact Name:** Felix Behrendt
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Install/Uninstall
- **Version:** NONE

## Problem Description
The customer reported that after uninstalling the Endpoint Protector (EPP) from a PC and deleting it from the server, the keyboard remained locked. The intention was to reinstall EPP to reset the keyboard lock status, but the issue persisted.

## Environment Details
- The issue occurred on multiple PCs that had been prepared and were awaiting deployment.
- The keyboard lock was associated with the initial installation of EPP.

## Troubleshooting Steps
1. Uninstalled the EPP client from the PC using a deployment tool.
2. Deleted the EPP client from the server.
3. Attempted to reinstall the EPP client on the PC.
4. Verified if the keyboard lock status was reset after reinstallation.

## Root Cause
The local database associated with the EPP client was not removed during the uninstallation process because the client was uninstalled using a deployment tool, which did not clear all related data.

## Solution
To resolve the issue, it was necessary to manually remove the local database associated with the EPP client after uninstalling it. This ensured that upon reinstallation, the keyboard lock status would be reset correctly.

## Notes
- When uninstalling the EPP client using a deployment tool, ensure that all associated local databases are also removed to prevent issues with residual configurations.
- For future installations, consider using the standard uninstallation process to ensure complete removal of all components.