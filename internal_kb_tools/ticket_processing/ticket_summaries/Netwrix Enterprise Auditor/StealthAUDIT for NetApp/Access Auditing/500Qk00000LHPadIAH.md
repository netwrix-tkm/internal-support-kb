```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000LHPadIAH
- **Case Number:** 434174
- **Status:** Closed - Resolved
- **Account/Company:** USAA
- **Contact Name:** Steven Giles
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for NetApp
- **Feature:** Access Auditing
- **Version:** 11.6

## Problem Description
The FSAA Scan job in StealthAUDIT was terminating unexpectedly during execution. The issue was accompanied by crashes logged in the Event Viewer and the generation of a process dump file in the StealthAUDIT directory.

## Environment Details
- **Product Version:** 11.6
- **Build Number:** 11.6.0.113

## Troubleshooting Steps
1. R&D reproduced the issue in their development environment.
2. Collected event logs and process dumps to analyze the crash.
3. Identified a key error in the Windows Application Event Log indicating a timeout with the named pipe server.
4. Investigated the stack trace related to SafeAccessTokenHandles not being finalized, leading to resource exhaustion.

## Root Cause
The root cause of the issue was identified as a product defect related to the improper handling of SafeAccessTokenHandles. This caused the application to run out of available handles during re-impersonation, leading to the termination of the FSAA Scan job.

## Solution
The issue was resolved by updating the product to the latest cumulative update (CU). The fix addressed the underlying defect in the code that managed resource handles, specifically in the core area of the product.

## Notes
- Customers experiencing similar issues should ensure they are running the latest cumulative update to avoid this defect.
- Monitoring the Event Viewer for related errors can help in diagnosing similar issues in the future.
- It is important to regularly check for updates and apply them to maintain system stability and performance.
```