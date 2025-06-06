## Ticket Metadata
- **Ticket ID:** 500Qk00000HiYLyIAN
- **Case Number:** 425661
- **Status:** Closed - Resolved
- **Account/Company:** Pension Boards United Church of Christ
- **Contact Name:** Johnnie Lopez
- **Product:** Netwrix Enterprise Auditor
- **Component:** Access Information Center
- **Feature:** Configuration
- **Version:** 11.6

## Problem Description
The customer reported that after upgrading to the latest version of Netwrix Enterprise Auditor (NEA), the Access Information Center (AIC) was no longer functioning and returned a 500 error when accessed.

## Environment Details
- **Previous AIC Version:** 11.5
- **Current NEA Version:** 11.6
- **AIC Access URL:** http://localhost:81/v2/login

## Troubleshooting Steps
1. Confirmed that the AIC was not upgraded alongside the NEA.
2. Verified the version of AIC currently in use (11.5).
3. Attempted to access the AIC interface, which resulted in an HTTP error 503 (Service Unavailable).
4. Provided the customer with instructions on how to upgrade AIC to version 11.6.

## Root Cause
The issue was caused by the AIC not being upgraded in conjunction with the NEA. The two components require compatible versions to function correctly.

## Solution
The issue was resolved by upgrading the AIC to version 11.6, which restored its functionality and compatibility with the upgraded NEA.

## Notes
- It is crucial to ensure that both NEA and AIC are kept at compatible versions during upgrades to avoid service interruptions.
- Future upgrades should include a checklist to verify that all dependent components are also updated accordingly.