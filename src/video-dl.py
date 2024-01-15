import customtkinter as ctk
import subprocess
import sys

# ***REMOVE THIS IMPORT LATER, IT IS NOT IN REQUIREMENTS.TXT***
from icecream import ic  # For debugging

# Make sure user has yt-dlp working
try:
    subprocess.run(["yt-dlp", "--help"], stdout=subprocess.DEVNULL)
except Exception as e:
    print(
        "There was an error with yt-dlp.  Make sure you are"
        " able to run yt-dlp from the command line.\n"
    )
    print(f"Error details: {e}")
    sys.exit(1)  # terminates program


testing_video = ""
video_link = ""
console_output = []
command_args = []  # arguments to pass to yt-dlp


def call_yt_dlp(video_link, *args):
    """
    Executes yt-dlp and returns the command's output.

    video_link is required and should be the URL string to the video
    to be downloaded.

    Other arguments should be strings, as they will be appended in order
    after the URL when invoking yt-dlp.

    We also capture console output here (both stdout and stderr) and append
    them as string objects to the console_output list initialized above.  Then,
    we can print those out.

    """
    result = subprocess.run(["yt-dlp", video_link], capture_output=True, text=True)

    console_output.append(result.stdout)
    console_output.append(result.stderr)

    for item in console_output:
        output_window.insert("0.0", "\n")
        output_window.insert("0.0", item)

    return result


def dl_button_press():
    """
    This function should not be run directly for the purposes of this script.

    Assign this function as a parameter when initalizing a customtkinter
    button object.  The function will then run any time the button is pressed.
    """

    url = video_url.get("0.0", "end")  # gets URL from video_url text box

    call_yt_dlp(url)


# Set up basic properties for ctk object
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
app = ctk.CTk()
app.title("video-dl")
app.geometry("800x500")
app.resizable(False, False)
app.grid_columnconfigure(0, weight=1)

# Input box for video URL
video_url = ctk.CTkTextbox(app, width=700, height=30, activate_scrollbars=False)
video_url.insert("0.0", "Paste URL of video here")
video_url.grid(sticky="w", row=0, column=0, padx=20, pady=20)


# Textbox for file path (where to save file..default = downloads?)
# Button to select this directory


# Submit/download button
download_button = ctk.CTkButton(app, text="Download", command=dl_button_press)
download_button.grid(sticky="w", column=0, padx=20, pady=20)

# Output window for yt-dlp output
output_window = ctk.CTkTextbox(
    app,
    width=700,
    height=150,
)
output_window.insert("0.0", "Output will be shown here")
output_window.grid(sticky="w", column=0, padx=20, pady=20)


# Layout
# grid method places widgets directly under the previous one by default

video_url.grid(padx=20, pady=20)
output_window.grid(padx=20, pady=20)


app.mainloop()
