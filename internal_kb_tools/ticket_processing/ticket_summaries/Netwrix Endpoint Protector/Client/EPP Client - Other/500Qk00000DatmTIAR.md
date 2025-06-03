```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000DatmTIAR
- **Case Number:** 416239
- **Status:** Closed - Resolved
- **Account/Company:** Booking.com
- **Contact Name:** Serhat Demir
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** EPP Client - Other
- **Version:** 5.9.4.1

## Problem Description
The customer reported receiving pop-ups indicating a connection drop due to a certificate hostname mismatch. The errors were logged in the `eppclient.log`, and the customer was unsure if the issue was related to DPI Bypass.

## Environment Details
- The issue was observed while accessing specific URLs, including `https://play.google.com` and `https://bam.eu01.nr-data.net`.

## Troubleshooting Steps
1. The customer reviewed the `eppclient.log` for error details.
2. Support investigated the logs but found that the event for `https://bam.eu01.nr-data.net` did not occur during the log collection.
3. Support advised the customer to collect a new set of logs if the issue reoccurred.

## Root Cause
The connection drop was caused by a DPI (Deep Packet Inspection) bypass issue, which resulted in a certificate hostname mismatch. The specific event related to the hostname mismatch was not captured in the logs at the time of the incident.

## Solution
The issue was resolved in version 5.9.4.1 of the Netwrix Endpoint Protector. The customer was informed that the fix was included in this release, and the ticket was subsequently closed.

## Notes
- Customers experiencing similar issues should ensure they are using the latest version of the software.
- If the issue recurs, it is recommended to collect a new set of logs for further analysis.
- The DPI bypass events should be logged in the EPP server and can be found in the Content Aware Reports.
```