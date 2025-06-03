## Ticket Metadata
- **Ticket ID:** 500Qk00000OwpHOIAZ
- **Case Number:** 444585
- **Status:** Closed - Resolved
- **Account/Company:** Technology & IT Data Analyst
- **Contact Name:** Philip Wang
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Device Recognition
- **Version:** 6.2.4.2

## Problem Description
The customer reported issues with several endpoints not being detected or listed under the Computers section in Endpoint Protector. Despite attempts to reinstall the client on these machines, they remained undetected.

## Environment Details
- Time zone of the customer: PT (Pacific Time)
- Main support contact: Iosif Muntean

## Troubleshooting Steps
1. Customer attempted to reinstall the Endpoint Protector client on several affected machines.
2. A remote session was requested to further investigate the issue.
3. A clean install of the latest Endpoint Protector client version (6.2.4.2) was performed.

## Root Cause
The issue was likely caused by an outdated or corrupted installation of the Endpoint Protector client on the affected endpoints, which prevented them from communicating with the EPP server.

## Solution
The problem was resolved by performing a clean installation of the latest Endpoint Protector client version (6.2.4.2) on the affected endpoints. This allowed the endpoints to properly connect and be recognized by the EPP server.

## Notes
- It is recommended to ensure that all endpoints are running the latest version of the Endpoint Protector client to avoid similar detection issues in the future.
- Follow-up with the customer is advised to confirm that all computers are now communicating effectively with the EPP server.