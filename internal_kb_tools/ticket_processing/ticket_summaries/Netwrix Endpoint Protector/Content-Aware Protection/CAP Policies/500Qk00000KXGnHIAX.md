## Ticket Metadata
- **Ticket ID:** 500Qk00000KXGnHIAX
- **Case Number:** 431821
- **Status:** Closed - Resolved
- **Account/Company:** Bright Life Care Limited
- **Contact Name:** Bhavishya Arya
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** CAP Policies
- **Version:** Not specified

## Problem Description
The customer reported that enabling "Cloudflare Services" on macOS caused the EPP (Endpoint Protector) policies to stop functioning. This issue appeared to stem from a conflict between Cloudflare Services and the EPP install certificates in the browser.

## Environment Details
- Operating Systems tested: macOS and UbuntuOS
- CAP policies configured with:
  - Block & report actions
  - Exit points selected for browsers
  - Denylist including file types such as Excel, PowerPoint, and PDF

## Troubleshooting Steps
1. Verified that CAP policies functioned correctly when Cloudflare Services were disabled.
2. Collected logs from both macOS and UbuntuOS, including extended DPI logs.
3. Reviewed the configuration of the DPI and Cloudflare solution.
4. Followed up with the customer to check if the network extension was approved on macOS.
5. Investigated the networking configuration that could affect the ability to scan uploaded items.

## Root Cause
The root cause of the issue was not definitively identified. However, it was established that the CAP policies worked as expected when Cloudflare Services were disabled, indicating a conflict between the two services.

## Solution
The issue was resolved by confirming that the customer could disable Cloudflare Services when using EPP policies. The customer indicated that they were satisfied with this workaround and requested to close the ticket.

## Notes
- It is important to note that enabling Cloudflare Services may interfere with the functionality of EPP policies on macOS and UbuntuOS.
- Future users experiencing similar issues should consider disabling Cloudflare Services as a potential workaround.
- Ensure that network extensions are approved on macOS to avoid similar conflicts.