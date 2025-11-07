from tkinter import * 
from tkinter import messagebox
from datetime import datetime
from PIL import ImageTk, Image
import pytz
import requests

window=Tk()

window.geometry('420x420')

window.title ("Bot Manager for telegram")

icon = Image.open( "icon.png")
icon_img = ImageTk.PhotoImage(icon)
window.iconphoto(False, icon_img)

window.mainloop()

