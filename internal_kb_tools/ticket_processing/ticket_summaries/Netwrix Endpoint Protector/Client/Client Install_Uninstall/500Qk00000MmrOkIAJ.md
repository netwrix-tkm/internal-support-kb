## Ticket Metadata
- **Ticket ID:** 500Qk00000MmrOkIAJ
- **Case Number:** 438342
- **Status:** Closed - Resolved
- **Account/Company:** Samsung - SRI Bangalore
- **Contact Name:** Mohammed Shafi
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Install/Uninstall
- **Version:** Ubuntu 18.04

## Problem Description
The customer reported an issue with installing the Netwrix Endpoint Protector offline agent on an Ubuntu 18.04 machine. The installation failed due to unmet dependencies.

## Environment Details
- Operating System: Ubuntu 18.04
- Installation Method: Offline repository

## Troubleshooting Steps
1. The customer attempted to install the Epp client from an offline repository.
2. The installation process generated errors related to unmet dependencies, including:
   - `libboost-chrono1.65.1`
   - `libevent-openssl-2.1-6`
   - `libevent-pthreads-2.1-6`
   - `libzip4`
   - `cifs-utils`
3. The customer was advised to check if the offline repository included the necessary dependencies.
4. The customer attempted to manually install/update the dependencies but continued to face issues.
5. A remote session was scheduled to assist with the installation process.

## Root Cause
The root cause of the installation failure was identified as missing dependencies that were not included in the offline repository. Additionally, the existing system libraries were incompatible with the required versions for the Epp client.

## Solution
The issue was resolved by advising the customer to upgrade the operating system version. This upgrade was necessary to ensure compatibility with the required dependencies for the Epp client installation. The customer was informed to plan for a backup machine to run the service in parallel during the upgrade process.

## Notes
- The customer was advised not to close the ticket for a period of three weeks due to the ongoing upgrade process.
- Future installations should ensure that all required dependencies are included in the offline repository or consider providing temporary internet access for the installation process.