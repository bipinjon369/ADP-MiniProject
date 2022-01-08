from tkinter import *
import re
#function decalred to center the login/register window to any screen aspect 
def center(window):
    app_width=1000 
    app_height=600
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x=(screen_width / 2) - (app_width/2)
    y=(screen_height / 2) - (app_height/2)
    window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
    window.deiconify()
#using regex to check if emails are in the correctr format
def emailformat(email):
    email_regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    match=email_regex.match(email)
    return match