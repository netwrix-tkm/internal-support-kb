## Ticket Metadata
- **Ticket ID:** 500Qk00000LHfDxIAL
- **Case Number:** 434189
- **Status:** Closed - Resolved
- **Account/Company:** Chapman and Cutler LLP
- **Contact Name:** Veronica Yessa
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Migration
- **Version:** Not specified

## Problem Description
The customer reported that after exporting the database from their on-premises server and importing it into the new SaaS environment, the Endpoint Protector Rights Functionality Priority setting was not updated as expected during the database import.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Migration Type:** From on-premises to SaaS

## Troubleshooting Steps
1. The issue was escalated to engineering for further investigation.
2. Engineering confirmed that the Rights Functionality Priority setting is not stored in the database but in a configuration file located at `/EPPServer/sieratool/apps/ratool/config/epp.yml`.
3. A list of other settings that are maintained outside the database was requested from engineering.

## Root Cause
The Rights Functionality Priority setting is maintained in a configuration file rather than the database, which is why it was not overwritten during the database import process.

## Solution
The issue was resolved by confirming with engineering that the configuration for the Rights Functionality Priority is stored in the configuration file (`epp.yml`) and not in the database. This information clarified that the observed behavior was expected and not a one-off issue.

## Notes
- Future database imports may not overwrite settings stored in configuration files. It is important to verify which settings are stored in the database and which are maintained in configuration files.
- The configuration file contains static data and directory paths, which should be reviewed during migration processes to ensure all necessary settings are correctly configured.