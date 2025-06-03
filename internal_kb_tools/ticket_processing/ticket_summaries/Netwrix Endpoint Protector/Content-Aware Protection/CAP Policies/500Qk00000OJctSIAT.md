## Ticket Metadata
- **Ticket ID:** 500Qk00000OJctSIAT
- **Case Number:** 442743
- **Status:** Closed - Resolved
- **Account/Company:** PrivatBank
- **Contact Name:** CoreWin Tech
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** CAP Policies
- **Version:** None

## Problem Description
PrivatBank reported an issue where a user experienced sound and microphone failures during Google Meet screen sharing. Specifically, the sound would drop, and the user could not be heard by colleagues while sharing their screen. The audio returned once screen sharing was stopped. Disabling or uninstalling the DLP Endpoint Protector client resolved the issue.

## Environment Details
- The issue was observed with the Endpoint Protector client version 3.0.4.1 and a test build version 3.0.4.0023.
- The customer was advised to collect logs from the latest official version 3.0.4.1006.

## Troubleshooting Steps
1. Collected logs from the affected user, which initially contained empty log files ("eppclient.log" and "eppsslsplit.log").
2. Suggested scheduling a remote session to observe the issue live and collect video evidence.
3. Requested the customer to test with the latest official version of the Endpoint Protector client.
4. Followed up with the customer regarding the remote session and log collection.

## Root Cause
The issue was identified as a product defect related to the DLP Endpoint Protector client interfering with audio functionality during Google Meet screen sharing.

## Solution
The ticket was temporarily closed as the customer decided to wait for a resolution from Google regarding the main issue. They were advised to monitor the situation and follow up if the issue reoccurred after any updates or changes.

## Notes
- It is important to ensure that logs are collected from the latest official version of the software to facilitate accurate troubleshooting.
- Future cases should consider the possibility of conflicts between DLP solutions and video conferencing tools, particularly during screen sharing activities.