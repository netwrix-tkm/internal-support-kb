## Ticket Metadata
- **Ticket ID:** 500Qk00000KLpiNIAT
- **Case Number:** 431427
- **Status:** Closed - Resolved
- **Account/Company:** DEPARTEMENT DU VAL D'OISE
- **Contact Name:** Sébastien LEGEAY
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Upgrade
- **Version:** 5.9.4.1

## Problem Description
The customer encountered an error during the upgrade process to version 5.9.4.1 of Netwrix Endpoint Protector. The error message indicated that some problems occurred during installation, specifically stating: "ERROR: 2 - Number of maximum retries for this update reached, skipping this update..."

## Environment Details
- **Current Version Prior to Upgrade:** 5.3
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Server

## Troubleshooting Steps
1. Verified the error message received during the upgrade attempt.
2. Checked the system logs for any additional error details related to the installation process.
3. Confirmed that the system met the necessary requirements for the upgrade to version 5.9.4.1.
4. Attempted to rerun the upgrade process multiple times, observing the same error message each time.

## Root Cause
The root cause of the issue was identified as the maximum number of retries for the update being reached without a successful installation. This typically indicates a failure in the upgrade process due to either system compatibility issues or insufficient resources.

## Solution
The issue was resolved by ensuring that the system met all prerequisites for the upgrade and then successfully executing the upgrade process after addressing any underlying compatibility issues. The customer confirmed that the upgrade was completed successfully, allowing the case to be closed.

## Notes
- Ensure that all system requirements are thoroughly checked before attempting an upgrade to prevent similar issues.
- It may be beneficial to monitor system resources during the upgrade process to identify any potential bottlenecks that could lead to installation failures.
- Document any specific compatibility issues encountered during the upgrade for future reference.