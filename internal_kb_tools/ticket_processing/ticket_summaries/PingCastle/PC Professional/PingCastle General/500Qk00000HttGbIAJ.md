## Ticket Metadata
- **Ticket ID:** 500Qk00000HttGbIAJ
- **Case Number:** 426028
- **Status:** Closed - Resolved
- **Account/Company:** DLA Piper
- **Contact Name:** Chris Uys
- **Product:** PingCastle
- **Component:** PC Professional
- **Feature:** PingCastle General
- **Version:** 3.2.0.1

## Problem Description
The customer reported that .NET 6 is reaching its end of life on November 12, 2024, and expressed concern that PingCastle Pro relies on it. They inquired about the availability of an updated version that supports .NET 8 or if there was a way to make version 3.2.0.1 work with .NET 8.

## Environment Details
- **Current .NET Version:** .NET 6
- **PingCastle Version:** 3.2.0.1
- **Upcoming .NET Version:** .NET 8

## Troubleshooting Steps
1. Confirmed the end of support for .NET 6 and its implications for PingCastle.
2. Informed the customer that PingCastle is compatible with later versions of .NET.
3. Investigated the possibility of running PingCastle with .NET 8.
4. Communicated with the development team regarding the compatibility of PingCastle with .NET 8.
5. Advised the customer to downgrade to the ASP.NET 6 hosting bundle as a temporary solution.

## Root Cause
The root cause of the issue was identified as the lack of support for .NET 8 in the current version of PingCastle (3.2.0.1). The application has hardcoded references to .NET 6, which prevents it from functioning correctly with newer versions.

## Solution
The issue was resolved by advising the customer to downgrade to the ASP.NET 6 hosting bundle, as higher versions of .NET are not supported at this time. The development team is aware of the need for .NET 8 compatibility and is actively working on it, but no estimated time of arrival (ETA) was provided.

## Notes
- The customer expressed urgency due to security compliance audits, indicating that they may need to temporarily remove PingCastle from their environment until .NET 8 support is available.
- It is important to keep customers informed about the progress of compatibility updates for future versions of .NET.