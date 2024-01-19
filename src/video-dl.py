import subprocess
import sys

from pathlib import Path
from threading import Thread

import customtkinter as ctk

# ***REMOVE THIS IMPORT LATER***
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


def get_downloads_folder():
    """
    Tries to locate the user's Downloads folder in their home directory.

    Only need to run this if user wants files downloaded there instead of
    the directory where the script was run.
    """
    try:
        dl_folder = Path.home() / "Downloads"
        if dl_folder.exists():
            return str(dl_folder)
            ic(str(dl_folder))
            ic("Download folder found")
    except:
        ic("Download folder not found")


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

    result = subprocess.run(
        ["yt-dlp", video_link, *args], capture_output=True, text=True
    )

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
    command_args = []  # arguments to pass to yt-dlp

    ic("Download button pressed")

    if sub_checkbox.get() == "on":
        command_args.append("--write-subs")

    if thumb_checkbox.get() == "on":
        command_args.append("--write-thumbnail")

    if radio_var.get() == 2:
        ic(get_downloads_folder())
        ic(isinstance(get_downloads_folder(), str))
        if isinstance(get_downloads_folder(), str) == True:
            folder_arg = "-P " + get_downloads_folder()
            ic(folder_arg)
            command_args.append(folder_arg)
            ic(command_args)

    dl_thread = Thread(target=call_yt_dlp, args=(url, *command_args))
    dl_thread.start()

    # call_yt_dlp(url, *command_args)  Commenting out to test threads


def checkbox_event():
    """
    This function should not be run directly.

    Assign this function as a parameter to a ctk checkbox object.
    """

    ic(sub_checkbox.get())
    ic(thumb_checkbox.get())


def radiobutton_event():
    """
    This function should not be run directly.

    Assign this function as a parameter to a ctk radiobutton object.

    """
    ic("Radio toggled.  Current value: ", radio_var.get())


download_folder = get_downloads_folder()  # can move this inside function

# Set up basic properties for ctk object
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
app = ctk.CTk()
app.title("video-dl")
app.geometry("800x500")
app.resizable(False, False)
app.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)

# Input box for video URL
video_url = ctk.CTkTextbox(app, width=700, height=30, activate_scrollbars=False)
video_url.insert("0.0", "Paste URL of video or playlist here")
video_url.grid(sticky="w", row=0, column=0, padx=20, pady=20)


# Frame for checkboxes
app.checkbox_frame = ctk.CTkFrame(app)
app.checkbox_frame.grid(row=100, column=0, padx=10, pady=(10, 0), sticky="w")

# Subtitle checkbox
subtitle_check = ctk.StringVar(value="on")
sub_checkbox = ctk.CTkCheckBox(
    app.checkbox_frame,
    text="Subtitles",
    command=checkbox_event,
    variable=subtitle_check,
    onvalue="on",
    offvalue="off",
)
sub_checkbox.grid(sticky="w", row=100, column=0, padx=5)

# Thumbnail checkbox
thumb_check = ctk.StringVar(value="on")
thumb_checkbox = ctk.CTkCheckBox(
    app.checkbox_frame,
    text="Thumbnail",
    command=checkbox_event,
    variable=thumb_check,
    onvalue="on",
    offvalue="off",
)
thumb_checkbox.grid(sticky="w", row=100, column=1, padx=5)


# Radio buttons for download location
radio_frame = ctk.CTkFrame(master=app, width=400, height=15)
radio_frame.grid(sticky="w", padx=20, pady=20)

radio_label = ctk.CTkLabel(radio_frame, text="Download location: ")
radio_label.grid(sticky="w", padx=20, pady=20, row=0)

radio_var = ctk.IntVar(value=1)

radio_current_folder = ctk.CTkRadioButton(
    radio_frame,
    text="Current Folder",
    command=radiobutton_event,
    variable=radio_var,
    value=1,
)
radio_current_folder.grid(sticky="w", padx=20, pady=20, row=0, column=150)

radio_downloads = ctk.CTkRadioButton(
    radio_frame,
    text="Downloads folder",
    command=radiobutton_event,
    variable=radio_var,
    value=2,
)
radio_downloads.grid(sticky="w", padx=20, pady=20, row=0, column=300)


# Textbox for file path (where to save file..default = downloads?)
# Button to select this directory


# Submit/download button
download_button = ctk.CTkButton(app, text="Download", command=dl_button_press)
download_button.grid(sticky="w", column=0, padx=20, pady=20)

"""

# Progress bar  - Possibly add in later - not yet working as expected

prog_label = ctk.CTkLabel(app, text="Progress:", fg_color="transparent")
prog_label.grid(sticky="w", padx=20)
progress_bar = ctk.CTkProgressBar(
    app, 
    orientation="horizontal", 
    height=30,
    width=300,
    mode="indeterminate"
)
progress_bar.grid(sticky="w", padx=20, pady=20)
progress_bar.set(0)

"""

# Output window for yt-dlp output
output_window = ctk.CTkTextbox(
    app,
    width=700,
    height=150,
)
output_window.insert(
    "0.0",
    "Output will be shown here.  It will only show up after the download "
    "has finished (or failed to download).",
)
output_window.grid(sticky="w", column=0, padx=20, pady=20)


app.mainloop()
