from ctypes import *
from tkinter import *
import time

#wall1 = "C:\\Users\\Hossein\\Desktop\\wall1.png".encode()
#windll.user32.SystemParametersInfoA(20 , 0 , c_char_p(wall1),0)






def wallper_photo():
    window = Tk()
    window.title("Wallper window")
    window.minsize(350,150)
    window.maxsize(350,150)
    def sign_in():
        na = name.get()
        wall1 = na.encode()
        windll.user32.SystemParametersInfoA(20 , 0 , c_char_p(wall1),0)
    Label(window, text="").pack()
    Label(window, text="Pach photo").pack()
    Label(window, text="").pack()
    name = Entry(window)
    name.pack()
    Label(window, text="").pack()
    btn = Button(window,text="Set Wallper",command=sign_in)
    btn.pack()
    window.mainloop()










def wallper_gif():
    win = Tk()
    win.title("Wallper window")
    win.minsize(350,400)
    win.maxsize(350,400)

    def sign_in():
        na = name.get()
        wall1 = na.encode()

        na_two = name_two.get()
        wall2 = na_two.encode()

        name_thi = name_thir.get()
        wall3 = name_thi.encode()

        n_time = name_time.get()
        timm = int(n_time)

        while True:
            time.sleep(timm)
            windll.user32.SystemParametersInfoA(20 , 0 , c_char_p(wall1),0)
            time.sleep(timm)
            windll.user32.SystemParametersInfoA(20 , 0 , c_char_p(wall2),0)
            time.sleep(timm)
            windll.user32.SystemParametersInfoA(20 , 0 , c_char_p(wall3),0)
    
    Label(win, text="").pack()
    Label(win, text="Pach photos 1").pack()
    Label(win, text="").pack()
    name = Entry(win)
    name.pack()

    Label(win, text="Pach photos 2").pack()
    Label(win, text="").pack()
    name_two = Entry(win)
    name_two.pack()

    Label(win, text="Pach photos 3").pack()
    Label(win, text="").pack()
    name_thir = Entry(win)
    name_thir.pack()

    Label(win, text="time photo").pack()
    Label(win, text="").pack()
    name_time = Entry(win)
    name_time.pack()

    Label(win, text="").pack()
    btn = Button(win,text="Set Wallper",command=sign_in)
    btn.pack()
    win.mainloop()














root = Tk()
root.title("Wallper window")
root.minsize(600,400)
root.maxsize(600,400)

Label(root, text="").pack()
Label(root, text="wallper window").pack()
Label(root, text="").pack()
Label(root, text="").pack()
Label(root, text="").pack()
btn = Button(root,text="   Set wallper by photo   ",command=wallper_photo)
btn.pack()
Label(root, text="").pack()
btn = Button(root,text="    Set Wallper by gif    ",command=wallper_gif)
btn.pack()

root.mainloop()
