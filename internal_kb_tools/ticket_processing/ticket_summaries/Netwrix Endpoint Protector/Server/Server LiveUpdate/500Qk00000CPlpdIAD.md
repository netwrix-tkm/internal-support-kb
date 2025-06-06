## Ticket Metadata
- **Ticket ID:** 500Qk00000CPlpdIAD
- **Case Number:** 413366
- **Status:** Closed - Resolved
- **Account/Company:** Barmherzige Brüder IT Services
- **Contact Name:** Patrick Gross
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server LiveUpdate
- **Version:** 6.2.2.1

## Problem Description
The customer, Patrick Gross, reported issues after applying the server-side patch (EPP Server Hotfix #1) as per Security Advisory ADV-2024-002. Although the patch was confirmed as successfully applied, it continued to show as available for installation. Additionally, the customer inquired about the availability of a newer client version, as the advisory indicated that both the server and client must be updated to fully resolve vulnerabilities.

## Environment Details
- **Client Version:** 6.2.2.1 deployed across endpoints.

## Troubleshooting Steps
1. The customer applied the EPP Server Hotfix #1 and confirmed the patch was applied successfully.
2. The customer refreshed the browser page and cleared the browser cache to check if the update status changed.
3. The customer reported that the patch still appeared as available despite being installed.
4. The customer noted that the patch was accidentally installed twice.

## Root Cause
The issue was identified as a display error in the EPP software update interface, where the system did not refresh correctly to reflect the applied patch status.

## Solution
The technical support engineer, Andrei Pop, advised the customer to refresh the browser page after applying the patch. Additionally, he confirmed that a newer client version was available, specifically version 6.2.2.2005, which the customer could download from the provided link.

## Notes
- It is important for users to refresh their browser after applying updates to ensure the interface reflects the current status.
- Always verify the version compatibility between the Endpoint Protector server and client to ensure all vulnerabilities are addressed as per security advisories.