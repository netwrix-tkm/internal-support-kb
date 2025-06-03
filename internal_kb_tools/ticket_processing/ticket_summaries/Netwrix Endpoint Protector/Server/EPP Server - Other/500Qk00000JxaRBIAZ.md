## Ticket Metadata
- **Ticket ID:** 500Qk00000JxaRBIAZ
- **Case Number:** 430828
- **Status:** Closed - Resolved
- **Account/Company:** Laykon Distributor
- **Contact Name:** Yağız Özkütük
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** NONE

## Problem Description
The customer reported that after installing VirtualBox and importing an .ovf file on their client’s machine, they were unable to access the web panel despite being able to ping the machine.

## Environment Details
- VirtualBox installed on the client’s machine.
- IP settings configured correctly.

## Troubleshooting Steps
1. Verified that the .ovf file was successfully imported into VirtualBox.
2. Checked the IP settings and confirmed that the machine was reachable via ping.
3. Investigated the status of the Nginx service, which was found to be not running.

## Root Cause
The Nginx service was not running due to a dhparam error, which prevented access to the web panel.

## Solution
The issue was resolved by running the dhparam command, which corrected the error and allowed the Nginx service to start successfully. After this, access to the web panel was restored.

## Notes
- Ensure that the Nginx service is running properly after installation and configuration to avoid similar access issues in the future.
- Monitor for any dhparam-related errors during the setup of web services to preemptively address potential service interruptions.