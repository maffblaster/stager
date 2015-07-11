
#### Preliminary plans for the installer function have been laid out in seven stages: ####

1. Gather and process hardware information.
2. Partition drives according to a default (or pre-set condition).
3. Extract compressed filesystem tarball (stage4).
4. Chroot into the newly extracted system.
5. Compile packages/kernel of choice.
6. Setup user accounts, timezone, etc.
7. Install the boot loader and EFI boot entry.
8. Reboot!

#### Preliminary plans for the recovery function: ####

1. The recovery function should work flawlessly with any stage4 backup of the root filesystem (created by Catalyst, or third party programs.)
2. Users should be able to rely on this system in case of emergency for "full metal backups".
3. Pulling the tarball over the network via protocols like http, rsync should be supported.

#### Preliminary plans for the backup function: ####

1. All Gentoo users should have a quick and effective way to create a stage4 tarball of their system.
2. Users should be able to select what directories to include and exclude and the compression type.

#### Preliminary plans for the serve function: ####

1. Accept a password entered at the command-line when the server is launched. This will provide simple protection against authorized installs.
2. Accept a profile.ini file to populate the http ui page. A profile.ini should also be able to be importable from the ui.
3. Be able to track the progress from the http ui and open a terminal to run commands manually if desired.