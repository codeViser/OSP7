import pynotify

# Only Text Notification
pynotify.init('Basic')
pynotify.Notification("File Transfer", "Completed Successfully").show()
