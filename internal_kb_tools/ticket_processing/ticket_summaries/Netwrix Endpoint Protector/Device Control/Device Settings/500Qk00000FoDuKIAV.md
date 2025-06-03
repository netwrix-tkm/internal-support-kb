## Ticket Metadata
- **Ticket ID:** 500Qk00000FoDuKIAV
- **Case Number:** 421098
- **Status:** Closed - Resolved
- **Account/Company:** Liverpool University Hospitals NHS Foundation Trust
- **Contact Name:** Ray Soong
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device Settings
- **Version:** NONE

## Problem Description
The customer reported that the log reports were only showing "Policies Received" events, which prevented them from seeing other critical events such as blocked actions or devices in "read-only" mode.

## Environment Details
- The issue was related to the Netwrix Endpoint Protector platform, specifically within the Device Control component.

## Troubleshooting Steps
1. Reviewed the log reports to confirm the absence of expected events.
2. Noted that the log table did not resemble the expected fields.
3. Suggested the customer enable Reporting V2 to enhance log reporting capabilities.
4. Optimized the server configuration to support 1500 Domain Controllers (DC).

## Root Cause
The root cause of the issue was identified as a misconfiguration in the logging setup, which resulted in incomplete log entries being recorded.

## Solution
The issue was resolved by optimizing the server settings to accommodate a larger number of Domain Controllers, which allowed the logs to be processed correctly. After this adjustment, the logs began to populate with the expected events, including those indicating blocked actions and device statuses.

## Notes
- It is recommended to monitor log configurations regularly to ensure they align with expected reporting standards.
- Enabling Reporting V2 can significantly improve the visibility of log events and should be considered in similar cases.