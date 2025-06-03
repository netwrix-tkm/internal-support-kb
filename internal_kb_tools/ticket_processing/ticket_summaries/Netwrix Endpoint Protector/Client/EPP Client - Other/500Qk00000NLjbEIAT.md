## Ticket Metadata
- **Ticket ID:** 500Qk00000NLjbEIAT
- **Case Number:** 440041
- **Status:** Closed - Resolved
- **Account/Company:** Slice Fintech
- **Contact Name:** Santosh Kaddu
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Client - Other
- **Feature:** Deep Inspection Packet (DIP)
- **Version:** Latest version mentioned in ticket

## Problem Description
The customer reported that enabling the Deep Inspection Packet (DIP) feature resulted in upload issues for end users, preventing them from uploading files.

## Environment Details
- The customer is using Netskope as a security solution alongside Netwrix Endpoint Protector.
- Other security solutions mentioned include SentinelOne and GlobalProtect.

## Troubleshooting Steps
1. Requested additional details from the customer regarding the issue's impact and reproduction steps.
2. Identified that enabling DIP caused upload issues for all end users.
3. Attempted to update both the server and client software.
4. Discovered that disabling Netskope allowed EPP to function correctly.
5. Attempted to whitelist EPP in Netskope but could not determine how to do so.
6. Advised the customer to contact Netskope for assistance with compatibility issues.

## Root Cause
The issue was caused by an incompatibility between Netwrix Endpoint Protector (EPP) and the Netskope security solution, specifically related to the replacement of certificates required for DIP to function properly.

## Solution
The issue was resolved by disabling the Netskope security solution, which allowed the EPP to operate as intended. The customer was advised to reach out to Netskope for further assistance in configuring their settings to allow EPP to work with DIP enabled.

## Notes
- It is important to consider potential conflicts with other security solutions when troubleshooting similar issues.
- Future users experiencing similar upload issues with DIP enabled should check for compatibility with other installed security software and consider disabling or reconfiguring those solutions as necessary.