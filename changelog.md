Changelog
===== 

This file is maintained for a high-level overview of changes. Look at the commit history for all the details.

#### 0.0.02 (pre-alpha) ####

* 

#### 0.0.01 (pre-alpha) ####

* Design updates:
 * Imported  stage7 Python 3 project.
 * Changed program name from <tt>stage</tt> to <tt>stager</tt>.
 * Reset versioning from 2.x.xx to 0.x.xx.
 * Added consistency to options (<code>-p</code> is *always* <code>--profile</code>).
 * Made argument descriptions lowercase.
 * Refined serve command options (<code>--url</code>, <code>--port</code>).
 * Changed verbosity/quiet option to set an integer level for future expansion  (<code>-1</code>, <code>0</code>, <code>1</code>).
 * Added maintainable meta-variables (__status__, etc.) for <tt>stager --help</tt> output.
 * Added type checking (mostly <code>str</code>) for arguments/options.
 * Subcommands can (now) be properly shortened (<tt>i</tt>, <tt>b</tt>, <tt>r</tt>, <tt>s</tt>)
 * <code>metavar</code> enables a pretty display of arguments.
 * <code>action=count</code> added to <code>--verbose</code> option for future expansion (multiple levels of verbosity).
 * 