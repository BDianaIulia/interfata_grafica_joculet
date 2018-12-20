from Tkinter import *

linie1 = input("Introduceti prima linie: ")
linie2 = input("Introduceti a doua linie: ")
zona = input("Introduceti zona: ")
nrClick = 0

class buton(Frame):
    def __init__ ( self, master, char ):
        Frame.__init__( self, master )
        self.grid()
        self.make_button()
        self.char = char

    def make_button(self):

        self.buton = Button(self, width=2)
        self.buton["command"] = self.update
    
        self.buton.pack()

    def update(self):
        global nrClick
        self.buton["text"] = self.char
        nrClick += 1
        click["text"] = "Numar incercari: " + str(nrClick)

def find( pozitie1, pozitie2 ):
    if zona <= 2:
        if pozitie1 >= linie1:
            return 'a'
    else:
        if pozitie1 < linie1:
            return 'a'

    if zona % 2 == 1:
        if pozitie2 >= linie2:
            return 'a'
    else:
        if pozitie2 < linie2:
            return 'a'

    return 'b'

def evaluate1( event ):
    if str(eval(e1.get())) == str(linie1):
        raspuns.grid(row = 14, columnspan= 12)

def evaluate2( event ):
    if str(eval(e2.get())) == str(linie2):
        raspuns["text"] = "Felicitari! Ai aflat raspunsul corect din " + str(nrClick) + " incercari! "

root = Tk()
root.title( "Matrice" )
root.geometry( "300x400" )

click = Label(root, text="Numar incercari: " + str(nrClick))
click.grid(row=11, columnspan = 5)
l1 = Label( root, text="Linie orizontala: " )
l2 = Label( root, text="Linie verticala: " )
l1.grid(row = 12, columnspan= 4)
l2.grid(row = 13, columnspan= 4)

e1 = Entry(root)
e1.grid(row = 12, column = 4, columnspan = 5)
e2 = Entry(root)
e2.grid(row = 13, column = 4, columnspan = 5)



for i in range(10):
    for j in range(10):
        ch = find( i , j )
        x = buton( root, ch )
        x.grid(row = i , column = j)

raspuns = Label( root, text="Mai ai de aflat o linie!")
e1.bind("<Return>", evaluate1)
e2.bind("<Return>", evaluate2)

root.mainloop() 
