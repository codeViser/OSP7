#!/bin/bash

echo Download link please?
read linkURL

wget linkURL

python downloadNoti.py

aplay ../resources/Download_completed_successfully.wav

