## Ticket Metadata
- **Ticket ID:** 500Qk00000LUTlFIAX
- **Case Number:** 434676
- **Status:** Closed - Resolved
- **Account/Company:** Stadtverwaltung Radolfzell
- **Contact Name:** Udo Friese
- **Product:** Netwrix Endpoint Protector
- **Component:** EasyLock / Enforced Encryption
- **Feature:** EasyLock - Other
- **Version:** NONE

## Problem Description
The customer reported an error message stating: "Die Version die Sie verteilen möchten konnte abgelaufen oder manipuliert sein. Bitte laden Sie EasyLock nochmal herunter." This translates to "The version you are trying to distribute may have expired or been tampered with. Please download EasyLock again." The error caused the application to close upon clicking "OK."

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Age of the Issue:** 21.1

## Troubleshooting Steps
1. The customer was advised to check for the presence of the EasyLock file.
2. It was suggested to replace the metadata folder associated with EasyLock.
3. The customer was instructed to attempt the steps and report back.

## Root Cause
The issue was identified as potentially being caused by a missing EasyLock file, which led to the error message indicating that the version was either expired or tampered with.

## Solution
The problem was resolved by replacing the metadata folder associated with EasyLock. This action restored the necessary files and allowed the application to function correctly without displaying the error message.

## Notes
- Ensure that the EasyLock file is present and not corrupted before distribution to avoid similar issues in the future.
- Regularly check for updates or changes in the metadata folder to maintain application integrity.