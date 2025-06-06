## Ticket Metadata
- **Ticket ID:** 500Qk00000IfDGhIAN
- **Case Number:** 427893
- **Status:** Closed - Resolved
- **Account/Company:** Zee Entertainment and Enterprises ltd
- **Contact Name:** Jagadish Ashadapu
- **Product:** Netwrix Endpoint Protector
- **Component:** System & Log Backups
- **Feature:** External Storage - Other
- **Version:** 6.1

## Problem Description
The customer requested assistance with configuring a weekly backup of system and logs to external storage via the EPP web interface. They confirmed that the Samba/Network share details and user credentials were correctly entered and that the external storage was accessible.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Backup Method:** Samba/Network share

## Troubleshooting Steps
1. Confirmed the correct configuration of Samba/Network share details and user credentials.
2. Verified accessibility of the external storage.
3. Scheduled a call to discuss best practices for system backup.
4. Provided information on the differences between snapshots in virtualization infrastructure and system backups through the EPP web portal.

## Root Cause
The issue was primarily related to the customer's need for clarification on the configuration and best practices for setting up regular backups, rather than a technical failure of the system.

## Solution
The issue was resolved through a discussion with the customer, where they were informed about the configuration for creating weekly backups and the importance of regular backups for server restoration. The customer successfully created a snapshot of the EPP server on Nutanix, confirming their understanding of the backup process.

## Notes
- Regular backups are essential for restoring the server in case of a breakdown.
- Ensure that all relevant team members are included in communications and meetings to facilitate smoother troubleshooting and resolution processes.