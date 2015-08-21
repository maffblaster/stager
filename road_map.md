## Goals ##

0.0.5 - Properly package software (module).

0.0.4 - Get backup functionality operational.

0.0.3 - Add support for ini-style profiles.

0.0.2 - Validate and parse command-line arguments. Start writing tests. - In process...

0.0.1 - <s>Prototype a (rough) command-line interface for stager.</s> - Complete!

### Preliminary plans for the installer function have been laid out in seven stages: ###

1. Gather and process hardware information. This step should prep the system based on hardware, if possible.
2. Partition drives according to a default (pre-set) condition.
3. Extract compressed filesystem tarball (stage4).
4. Chroot into the newly extracted system.
5. Compile packages/kernel of choice. This is dangerous and it might not be possible to do this well.
6. Setup user accounts, timezone, etc.
7. Install the boot loader and EFI boot entry. Reboot!

### Preliminary plans for the recover function: ###

1. The recovery function should work flawlessly with any stage4 backup of the root filesystem (created by Catalyst, GRS suite, or third party programs.)
2. Users should be able to rely on this system in case of emergency for "full metal backups".
3. Pulling the tarball over the network via protocols like http, rsync should be supported.

### Preliminary plans for the backup function: ###

1. All Gentoo users should have a quick and effective way to create a stage 4 tarball (bare metal backup) of their system.
2. Users should be able to select what directories to include and exclude and the compression type.
3. Users should be able to use command-line options or the .ini file to provide configuration for backups.

### Preliminary plans for the serve function: ###

1. Accept a password entered at the command-line when the server is launched. This will provide simple protection against authorized installs.
2. Accept a profile.ini file to populate the http ui page. A profile.ini should also be able to be importable from the ui as well.
3. Be able to track the progress from the http ui and open a terminal (either by enabling <tt>ssh</tt> or through the UI) to run commands manually.

## Feature requests ##

Many of the feature requests printed here have been taken from the [request for comments (RFC) e-mail](https://archives.gentoo.org/gentoo-dev/message/361f30d23a4740e0f2e820ab4455ae21) on the gentoo-dev mailing list.
 
 * Eventual support for  embedded platforms like PPC, ARM (particular 
arm8v) as well as new files systems (btrfs).
* Use USB media and persistence as the primary media for installation (instead of CD/DVDs).

## Comments ##

* "If you can start with the simplest use-case and increase complexity
gradually you will succeed. It is an exercise of patience and I praise you for giving it a try." -Luca Barbato

* "In the ideal world it would be nice to have such stage4 ebuilds
available to speed-up initial installation and configuration
process." -Andrew Savchenko

