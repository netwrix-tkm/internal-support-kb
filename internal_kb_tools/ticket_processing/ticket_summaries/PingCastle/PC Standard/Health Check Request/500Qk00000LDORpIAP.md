## Ticket Metadata
- **Ticket ID:** 500Qk00000LDORpIAP
- **Case Number:** 433971
- **Status:** Closed - Resolved
- **Account/Company:** Nebulan
- **Contact Name:** Federico Gallo
- **Product:** PingCastle
- **Component:** Health Check Request
- **Feature:** Health Check Report
- **Version:** 3.3

## Problem Description
The customer generated a health check report and encountered a legend stating: 
"RESTRICTEDTOUSER - The permission described above is restricted to Users." They were unable to find any details regarding this legend in the Access Control List (ACL) for the object, and the corresponding privilege was not visible in the ACL.

## Environment Details
- **Platform:** PingCastle
- **Collector Code:** PC Standard
- **Product Version:** 3.3

## Troubleshooting Steps
1. Reviewed the health check report for the legend "RESTRICTEDTOUSER."
2. Investigated the ACL for the object in question to locate the corresponding privilege.
3. Confirmed that the privilege marked as "RESTRICTEDTOUSER" was not visible in the ACL.
4. Gathered information on the implications of the "RESTRICTEDTOUSER" designation.

## Root Cause
The root cause of the issue was identified as the nature of the "RESTRICTEDTOUSER" designation, which indicates that the permissions apply only when a user interacts with the object. This means that the privilege may not be explicitly listed in the ACL but is still applicable under certain user interactions.

## Solution
The issue was resolved by clarifying that the "RESTRICTEDTOUSER" legend signifies that the permissions are context-dependent and may not appear in the ACL unless a user is actively interacting with the object. No changes were required to the ACL itself, as the permissions are inherently designed to be user-specific.

## Notes
- It is important for users to understand that "RESTRICTEDTOUSER" permissions may not always be visible in the ACL, and this is by design.
- Future inquiries regarding similar legends should focus on user interaction contexts rather than solely on the ACL visibility.