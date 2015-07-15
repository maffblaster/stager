FAQ
-----

**Q:** What will happen if there are command-line options passed *and* a profile at the same time? For example <tt>stager backup --profile /tmp/backup.ini --exclude /sys /proc /dev --destination /tmp/backup</tt>

**A:** In the situation that command line options are provided along side a profile, the command-line options will overwrite any set values in the profile.