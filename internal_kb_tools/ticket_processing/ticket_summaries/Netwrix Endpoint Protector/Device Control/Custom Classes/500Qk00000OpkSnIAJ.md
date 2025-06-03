## Ticket Metadata
- **Ticket ID:** 500Qk00000OpkSnIAJ
- **Case Number:** 444151
- **Status:** Closed - Resolved
- **Account/Company:** SHW AG
- **Contact Name:** Christian Kopf
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Custom Classes
- **Version:** NONE

## Problem Description
The customer, Christian Kopf from SHW AG, requested assistance on how to move their EPP virtual appliance from Nutanix to VMware, specifically inquiring about the need for SSH login to facilitate this process.

## Environment Details
- **Current Platform:** Nutanix
- **Target Platform:** VMware
- **Product in Use:** Netwrix Endpoint Protector (EPP)

## Troubleshooting Steps
1. The customer was advised against directly moving the virtual appliance via SSH.
2. Recommended a better approach: deploy a new EPP appliance on VMware.
3. Informed the customer that migration could be performed using System Backup V2 along with an Audit Log Backup.
4. Confirmed that the customer activated trial licenses for the new setup.

## Root Cause
The initial inquiry stemmed from a misunderstanding of the migration process between different virtualization platforms. The customer was looking for a direct transfer method, which was not the optimal approach.

## Solution
The issue was resolved by guiding the customer to deploy a new EPP appliance on VMware and perform the migration using System Backup V2 and Audit Log Backup. The customer confirmed that all steps worked fine after activating the trial licenses.

## Notes
- It is important to inform customers about the best practices for migrating virtual appliances between different platforms to avoid complications.
- Always recommend using the latest backup and migration tools provided by Netwrix for seamless transitions.