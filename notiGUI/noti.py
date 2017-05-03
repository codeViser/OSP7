import pynotify

# Only Text Notification
pynotify.init('Basic')
pynotify.Notification("Title", "simple text").show()


# Lets try with an image
pynotify.init('Image')
## Use absolute Path of the photo
pynotify.Notification("Title", "My Photo here!!", "/home/nafis/Pictures/me.png").show()

# Try Markup 
pynotify.init("markup") ## all smallerCase "markup"
# but in parameter, first letter capital  
pynotify.Notification("Markup", 
  '''
  <b>bold</b>, <i>italic</i>, <u>underline</u>
  and even <a href="http://google.com">links</a> are supported!
  '''
).show()

#sound produce
echo -e "\a"

#Notification message through cmd
notify-send "Job finished!"
