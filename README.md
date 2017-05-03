# OSP7
This is the repo for the csn232 OSP.

# ParallelDE
One usually can run only one DE ( Desktop Environment at a time)
To change the DE one has to install its required files and logout and then login again to change the DE for a different desktop experience.

This push explains how to use them in parallel and switch between them instantly.
Linux allows multi-user interface from TTY 1 to 7.
We by default are in 7.

What we need to do is download the respective DEs and create an .xinitrc executable for home directory to configure startx command to initiate a different DE session.

Then simply initiate another tty and run startx.

Switching between them simply by Ctrl+Alt+i (i can be 1 to 6) and Ctrl+Alt+7.

# downloadGUI
There are two implementations for it.
1.A simple script to intercept complete of download from wget and use pynotify and aplay to play sound.
2.The second one is interesting. We use a system call inotifywait to generate a log of all the system calls made associated to a directory (Downloads) and store them in a file test.t.
We then make a regular scan of the file test.t for 2 system calls "MOVED_TO" and "CREATE", which indicate creation of a new file within the Downloads directory. This is intercepted and then requited aplay and pynotify commands are executed.

The net effect would be that from now on any download made or any file copy created on the targeted directory (Downloads here) will suitably notify us.


# Welcome Notifications
/etc/init is run by the OS when a user logs in. The file is edited or a suitable script is added to startup to get custom welcome notes.

# Other GRUB Modifications
Other ways to customize the boot screen is to edit /etc/default/grub for relevant flags which can create required effects on boot.
