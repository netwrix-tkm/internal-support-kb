## Ticket Metadata
- **Ticket ID:** 500Qk00000KJErnIAH
- **Case Number:** 431316
- **Status:** Closed - Resolved
- **Account/Company:** Barthelmeß EDV-Service GmbH
- **Contact Name:** Alexander Support
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Other
- **Version:** 5.9.4.0 to 5.9.4.1

## Problem Description
The customer encountered an error while attempting to apply an update from version 5.9.4.0 to 5.9.4.1. The error message indicated that there were issues during installation, specifically stating that the update script checksum did not match the checksum received from the Live Update Server.

## Environment Details
- The issue was reproduced in the customer's environment.
- The error was present in the Live Update feature of the Netwrix Endpoint Protector.

## Troubleshooting Steps
1. Verified the error message during the update process.
2. Attempted to reproduce the issue in the customer's environment.
3. Identified that the checksum mismatch was causing the update failure.
4. Communicated with the customer to gather more information about the error.

## Root Cause
The root cause of the issue was not definitively identified. However, it was determined that the checksum mismatch between the update script and the Live Update Server was the primary symptom leading to the installation failure.

## Solution
The issue was resolved by removing the error present in the Live Update. Specific steps taken to remove the error were not detailed, but it involved direct communication with the customer to ensure the update could proceed without further issues.

## Notes
- It is important to monitor checksum values during updates to prevent similar issues in the future.
- Ensure that the Live Update Server is functioning correctly and that the update scripts are not corrupted before attempting to apply updates.
- Future cases involving checksum mismatches should consider checking the integrity of the update files and the connection to the Live Update Server.