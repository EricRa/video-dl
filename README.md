# video-dl
A GUI for yt-dlp


![Screenshot of video-dl application on Windows 10.](/media/video-dl.png)

## Status

App is now working as of 1-19-24.  All currently displayed features are tested and working on Windows.

This is still in very early stages, so any feedback or issue submissions are welcome.

I will continue to add features as I have time.


## Requirements/Dependencies

This has mostly been tested with python 3.12.0 on Windows 10.  It has also been verified to work on Ubuntu Linux, but it has not been extensively tested there.

In theory, it is cross-platform and should work with any OS and any somewhat recent version of Python (>=3.7).

There may be some minor cosmetic issues with the UI if using a python version below 3.10.
	
### yt-dlp

yt-dlp needs to be installed for this to work.  I chose not to bundle it because yt-dlp is updated quite often to ensure compatibility with different video sites.
	
You should keep yt-dlp up to date to get the best results.  For testing, yt-dlp version 2023.12.30 was used.
	
### Additional Requirements

	- customtkinter
	- icecream  (Currently using this for debugging.  Necessary for now, but will remove later.)
	
## Installation and usage

- First, install yt-dlp if you don't have it:
	>pip install yt-dlp

- Upgrade it:
	> pip install yt-dlp --upgrade

- Be sure that yt-dlp is working from the command line.  Make sure this runs:
	> yt-dlp --help
	
- Install dependencies from requirements.txt in this repo.  Can do this manually in pip or can download the file and (with requirements.txt in the same directory):
	> pip install -r requirements.txt
	
- Now you can just run the script (video-dl.pyw) to start the GUI.
	- Note that the .py and .pyw scripts have identical contents.  You should run the .pyw extension on Windows if you want to prevent a console window from opening.  That's the only difference.
	
- By default, videos will download in the same folder as the script, but there is an option in the GUI to change this to the system Downloads folder.


## License

- This software is MIT licensed.
