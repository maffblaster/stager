Design
-----


## Configuration priorities

Configuration arguments passed on the command-line will override arguments found in configuraiton files.

## Workflow

The process to get the installer running on the system would be as follows:

 1. Boot the live installation media.
 * This will get the environment to a place where stager will run.
  * Grub -> Kernel -> Initramfs -> init
  * Attached NICs will be configured to DHCP by default (can be adjusted via a kernel cmdline argument: `stager.nodhcp`)
 2. Start `stager` on a tty
 * Parse the currenly running environment to gather information on available system functionality
  * Software
   * Kernel filesystem support
   * Userspace filesystem tools
  * Hardware
   * PCI devices
    * Disks
    * NICs
    * Audio
    * Graphic cards
   * USB devices
    * NICs
   * CPU (Intel or AMD)
    * Flags
 3. `stager` will generate a authentication token and print the IP address/port to the tty
 4. The user will connect to `stager` via a 'thin client'.
 * To populate the system, the user can then:
  * Upload a pre-made configuration file (json) to be parsed, loaded by stager.
   * stager will compare the attempted configuraiton file against the current system and raise errors if something doesn't 'line up' (missing support for something).
  * Hand configure the system disks / NICs / Timezone / Keymap / etc. through web interface
 5. After configuration is finished, the user then will press "Go!" and watch the installer run.
 * User can choose to have the system restart after upon successful installation.
  * Once the installation is finished the user can also have an option to export the working configuration to the clound (GitHub gist, pastebin, etc.) or into the working system.
