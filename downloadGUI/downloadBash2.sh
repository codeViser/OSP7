while true; do

#system call 
inotifywait /home/shubham/Downloads --recursive --monitor > test.t &

#Also can use MOVED_TO

if grep -q CREATE test.t; then
    python downloadTalk.py
	aplay /home/shubham/Documents/git/OSP7/resources/file_transfer_completed.wav
	echo found
else
	echo not found
fi

done
