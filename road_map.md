Road map
-----

0.0.4 - Properly package software (Python module).

0.0.3 - Add support for json configuration files.

0.0.2 - Validate and parse command-line arguments. Start writing tests. - In process...

0.0.1 - <s>Prototype a (rough) command-line interface for stager.</s> - Complete!

### Installation stages

Preliminary plans for the installer function have been laid out in seven stages:

1. Gather and process hardware information. This step should prep the system based on hardware, if possible.
2. Partition drives according to a default (pre-set) condition.
3. Extract compressed filesystem tarball (stage file).
4. Chroot into the newly extracted system.
5. Compile packages/kernel of choice.
6. Setup user accounts, configure system, etc. Integrate with [Ansible](https://www.ansible.com/)?
7. Install the boot loader. Reboot!

## Feature requests

Many of the feature requests printed here have been taken from the [request for comments (RFC) e-mail](https://archives.gentoo.org/gentoo-dev/message/361f30d23a4740e0f2e820ab4455ae21) on the gentoo-dev mailing list.

* Eventual support for embedded platforms like PPC, ARM (particular arm8v).
* Use USB media and persistence as the primary media for installation (instead of CD/DVDs).

## Comments / Feedback

* "If you can start with the simplest use-case and increase complexity gradually you will succeed. It is an exercise of patience and I praise you for giving it a try." -Luca Barbato

* "In the ideal world it would be nice to have such stage4 ebuilds available to speed-up initial installation and configuration process." -Andrew Savchenko

