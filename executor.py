from Tkinter import *

def ShowChoice():
    if v.get() == '1':
        import pc
    if v.get() == '2':
        import matrice

app = Tk()
app.title('Application')
app.geometry('300x300')

title = Label( app , width = 10, text = "Lines'game", font=("Helvetica", 36), bd = 10, fg = 'red' , height = 2, relief=RAISED )
title.pack()

MODES = [
    ("Choose", "0"),
    ("You vs PC", "1"),
    ("PC vs You", "2"),
]

v = StringVar()
v.set("0") # initialize

for text, mode in MODES:
    b = Radiobutton(app, text = text, indicatoron = 0, command = ShowChoice,
                        variable=v, value=mode)
    b.pack()

print(mode)
app.mainloop()

