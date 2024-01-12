import customtkinter as ctk
import subprocess
import sys

# ***REMOVE THIS IMPORT LATER, IT IS NOT IN REQUIREMENTS.TXT***
from icecream import ic  # For debugging

# Make sure user has yt-dlp working
try:
    subprocess.run(
        ["yt-dlp", "--help"],
        stdout = subprocess.DEVNULL
    )
except Exception as e:
    print("There was an error with yt-dlp.  Make sure you are"
      " able to run yt-dlp from the command line.\n")
    print(f"Error details: {e}")
    sys.exit(1) # terminates program


testing_video = ""
command_args = [] # arguments to pass to yt-dlp

def call_yt_dlp(*args):
    """
    Executes yt-dlp and returns the command's output
    """
    result = subprocess.call(["yt-dlp", testing_video])
    
    return result
    
# Set up basic properties for ctk object
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
app = ctk.CTk()
app.title("video-dl")
app.geometry("800x500")
app.resizable(False, False)

# Input box for video URL
video_url = ctk.CTkTextbox(
    app, 
    width = 700,
    height = 30,
    activate_scrollbars = False
)
video_url.insert("0.0", "Paste URL of video here")
#video_url_output = video_url.get("0.0", "end") # Use later to get text


# Textbox for file path (where to save file..default = downloads?)
# Button to select this directory


# Output window for yt-dlp output
output_window = ctk.CTkTextbox(
    app,
    width = 700,
    height = 150,
)    
output_window.insert("0.0", "Output will be shown here")





# Layout
# grid method places widgets directly under the previous one by default

video_url.grid(padx = 20, pady = 20)
output_window.grid(padx = 20, pady = 20)


# Run yt-dlp to fetch video
call_yt_dlp()



app.mainloop()