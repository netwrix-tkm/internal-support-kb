## Ticket Metadata
- **Ticket ID:** 500Qk00000MNhijIAD
- **Case Number:** 437272
- **Status:** Closed - Resolved
- **Account/Company:** AVL Tippelmann GmbH
- **Contact Name:** Detlef Janik
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Upgrade
- **Version:** Not specified

## Problem Description
The customer reported that they attempted multiple times to install backend updates, but the updates were not being applied successfully.

## Environment Details
- The EPP server is hosted on the customer's site as a virtual machine in VMware vSphere.
- The boot partition had only 233 MB of free space available.

## Troubleshooting Steps
1. Confirmed the free space on the boot partition.
2. Planned a remote session with the customer to investigate the backend.
3. Attempted to manually install the backend security updates due to insufficient space for automatic updates.
4. Suggested steps to clear space on the boot partition and reapply the updates:
   - Checked the free space using `df -h`.
   - Ran `dpkg --configure -a` to fix any broken package configurations.
   - Noted the currently running kernel version using `uname -r`.
   - Removed old kernel packages to free up space.
   - Installed the latest kernel version with `apt-get --no-install-recommends install linux-generic-hwe-22.04`.
   - Rebooted the server and verified that it was operational.

## Root Cause
The issue was primarily caused by insufficient free space on the boot partition, which prevented the backend updates from being installed automatically.

## Solution
The backend security updates were successfully applied manually after clearing space on the boot partition. The following command sequence was executed:
```bash
# Check free space
df -h

# Fix broken package configurations
dpkg --configure -a

# Note current kernel version
uname -r

# Remove old kernel packages
apt-get remove --purge `dpkg -l | grep linux | egrep -e 'linux-generic|linux-headers|linux-hwe|linux-image|linux-modules' | grep -v $(uname -r) | awk '{print $2}'`

# Install the latest kernel version
apt-get update
apt-get --no-install-recommends install linux-generic-hwe-22.04

# Reboot the server
reboot

# Remove old kernel packages
apt-get remove --purge `dpkg -l | grep linux | awk '{print $2}' | grep <old_kernel_version>`

# Final reboot to check server status
reboot
```

## Notes
- Ensure that there is adequate free space on the boot partition before attempting to install updates in the future.
- Regularly monitor the server's disk usage to prevent similar issues from occurring.
- Consider scheduling maintenance windows for updates to minimize disruption.