import pynotify

# Try Markup 
pynotify.init("markup") ## all smallerCase "markup"
# but in parameter, first letter capital  
pynotify.Notification("<u>Markup</u>", 
  '''
  <b>bold</b>, <i>italic</i>, <u>underline</u>
  and even <a href="http://google.com">links</a> are supported!
  '''
).show()
