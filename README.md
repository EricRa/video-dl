# video-dl
A GUI for yt-dlp

## Status

Minimal app is now working.  

- The only note is that, for now, "icecream" is an additional dependency that must be installed for the script to run.  I'm using it as a debugging tool and may be included in the code here and there.  I'll remove it eventually.

## Requirements

- This has mostly been tested with python 3.12.0 on Windows 10.  In theory, it is cross-platform and should work with any OS and any somewhat recent version of Python 3.

	- Additionally, there may be some cosmetic issues with the UI if using a python version below 3.10.
	
- yt-dlp

	- yt-dlp needs to be installed for this to work.  I chose not to bundle it because yt-dlp is updated quite often to ensure compatibility with different video sites.
	
	- You should keep yt-dlp up to date to get the best results.  For testing, yt-dlp version 2023.12.30 was used.
	
	
## Installation and usage

- First, install yt-dlp if you don't have it:
	>pip install yt-dlp

- Upgrade it:
	> pip install yt-dlp --upgrade

- Be sure that yt-dlp is working from the command line.  Make sure this runs:
	> yt-dlp --help
	
- Install dependencies from requirements.txt in this repo.  Can do this manually in pip or can download the file and (with requirements.txt in the same directory):
	> pip install -r requirements.txt
	
- Now you can just run the script (video-dl.py) to start the GUI.


## License

- This software is MIT licensed.
