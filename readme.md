1. lock_unlock_sound.sh : This file will simply produce a sound whenever you lock your pc or reopen it (say using Win+L). The music file is uploaded along with it in the same directory. To make it work the script must run beforehand. This can be done by going in the StartUpApplications and "Add" a new feature to make it run using
 `bash lock_unlock_sound.sh` command.

2. PROXY_CHANGE: One of my favourites. For some of some us altering proxy becomes very cumbersome. So to overcome it this file will toggle betweem ,`manual` and `none` proxy. All you have to do is initially set up the manual proxy in the gloabal settings (UI or via terminal). Second go to keyboard shortcuts and add a new shortcut example `ctrl+alt+p` for the proxy toggle.

3. BRIGHTNESS_CONTROL : This problem was something, i guess specific to my laptop, the brightness keys NOT WORKING. So i have created the brightness_change.py file to control it as below:
	* to increase `python3 brightness_change.py -u` in the shell
	* to decrease `python3 brightness_change.py -d` in the shell
also later you have to allot the specific keys of your laptop to the respective features by setting up the keyboard shortcuts. Enjoy!
