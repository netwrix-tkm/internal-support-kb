## Ticket Metadata
- **Ticket ID:** 500Qk00000JykwNIAR
- **Case Number:** 430854
- **Status:** Closed - Resolved
- **Account/Company:** Xentris Wireless, LLC
- **Contact Name:** Pranav Patel
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Access Error
- **Version:** Not specified

## Problem Description
The customer reported an issue where they could not access the URL for the Netwrix Endpoint Protector, and upon attempting to log in, they received a message indicating that the disk was full. Additionally, they had lost access to the root password.

## Environment Details
- The issue occurred on a server running Netwrix Endpoint Protector.
- The specific environment details such as OS version or hardware specifications were not provided.

## Troubleshooting Steps
1. Cleared locations on the system disk related to email alerts to free up space.
2. Cleared the database of unsent email alerts that may have contributed to disk space issues.
3. Reset the root UI login password to regain access.
4. Advised the customer to either delete alerts or configure the System Configuration -> System Settings -> Email SMTP settings, as the lack of configuration was identified as a contributing factor to the issue.
5. Reset the uninstall password for agents to ensure proper access.

## Root Cause
The root cause of the issue was identified as a full disk due to unsent email alerts accumulating on the system. Additionally, the absence of configured SMTP settings for email alerts exacerbated the situation, leading to the disk space issue.

## Solution
The issue was resolved by performing the following actions:
- Clearing unnecessary files related to email alerts to free up disk space.
- Resetting the root UI login password to restore access.
- Advising the customer to configure the SMTP settings to prevent future accumulation of unsent email alerts, or to delete existing alerts to manage disk space effectively.
- Resetting the uninstall password for agents to ensure continued access.

## Notes
- It is important to regularly monitor disk space and configure email alert settings to avoid similar issues in the future.
- Customers should be advised to periodically check for unsent email alerts and clear them if necessary to maintain optimal system performance.