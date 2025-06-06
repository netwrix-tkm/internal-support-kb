## Ticket Metadata
- **Ticket ID:** 500Qk00000CfAirIAF
- **Case Number:** 414040
- **Status:** Closed - Resolved
- **Account/Company:** Laykon Distributor
- **Contact Name:** Faruk Sarı
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Disk Space
- **Version:** NONE

## Problem Description
The customer reported that despite having a 500 GB disk allocation on Google Cloud Platform (GCP), the system only recognized 91 GB of disk space (50 GB for the system and 41 GB for the EPP server). They sought clarification on why the disk space appeared as 91 GB and requested assistance in fixing or increasing it.

## Environment Details
- **Platform:** Google Cloud Platform (GCP)
- **Product in Use:** Netwrix Endpoint Protector

## Troubleshooting Steps
1. Initial assessment of the disk allocation settings on the GCP instance.
2. Communication with the customer to schedule a remote session for further investigation.
3. Planned a remote connection to adjust the server settings to utilize the full disk space.

## Root Cause
The issue was identified as a configuration problem where the server was not set to utilize the entire allocated disk space, leading to the discrepancy in reported disk size.

## Solution
The issue was resolved by increasing the server size during a remote session. This adjustment allowed the server to recognize and utilize the full 500 GB disk allocation as intended.

## Notes
- Ensure that server configurations are verified after any disk allocation changes to prevent similar issues in the future.
- It is advisable to document any changes made during remote sessions for future reference and troubleshooting.