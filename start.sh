#!/bin/sh

__inf_color='\033[33m';
__err_color='\033[31m';
__log_color='\033[32m';
__end='\033[39m';

echo ${__log_color}Start AAC2...${__end}

if ! type python3 > /dev/null; then
  sudo apt-get install -y python3
fi

python3 -c "import tkinter" >/dev/null 2>/dev/null
if [ $? ]; then
  sudo apt-get install -y python3-tk
fi

sudo python3 script/aac_gui.py
echo ${__inf_color}All is initialised, now click on Download Source.${__end}
sudo python3 script/aac_gui.py
echo ${__inf_color}Sources successfully downloaded, now click on Build Options.${__end}
sudo python3 script/aac_gui.py
echo ${__log_color}If you had no errors, you ROM is successfully builded.${__end}
echo ${__log_color}Program end${__end}
