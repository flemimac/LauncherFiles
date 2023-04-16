import os 
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import OK, INFO, showinfo 

window = Tk()
window.title("Launcher Files")
window.geometry("600x300")
window.configure(background='#8983B1')

def Information():
    showinfo(title="Запуск...", message="Программа запускается! Ждите...", icon=INFO,  default=OK)

def OpenFiles(a):
    os.startfile(a)
    Information()
    


label = Label(window, text='Выбери необходимые файлы для открытия', width=40, height=20, font=5, bg='#8983B1', fg='#373543')

button_paint = Button(window, text='Paint', width=4, height=1, bg='#928EB1', command=lambda: OpenFiles(r'C:\Windows\system32\mspaint.exe'))
button_chrome = Button(window, text='Chrome', width=6, height=1, bg='#928EB1', command=lambda: OpenFiles(r'C:\Program Files\Google\Chrome\Application\chrome.exe'))
button_TLauncher = Button(window, text='TLauncher', width=7, height=1, bg='#928EB1', command=lambda: OpenFiles(r'C:\Users\CODOLOGIA\AppData\Roaming\.minecraft\TLauncher.exe'))
button_RobloxStudio = Button(window, text='Roblox Studio', width=12, height=1, bg='#928EB1', command=lambda: OpenFiles(r'C:\Users\CODOLOGIA\AppData\Local\Roblox\Versions\version-161ebe8a914a48fa\RobloxStudioLauncherBeta.exe'))
button_MCreator = Button(window, text='MCreator', width=12, height=1, bg='#928EB1', command=lambda: OpenFiles(r'C:\Program Files\Pylo\MCreator\mcreator.exe'))


label.place(x=130, y=-150)
button_paint.place(x=100, y=80)
button_chrome.place(x=150, y=80)
button_TLauncher.place(x=220, y=80)
button_RobloxStudio.place(x=300, y=80)
button_MCreator.place(x=415, y=80)

window.mainloop()