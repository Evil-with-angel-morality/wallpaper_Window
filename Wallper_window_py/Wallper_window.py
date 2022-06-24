from ctypes import *
from tkinter import *
from pymsgbox import confirm

#wall1 = "C:\\Users\\Hossein\\Desktop\\wall1.png".encode()
#windll.user32.SystemParametersInfoA(20 , 0 , c_char_p(wall1),0)


window = Tk()
window.title("Wallper window")
window.minsize(350,120)
window.maxsize(350,150)

def start():

    text = "Are You Sure about this ?"
    title = "Are You Sure about this ?"
    output = confirm(text = text , title = title , buttons = ("YES" , "NO"))

    if output == "YES":
        windll.user32.SystemParametersInfoA(20 , 0 , c_char_p(poto.get),0)
    elif output == "NO":
        print("oK :(")


Label(window, text="Enter the photo path").pack()
poto = Entry(window)
poto.pack()

btn = Button(window,text="set Wallper windows",command=start)
btn.pack()

window.mainloop()