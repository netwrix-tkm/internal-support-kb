## Ticket Metadata
- **Ticket ID:** 500Qk00000HksgLIAR
- **Case Number:** 425768
- **Status:** Closed - Resolved
- **Account/Company:** Halodata International Pte Ltd
- **Contact Name:** Halodata Support Tech
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** NONE

## Problem Description
The customer requested documentation regarding High Availability (HA) configuration for the Netwrix Endpoint Protector (EPP). They expressed concern that currently, only one server receives logs at any given time due to the connection being made via server IP. They needed a solution to ensure logs could be duplicated to both servers to comply with regulatory requirements.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Server
- **Age of the Issue:** 4.1 days

## Troubleshooting Steps
1. Reviewed the customer's request for HA documentation.
2. Clarified the current logging mechanism and its limitations regarding HA.
3. Provided information on potential configurations to achieve log duplication across servers.

## Root Cause
The issue stemmed from a lack of understanding of the EPP's current logging architecture, which only allows one server to receive logs at a time due to the use of a single server IP for connections.

## Solution
The support team provided the necessary documentation and guidance on configuring HA for EPP. This included steps to set up log duplication across multiple servers, ensuring compliance with the customer's regulatory requirements.

## Notes
- It is important for customers to understand the limitations of the current logging setup in EPP.
- Future inquiries regarding HA configurations should reference the provided documentation to expedite the resolution process.
- Ensure that customers are aware of the compliance implications when configuring logging systems.