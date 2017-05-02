Customizing the desktop background:
Instead of having a static background, the background can be varied continuosly at varying time intervals.

1. The wallpapers in ubuntu are stored in /usr/share/backgrounds location.
2. The various settings like duration and images are stored in xml files (trusty.xml in my case).
3. The settings can be changed as per user requirements to vary the apperarance of desktop. 

# Information from net
( Now, when you dig into where Ubuntu desktop themes, and their bundled wallpaper art, which are in /usr/share/themes and /usr/share/backgrounds - or in case you've already selected such a "live" wallpaper, you can discover where it comes from with How to find the path of the image currently used as Ubuntu desktop wallpaper. OK, so when you check out background files, you'll notice that some of these are actually XML files, like trusty.xml (named <Ubuntu code-name>.xml, for the version they shipped with). These files control what seems to be called a "background slideshow". They contain simple rules for interval, image, etc.:

I don't know how this is implemented, as I haven't found the docs for this feature, but it's probably controlled by unity or nautilus. In terms of "frame-rate", it seems even changing the wallpaper every few seconds is okay, although the shipped file does a change every few hours. The starttime tag suggests, you can pin slideshow cycles to a specific time-base, so the fades happen at certain times of day and "feel live" - depending on what you display. I'm still unsure on what starttime is based, it's not UNIX epoch, or has some bugs, I don't know but when I set it to be based on midnight, it was always off with a test wallpaper rotating every hour. But I found it reacts to local time stting, so it's based on what you set your time to in System Settings. )
