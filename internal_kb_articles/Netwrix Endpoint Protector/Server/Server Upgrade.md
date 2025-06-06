# Netwrix Endpoint Protector Knowledge Base: Server Upgrade Guide

## Overview

Server upgrades are a critical aspect of maintaining the Netwrix Endpoint Protector (EPP) environment. They ensure compatibility with the latest features, address security vulnerabilities, and improve system performance. This guide provides a comprehensive reference for diagnosing, troubleshooting, and resolving server upgrade issues. It is designed to equip support engineers with systematic methodologies, proven techniques, and real-world insights to handle these cases effectively and consistently.

---

## Technical Background

### Key Concepts
- **Netwrix Endpoint Protector (EPP):** A Data Loss Prevention (DLP) solution designed to secure sensitive data across endpoints.
- **Server Upgrade:** The process of updating the EPP server software or its underlying operating system to a newer version to address vulnerabilities, introduce new features, or improve performance.
- **Live Update:** A feature that allows servers to download and apply updates directly from Netwrix servers.
- **Offline Patch:** A downloadable update package used in environments with restricted internet access or when live updates fail.
- **Hotfix:** A targeted update addressing specific issues or vulnerabilities.
- **Database Partitioning:** A method to optimize database performance by dividing large datasets into smaller, manageable segments.
- **Snapshot:** A backup of the server state, critical for rollback in case of upgrade failure.

### Terminology
- **Hash Mismatch:** An error indicating a corrupted or altered patch file.
- **Air-Gapped Environment:** A network isolated from the internet for security purposes.
- **MD5 Checksum:** A hash value used to verify the integrity of update files.
- **Firewall Rules:** Network configurations that control traffic flow to and from the server.
- **Inodes:** Data structures used by Linux file systems to store information about files.

### System Context
- EPP servers are typically deployed in virtualized environments (e.g., VMware, Hyper-V, AWS) and may operate in air-gapped or restricted network setups.
- Upgrades often involve compatibility checks, disk space management, and network configuration adjustments.
- Unsupported hardware appliances or outdated OS versions can complicate upgrades.

---

## Issue Recognition & Triage

### Identifying Upgrade Issues
Common symptoms include:
- Update process stalls or fails.
- Error messages such as "Hash does not match," "Database partitions are disabled," or "Maximum retries reached."
- Persistent update notifications despite successful application.
- Server becomes inaccessible post-upgrade.
- Disk space warnings preventing upgrades.
- Connectivity issues between client machines and the server after upgrades.

### Priority Assessment
- **High Priority:** Security vulnerabilities (e.g., remote code execution), server inaccessibility, or critical functionality loss.
- **Medium Priority:** Persistent update failures, compatibility issues, or non-critical upgrade errors.
- **Low Priority:** Cosmetic issues or general inquiries about upgrade procedures.

---

## Diagnostic Methodology

### Systematic Approach
1. **Verify Environment Details:**
   - Confirm the current server version, target version, operating system, and deployment type (e.g., on-premise, cloud-hosted).
   - Identify whether the environment is air-gapped or internet-connected.
2. **Reproduce the Issue:**
   - Attempt the upgrade or patch application to gather firsthand observations.
   - Document error messages and behavior.
3. **Check Logs:**
   - Review update logs for errors or warnings.
   - Examine system logs for network or configuration issues.
4. **Assess Disk Space:**
   - Use `df -h` to check available space on critical partitions (e.g., `/boot`).
5. **Test Network Connectivity:**
   - Perform telnet tests to verify access to update servers.
6. **Apply Targeted Fixes:**
   - Use offline patches or hotfixes as needed.
   - Adjust server or network settings.
7. **Monitor Results:**
   - Confirm resolution and check for lingering issues.

---

## Information Collection

### Customer Questions
- What is the current server version and target version?
- Is the environment air-gapped or internet-connected?
- Are there any error messages during the upgrade process?
- Has a snapshot or backup been created before the upgrade?
- Are there any recent changes to the server environment (e.g., hardware upgrades)?

### Logs and Data to Collect
- **Update Logs:** Found in the Live Update section.
- **System Logs:** For network or configuration-related issues.
- **Disk Usage:** Use `df -h` to check available space.
- **Firewall Rules:** Verify port access for update servers.
- **Screenshots:** To verify error messages or interface behavior.

---

## Common Scenarios & Solutions

### Scenario 1: Hash Mismatch Error
- **Symptoms:** "Hash does not match" error during patch application.
- **Resolution:**
  1. Verify the integrity of the patch file using the MD5 checksum.
  2. Re-download the patch or use an offline patch.
  3. Delete erroneous patches from the backend if necessary.

### Scenario 2: Persistent Update Notifications
- **Symptoms:** Notifications remain after applying updates.
- **Resolution:**
  1. Check the "Applied Updates" section to confirm installation.
  2. Inform the customer that notifications may persist until the next major version release.

### Scenario 3: Database Partition Errors
- **Symptoms:** Updates fail with "Database partitions are disabled."
- **Resolution:**
  1. Deploy the Offline Partitioning Patch.
  2. Enable database partitions via the backend.

### Scenario 4: Air-Gapped Environment
- **Symptoms:** Unable to download updates due to lack of internet access.
- **Resolution:**
  1. Provide offline patches for manual upload.
  2. Guide the customer through the Offline Patch Uploader process.

### Scenario 5: Disk Space Insufficient for Upgrade
- **Symptoms:** Warnings about low disk space on `/boot` or root partitions.
- **Resolution:**
  1. Remove old kernel packages:
     ```bash
     apt-get remove --purge `dpkg -l | grep linux | awk '{print $2}' | grep <old_kernel_version>`
     ```
  2. Clear logs and backups from `/var/eppfiles/`.
  3. Reattempt the upgrade.

### Scenario 6: Connectivity Issues Post-Upgrade
- **Symptoms:** Client machines cannot connect to the server.
- **Resolution:**
  1. Verify compatibility between client and server versions.
  2. Check network configurations and firewall settings.

---

## Best Practices & Tips

### Pre-Upgrade Preparation
- Always create a snapshot or backup of the server before upgrades.
- Verify disk space and database partitioning status.
- Ensure compatibility of the OS and hardware with the target version.

### Patch Management
- Use verified patches to avoid hash mismatch errors.
- Apply patches in the correct order for sequential upgrades.

### Customer Communication
- Provide clear, step-by-step instructions for complex processes like migrations.
- Set realistic expectations about timelines and potential risks.
- Explain known interface behaviors (e.g., persistent hotfix notifications).

### Post-Upgrade Verification
- Check the "Applied Updates" section to confirm successful patch application.
- Monitor system logs for any post-upgrade anomalies.

---

## Escalation Guidelines

### When to Escalate
- Persistent server inaccessibility post-upgrade.
- Critical security vulnerabilities unresolved after patch application.
- Complex backend issues requiring DevOps intervention.

### How to Escalate
1. Gather all relevant logs and screenshots.
2. Document troubleshooting steps taken.
3. Submit a detailed escalation request to the appropriate team (e.g., Development, Customer Success).
4. Clearly state the impact on the customer and the urgency of the resolution.

---

This guide serves as a definitive reference for handling server upgrade issues in Netwrix Endpoint Protector, ensuring consistent and effective resolution across support teams. By following the outlined methodologies and leveraging case studies, support engineers can resolve these issues efficiently and effectively.