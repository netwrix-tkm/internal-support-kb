## Ticket Metadata
- **Ticket ID:** 500Qk00000CWHgOIAX
- **Case Number:** 413598
- **Status:** Closed - Resolved
- **Account/Company:** CEA
- **Contact Name:** Julien Langot
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Upgrade
- **Version:** 5.2.0.7 (Server), 5.1.2 (Client)

## Problem Description
The customer, Julien Langot, requested guidance on upgrading their EPP Server/Client system, which was running on an outdated version (Server: 5.2.0.7, Client: 5.1.2). They were operating in an offline, on-premise environment and needed to know the best upgrade path.

## Environment Details
- **Current Server Version:** 5.2.0.7
- **Current Client Version:** 5.1.2
- **Operating System:** Likely Ubuntu 14 (based on the age of the appliance)

## Troubleshooting Steps
1. Acknowledged the customer's request and initiated internal investigation.
2. Confirmed the age of the appliance and its operating system version.
3. Determined that upgrading from such an old version would require applying over 20 patches, which could not be supervised due to the air-gapped nature of the appliance.
4. Assessed compatibility issues with the required patch version (5.6.5.0) that necessitated at least Ubuntu 18.
5. Recommended a fresh installation of the EPP server and a new set of EPP clients.

## Root Cause
The primary issue was the outdated version of the EPP server and its underlying operating system (Ubuntu 14), which made it impossible to perform a straightforward upgrade. The significant number of required patches and the air-gapped environment further complicated the upgrade process.

## Solution
The resolution involved recommending a fresh installation of the EPP server. This approach would ensure that the system was up-to-date and compatible with the latest software requirements. The customer was informed that the existing configuration could not be exported to the new server due to version differences.

## Notes
- **Important Consideration:** Future upgrades should be planned with regular updates to avoid falling behind on software versions, which can complicate upgrade paths.
- **Configuration Export Limitation:** Due to differences in server versions, exporting configurations from the old server to the new one is not feasible. Customers should prepare for manual configuration on the new installation.