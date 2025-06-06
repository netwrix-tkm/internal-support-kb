## Ticket Metadata
- **Ticket ID:** 500Qk00000EQtqUIAT
- **Case Number:** 418123
- **Status:** Closed - Resolved
- **Account/Company:** Albany International
- **Contact Name:** Justin Packard
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Performance

## Problem Description
The customer reported that while using the web interface of the EPP server, the system would intermittently freeze, resulting in a message indicating that the page was not responding. The customer noted that the system appeared to be in good health prior to the lock-ups.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Server

## Troubleshooting Steps
1. Verified the health of the system through the web interface.
2. Attempted to access the cap policy page, which did not load entirely, leading to a browser timeout.
3. Optimized server settings based on current resource allocation.
4. Enabled widget view for policies and removed all computers/users assigned as entities, retaining only department-level access for all policies.

## Root Cause
The issue was primarily due to insufficient server resources, which caused the web interface to hang and time out during operations.

## Solution
The problem was resolved during the first remote session by:
- Optimizing the server configuration to better utilize existing resources.
- Adjusting policy settings to reduce the load on the web interface by enabling widget view and limiting access to department-level entities only.
- The customer was advised to consider increasing server resources to prevent similar issues in the future.

## Notes
- It is recommended that the customer increase server resources to enhance performance and prevent future occurrences of similar issues.
- Continuous monitoring of server performance is advised to ensure optimal operation of the Netwrix Endpoint Protector.