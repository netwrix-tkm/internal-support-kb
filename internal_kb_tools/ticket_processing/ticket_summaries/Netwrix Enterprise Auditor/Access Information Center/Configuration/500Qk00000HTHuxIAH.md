## Ticket Metadata
- **Ticket ID:** 500Qk00000HTHuxIAH
- **Case Number:** 425074
- **Status:** Closed - Resolved
- **Account/Company:** Kerry Group Services International Limited
- **Contact Name:** Lorcan O'Sullivan
- **Product:** Netwrix Enterprise Auditor
- **Component:** Access Information Center
- **Feature:** Configuration
- **Version:** 11.6

## Problem Description
The customer reported an issue where they were unable to add non-ICT domain owners in the 'resource owners' section of the Netwrix Access Information Center. Previously, multiple domains were visible for selection, but now only the ICT domain was available.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Collector Code:** Access Information Center

## Troubleshooting Steps
1. Confirmed that the Active Directory (AD) account used for running scans was re-enabled.
2. Advised the customer to ensure the Host List included all necessary domains.
3. Suggested running the ".Active Directory Inventory" group scan manually.
4. Identified that domains were missing in the "AuthSearchDomain" field in the "AccessInformationCenter.Service.exe.config" file.
5. Provided instructions to add non-ICT domains to the "AuthSearchDomain" field.
6. Instructed the customer to restart the "Netwrix Access Information Center" service after making changes to the config file.

## Root Cause
The issue was caused by missing non-ICT domains in the "AuthSearchDomain" field of the "AccessInformationCenter.Service.exe.config" file, which restricted the selection of resource owners to only the ICT domain.

## Solution
The resolution involved:
- Adding the required non-ICT domains to the "AuthSearchDomain" field in the "AccessInformationCenter.Service.exe.config" file.
- Restarting the "Netwrix Access Information Center" service to apply the changes.

The customer confirmed that after these steps, they were able to see and select the additional domains when adding resource owners.

## Notes
- Ensure that the configuration file is saved with the correct permissions to prevent loss of changes after a service restart.
- Always restart the service after making changes to the configuration file to ensure that the changes take effect.
- Monitor for any potential issues with the AD scan that could affect domain visibility in the future.