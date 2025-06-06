## Ticket Metadata
- **Ticket ID:** 500Qk00000FrYhGIAV
- **Case Number:** 421215
- **Status:** Closed - Resolved
- **Account/Company:** ZS
- **Contact Name:** Manpreet Singh
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Performance
- **Version:** NONE

## Problem Description
The customer reported confusion regarding the contents of the backups being taken on external storage in the ZS environment. Specifically, they wanted clarification on whether the entries labeled "Shadows," "Audit Log Backup," and "System Backups" included appliance configuration backups or if they were solely logs.

## Environment Details
- **External Storage:** Hosted in ZS environment
- **Backup Types:** Shadows, Audit Log Backup, System Backups

## Troubleshooting Steps
1. Reviewed the backup entries listed by the customer.
2. Analyzed the documentation related to backup types in Netwrix Endpoint Protector.
3. Clarified the definitions and purposes of "Shadows," "Audit Log Backup," and "System Backups."
4. Provided detailed explanations to the customer regarding the nature of each backup type.

## Root Cause
The confusion arose from a lack of clarity in the documentation regarding what each backup type contained, leading to uncertainty about whether appliance configuration backups were included.

## Solution
The issue was resolved by providing the customer with detailed information about the backup types:
- **Shadows:** Typically contain snapshots of the system state.
- **Audit Log Backup:** Contains logs of activities and changes made within the system.
- **System Backups:** Generally include system files and configurations but do not specifically denote appliance configuration backups.

The customer was informed that appliance configuration backups are separate and not included in the mentioned backup types.

## Notes
- It is important to ensure that documentation clearly defines backup types and their contents to prevent similar confusion in the future.
- Consider providing a summary of backup types in the user interface or as part of the backup configuration process to enhance user understanding.