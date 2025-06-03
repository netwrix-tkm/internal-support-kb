## Ticket Metadata
- **Ticket ID:** 500Qk00000MOMSbIAP
- **Case Number:** 437312
- **Status:** Closed - Resolved
- **Account/Company:** PROOF
- **Contact Name:** Samantha Skinner
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** 5.9.4.1

## Problem Description
The customer reported that their Endpoint Protector EC2 instance had several critical vulnerabilities identified by a security tool. They were unable to SSH into the instance to perform updates, and the web server was not providing any updates to run.

## Environment Details
- **EPP Version:** 5.9.4.1
- **Operating System:** Linux Ubuntu 18.04.6
- **PHP Version:** 5.2.17
- **Hosting:** AWS

## Troubleshooting Steps
1. **Remote Session:** Joined a remote session with the customer to assess the situation.
2. **SSH Access:** Identified that port 62828 needed to be opened to allow SSH access.
3. **Version Confirmation:** Confirmed the EPP version was 5.9.4.1.
4. **Security Scan Review:** Reviewed the security scan results provided by the customer.
5. **PHP Upgrade Inquiry:** Created an ADO to inquire about the status of the PHP upgrade process.
6. **Migration Discussion:** Discussed the possibility of migrating the server to Ubuntu 22.

## Root Cause
The inability to SSH into the EC2 instance was due to the necessary port (62828) being closed. Additionally, the outdated PHP version and the EPP version contributed to the vulnerabilities identified by the security tool.

## Solution
The issue was resolved by:
- Advising the customer to open the necessary SSH port (62828).
- Informing the customer that Netwrix has obtained extended life support for Ubuntu 18, which includes security updates.
- Offering to migrate the instance to Ubuntu 22 if preferred, with detailed steps provided for the migration process.

## Notes
- The customer was informed that the Endpoint Protector development team is actively working on a project to update the PHP version in phases, with the first phase expected to occur within four months.
- It is recommended that customers regularly check for updates and security patches to avoid similar issues in the future.