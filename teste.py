from tkinter import *

def label_text():
    label.config(text=entry.get())
    return app.update()

def keybind(event):
    print(event)
    return event


app = Tk()
app.geometry('500x300')

label = Label(app, text='Nada')
label.pack()

entry = Entry(app)
entry.pack(ipadx=100)
entry.bind('<Key>', keybind)

btn = Button(app, text='Mudar label', command=label_text)
btn.pack()


app.mainloop()