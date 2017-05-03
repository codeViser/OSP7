# OSP7
This is the repo for the csn232 OSP.

# Customizing the desktop background:
Instead of having a static background, the background can be varied continuosly at varying time intervals.

The wallpapers in ubuntu are stored in /usr/share/backgrounds location.
The various settings like duration and images are stored in xml files (trusty.xml in my case).
The settings can be changed as per user requirements to vary the apperarance of desktop. 
 
The start-time for the variation can be set using the starttime tag in the xml file. Settings can be added and the new xml file can be stored in the specific location containing trusty.xml file.

# Adding boot sound 
The sound is added at the instant just before the bootloader screen where we can select the os to boot.

For this, changes can be made in the etc/default/grub file. GRUB_INIT_TUNE can be set at the desired value to play the sound at grub startup as required by the user. The value is given in the form of a series of numbers.

The syntax is: GRUB_INIT_TUNE="tempo [pitch1 duration1] [pitch2 duration2] ..."
