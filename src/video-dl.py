import customtkinter as ctk

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

app.mainloop()