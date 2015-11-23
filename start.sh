#!/bin/sh

echo Start AAC2...
sudo apt-get install python3-tk
sudo python3 script/aac_gui.py
echo All is initialised, now click on Download Source.
sudo python3 script/aac_gui.py
echo Sources successfully downloaded, now click on Build Options.
sudo python3 script/aac_gui.py
echo If you had no errors, you ROM is successfully builded.
echo Program end
