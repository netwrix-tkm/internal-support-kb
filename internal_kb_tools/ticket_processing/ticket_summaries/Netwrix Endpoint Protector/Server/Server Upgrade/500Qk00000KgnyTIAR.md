## Ticket Metadata
- **Ticket ID:** 500Qk00000KgnyTIAR
- **Case Number:** 432412
- **Status:** Closed - Resolved
- **Account/Company:** Paramount Computer Systems
- **Contact Name:** Hussain Mansoor
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Upgrade
- **Version:** None

## Problem Description
The customer requested assistance with upgrading their two different Endpoint Protector (EPP) Consoles from older versions to the latest stable version. They sought clarification on the latest version, potential downtime, upgrade paths, backward compatibility, and the implications of upgrading the server while keeping the client on an older version.

## Environment Details
- **EPP MAC Version:** 5.5.0.0
- **EPP Windows Version:** 5.8.1.0
- **Current Server OS:** Ubuntu 14
- **Event Logs:** Approximately 16 million entries
- **Database Partitioning:** Not enabled

## Troubleshooting Steps
1. Identified the current versions of the EPP Consoles and the server environment.
2. Attempted to apply an update patch to version 5.6.5.0, which failed due to the limitations of Ubuntu 14 in handling large databases without partitioning.
3. Discussed potential upgrade paths and compatibility issues with the customer.

## Root Cause
The failure to upgrade the EPP Server from version 5.5.0.0 to 5.6.5.0 was primarily due to the outdated Ubuntu 14 operating system, which lacked the capability to partition the large database of 16 million event logs.

## Solution
The resolution involved a two-step migration process:
1. Migrate the EPP Server to an older appliance version 5.6.0.0 running on Ubuntu 18.
2. Subsequently upgrade to EPP Server version 5.9.3.0, with plans for a future migration to Ubuntu 22.04.

The customer successfully completed the migration to Ubuntu 18 and upgraded to EPP Server 5.9.3.0. They will notify support when they are ready for the next migration.

## Notes
- Ensure that database partitioning is enabled in future upgrades to handle large event logs effectively.
- Always verify the compatibility of the operating system with the intended EPP version before initiating an upgrade.
- Consider potential downtime and inform customers accordingly during the upgrade process.