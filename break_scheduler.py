import time
import os
import webbrowser
import tkinter as tk
from tkinter import ttk

NORM_FONT= ("Verdana", 10)
def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("Message")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    popup.geometry("400x400+120+120")
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

n=3600  #Time after which break takes place (its in seconds)(so after 1 hour, break will take place )(1 hour=3600 seconds)
m=5   # no of times break takes place (its in seconds) (the break will take place 5 a day after every 1 hour)
o=900   #time ater which break gets over (its in seconds)(the break will be for 15 minutes each)(15 minutes=900seconds)
i=0
while(i<m):
    i=i+1
    popupmsg("Work Hard till Break")
    print("Work Hard till Break")
    start_time = time.time()
    time.sleep(n)
    elapsed_time = time.time() - start_time
    popupmsg("Now it's Break Time")
    print("You Worked for:",elapsed_time/3600," hour")
    if i==1:
        print("Time to go for break, Read some news.")
        popupmsg("Time to go for break, Read some news.")
        webbrowser.open('https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en')
        start_time1 = time.time()
        time.sleep(o)
        print("Get back to work")
        popupmsg("Get back to work")
        elapsed_time1 = time.time() - start_time1
        print("You took Break for:",elapsed_time1/60," minutes")
        browserExe = "chrome.exe"
        os.system("taskkill /f /im "+browserExe)
    elif i==2:
        print("Time to go for break, Listen to some Music.")
        popupmsg("Time to go for break, Listen to some Music.")
        webbrowser.open('https://www.youtube.com/')
        start_time1 = time.time()
        time.sleep(o)
        popupmsg("Get back to work")
        print("Get back to work")
        elapsed_time1 = time.time() - start_time1
        print("You took Break for:",elapsed_time1/60," minutes")
        browserExe = "chrome.exe"
        os.system("taskkill /f /im "+browserExe)
    elif i==3:
        print("Time to go for break, Learn about new technologies coming.")
        popupmsg("Time to go for break, Learn about new technologies coming.")
        webbrowser.open('https://www.gadgetsnow.com/tech-news')
        start_time1 = time.time()
        time.sleep(o)
        print("Get back to work")
        popupmsg("Get back to work")
        elapsed_time1 = time.time() - start_time1
        print("You took Break for:",elapsed_time1/60," minutes")
        browserExe = "chrome.exe"
        os.system("taskkill /f /im "+browserExe)
    elif i==4:
        print("Time to go for break, read this article")
        popupmsg("Time to go for break, read this article")
        webbrowser.open('https://www.theverge.com/2018/8/17/17724658/screen-time-blue-light-blindness-sciencel')
        start_time1 = time.time()
        time.sleep(o)
        print("Get back to work")
        popupmsg("Get back to work")
        elapsed_time1 = time.time() - start_time1
        print("You took Break for:",elapsed_time1/60," minutes")
        browserExe = "chrome.exe"
        os.system("taskkill /f /im "+browserExe)
    elif i==5:
        print("Time to go for break, Listen to Music")
        popupmsg("Time to go for break, Listen to Music")
        webbrowser.open('https://www.youtube.com/')
        start_time1 = time.time()
        time.sleep(o)
        print("Get back to work")
        popupmsg("Get back to work")
        elapsed_time1 = time.time() - start_time1
        print("You took Break for:",elapsed_time1/60," minutes")
        browserExe = "chrome.exe"
        os.system("taskkill /f /im "+browserExe)
