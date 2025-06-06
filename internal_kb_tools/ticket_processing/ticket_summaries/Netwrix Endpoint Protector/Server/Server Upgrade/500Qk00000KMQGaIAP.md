## Ticket Metadata
- **Ticket ID:** 500Qk00000KMQGaIAP
- **Case Number:** 431474
- **Status:** Closed - Resolved
- **Account/Company:** Publica Group Ltd.
- **Contact Name:** Tom Rose
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Upgrade
- **Version:** 5.9.4.0 to 5.9.4.1

## Problem Description
The customer reported an upgrade failure while attempting to upgrade the virtual appliance of Endpoint Protector from version 5.9.4.0 to 5.9.4.1. An error message appeared during the upgrade process indicating that "some problems occurred during installation. Please contact support. (Error 2 - Number of maximum retries for this update reached, skipping this update)."

## Environment Details
- **Virtual Appliance:** Netwrix Endpoint Protector
- **Current Version:** 5.9.4.0
- **Target Version:** 5.9.4.1

## Troubleshooting Steps
1. The customer initiated the upgrade process from version 5.9.4.0 to 5.9.4.1.
2. Upon encountering the error message, the customer attempted to resolve the issue by checking for any prerequisites or known issues related to the upgrade.
3. The customer reverted to a previous snapshot of the virtual appliance to clear the error.

## Root Cause
The root cause of the upgrade failure was identified as exceeding the maximum number of retries allowed for the update process, which resulted in the installation being skipped.

## Solution
The issue was resolved by the customer reverting to a previous snapshot of the virtual appliance, which allowed them to restore the system to a stable state prior to the failed upgrade attempt.

## Notes
- It is recommended to ensure that all prerequisites for the upgrade are met before initiating the process to avoid similar issues in the future.
- Customers should consider taking a snapshot of the virtual appliance before performing upgrades to facilitate easy recovery in case of failure.
- Monitoring logs during the upgrade process may provide additional insights into potential issues that could arise.