## Ticket Metadata
- **Ticket ID:** 500Qk00000IFNtDIAX
- **Case Number:** 426878
- **Status:** Closed - Resolved
- **Account/Company:** Halodata International Pte Ltd
- **Contact Name:** Halodata Support Tech
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** 20.1

## Problem Description
The customer, Halodata International Pte Ltd, reached out with queries regarding the Netwrix Endpoint Protector (EPP) server, specifically about log retention and file types used for SIEM integration.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Server

## Troubleshooting Steps
1. Responded to the customer’s initial queries regarding log retention and SIEM file types.
2. Provided information on log size retention calculations and the types of files sent to the SIEM application.
3. Addressed a follow-up question regarding support for RHEL 8.3 and provided the necessary client download link.

## Root Cause
The queries were based on a lack of documentation regarding log retention timeframes and file types for SIEM integration in the user guide.

## Solution
- For log retention, it was explained that the retention is calculated based on the size of the logs rather than time. The customer was informed that the size of logs can vary, and thus, it is difficult to estimate how long it would take for older logs to be overwritten.
- The customer was informed that only syslog files are sent to the SIEM application.
- Provided a download link for the RHEL 8.3 client and recommended upgrading to the latest client version due to the age of the OS and client.

## Notes
- It is important to clarify that log retention is based on size (MB) rather than time, as this can vary significantly based on user activity.
- Future inquiries regarding specific OS support should include recommendations for upgrading to ensure compatibility with the latest features and security updates.