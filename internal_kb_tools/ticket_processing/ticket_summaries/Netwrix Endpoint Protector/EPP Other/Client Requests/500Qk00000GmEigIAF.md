# Support Case Summary

## Ticket Metadata
- **Ticket ID:** 500Qk00000GmEigIAF
- **Case Number:** 423273
- **Status:** Closed - Resolved
- **Account/Company:** Catchpoint India
- **Contact Name:** Indu Shekhar
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Client Requests
- **Version:** NONE

## Problem Description
The customer reported receiving logs related to DPI bypassed traffic in the Netwrix Endpoint Protector system. These logs were categorized under "Content Threat Detected" and contained junk data, which the customer found unhelpful for their current setup. They requested assistance in disabling these DPI traffic logs.

## Environment Details
- **Build Number:** 5940
- **Age:** 7.8

## Troubleshooting Steps
1. Reviewed the log settings in the Endpoint Protector portal.
2. Investigated the configuration related to DPI bypassed traffic logging.
3. Suggested potential adjustments to log settings to filter out unwanted logs.
4. Recommended upgrading the agents to the latest version as a potential solution.

## Root Cause
The issue was identified as being related to outdated agents that were not properly handling DPI bypassed traffic logs, resulting in the generation of junk data.

## Solution
The issue was resolved by upgrading the agents to the latest version. This upgrade improved the handling of DPI bypassed traffic logs, eliminating the generation of junk data and ensuring that logs were categorized correctly.

## Notes
- Ensure that agents are kept up to date to avoid similar issues in the future.
- Monitor log settings regularly to ensure they align with the organization's needs and do not capture unnecessary data.