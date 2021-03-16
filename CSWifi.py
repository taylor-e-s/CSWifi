#Taylor Shirk  Claire DeVinney
import tkinter
parent = tkinter.Tk()
parent.overrideredirect(1)
parent.iconbitmap("PythonIcon.ico")
parent.withdraw()
from tkinter import messagebox

def get_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)

def disconnection_warning():
    yesno = messagebox.askyesno('Your internet connection has been lost.', 'Would you like to reconnect it?', parent=parent)

#attempting to connecting to wifi
from wifi import Cell, Scheme
Cell.all('wlan0')
