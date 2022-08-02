from tkinter import Tk, PhotoImage, Label

root = Tk()
root.overrideredirect(1)
root.wm_attributes('-topmost', True)
root.wm_attributes('-transparent', True)


root.geometry('300x300')
root.config(bg='systemTransparent')

label = Label(root)
# label.config(bg='black')
label.config(bg='systemTransparent')
label.pack()
frame = 1
fps = 10


def update():
    global frame
    try:
        root.image = PhotoImage(
            file='./ezgif.com-gif-maker-2.gif', format=f'gif -index {frame}')
        frame += 1
    except Exception:
        frame = 1
    label.config(image=root.image)
    root.after(int(1000/fps), update)


root.after(0, update)

root.mainloop()
