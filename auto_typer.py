import pyautogui
import keyboard
from tkinter import *
import tkinter as tk
root = tk.Tk()
root.geometry("440x550")
root.configure(bg='black')
photo = PhotoImage(file = "./extrafiles/background.png")
root.resizable(False, False)
label=Label(root, image=photo)
label.place(x=0,y=0)

def getTextInput():
    result=textExample.get("1.0","end")
    result1 = secs.get()
    pyautogui.typewrite(result, interval=result1)
    #print(result)


textExample=tk.Text(root, height=24,bg='white',border=0,width=40)
textExample.place(x=60,y=54)
secs=tk.Entry(root,bg='white',border=0,font=('arial',14,'bold'),width=5)
secs.place(x=254,y=480)
img0 = PhotoImage(file = f"./extrafiles/img0.png")
b0 = Button(image = img0,borderwidth = 0,highlightthickness = 0,command = getTextInput,relief = "flat",bg='#4D4C4C')
b0.place(x = 99, y = 469,width = 97,height = 45)



root.mainloop()