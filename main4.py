from tkinter import *
from speedtest import Speedtest

def test():
    download = Speedtest().download()
    upload = Speedtest().upload()
    download_speed = round(download / (10**6), 2)
    upload_speed = round(upload / (10**6), 2)

    download_label.config(text="Download speed:\n" + str(download_speed) + " Mbit/s")
    upload_label.config(text="Upload speed:\n" + str(upload_speed) + " Mbit/s")
root = Tk()

root.title("SpeedTest")
root.geometry("400x300")

button = Button(root, text="Click to start", font=40, command=test)
button.pack(side=BOTTOM, pady=40)

download_label = Label(root, text="Download speed:\n-", font=35)
download_label.pack(pady=(50, 0))
upload_label = Label(root, text="Upload speed:\n-", font=35)
upload_label.pack(pady=10)

root.mainloop()