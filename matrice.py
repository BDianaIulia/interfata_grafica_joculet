from Tkinter import *
import generator as g

linie1, linie2, zona = g.generator_input()
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
    global ok1
    global ok2
    if str(eval(e1.get())) == str(linie1):
        raspuns.grid(row = 14, columnspan= 12)
        if ok2:
            evaluate2( event )
        else:
            raspuns["text"] = "Mai ai de aflat o linie!"
        ok1 = 1
    else:
        raspuns.grid(row = 14, columnspan= 12)
        raspuns["text"] = "Ai gresit!"

def evaluate2( event ):
    global ok1
    global ok2
    if str(eval(e2.get())) == str(linie2):
        ok2 = 1
        if ok1:
            raspuns["text"] = "Felicitari! Ai aflat raspunsul corect din " + str(nrClick) + " incercari! "
            for it in ButtonsList:
                if it.char == 'b':
                    it.buton.configure( text = it.char , fg = 'blue' )
                else:
                    it.buton["text"] = it.char
        else:
            raspuns.grid(row = 14, columnspan= 12)
            raspuns["text"] = "Mai ai de aflat o linie!"
    else:
        raspuns.grid(row = 14, columnspan= 12)
        raspuns["text"] = "Ai gresit!"

        
root = Tk()
root.title( "Matrice" )
root.geometry( "300x400" )

ok1 = 0
ok2 = 0

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


ButtonsList = []
for i in range(10):
    for j in range(10):
        ch = find( i , j )
        x = buton( root, ch )
        x.grid(row = i , column = j)
        ButtonsList.append(x)

raspuns = Label( root, text="Mai ai de aflat o linie!")
e1.bind("<Return>", evaluate1)
e2.bind("<Return>", evaluate2)

root.mainloop() 
