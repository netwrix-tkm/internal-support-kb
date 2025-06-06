## Ticket Metadata
- **Ticket ID:** 500Qk00000GqBCiIAN
- **Case Number:** 423472
- **Status:** Closed - Resolved
- **Account/Company:** Fair Isaac Corporation (FICO)
- **Contact Name:** Prashanth Varma Sammeta
- **Product:** Netwrix Enterprise Auditor
- **Component:** Access Information Center
- **Feature:** Self-Service
- **Version:** 11.6

## Problem Description
The customer reported an urgent issue regarding the inability to locate the StealthAudit site in IIS while attempting to install an SSL certificate.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Collector Code:** Access Information Center
- **Issue Type:** Incorrect configuration: target server software

## Troubleshooting Steps
1. Attempted to locate the StealthAudit site in IIS.
2. Reviewed the current SSL certificate configuration.
3. Engaged with team members for insights on certificate installation requests.
4. Scheduled an impromptu meeting to discuss the issue, which the customer did not attend.

## Root Cause
The issue was identified as an incorrect configuration related to the target server software, which prevented the SSL certificate from being properly updated.

## Solution
The resolution involved changing the SSL certificate for the published reports on port 8082 and for the Access Information Center on port 481. This adjustment allowed the SSL certificate installation to proceed successfully.

## Notes
- Ensure that the server configuration is verified before attempting SSL certificate installations to avoid similar issues in the future.
- It may be beneficial to have a checklist for SSL certificate updates that includes verifying site visibility in IIS and confirming the correct ports are being used.