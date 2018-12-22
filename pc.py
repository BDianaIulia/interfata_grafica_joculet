from Tkinter import *
import generator as g
import functii as f


class buton(Frame):
    def __init__ ( self, master, char ):
        Frame.__init__( self, master )
        self.grid()
        self.make_button()
        self.char = char

    def make_button(self):
        self.buton = Button(self, width=2)
        self.buton.pack()


def evaluate1( event ):
    global linie1
    linie1 = int(e1.get())
    start()
    
def evaluate2( event ):
    global linie2
    linie2 = int(e2.get())
    start()

def evaluate3( event ):
    global zona
    zona = int(e3.get())
    start()


def start():
    global linie1
    global linie2
    global nrClick
    global zona
    global ButtonsList
    
    if linie1 != 0 and linie2 != 0 and zona != 0:
        my = f.Matrice( linie1, linie2, zona )
        for i in range(1, 11):
            for j in range(1, 11):
                ch = my.find(i, j)
                x = buton( root, ch )
                x.grid(row = i , column = j)
                ButtonsList.append(x)
                
        calc = f.Calculator()
        while calc.raspuns[0] == 0:
            (p1, p2) = calc.fabrica_intrebari()
            calc.adaugareRaspuns( p1, p2, my.find( p1, p2 ) )
            root.update()
            timp = 6000000 * 2
            while timp:
                timp -= 1
            it = ButtonsList[ 10 * (p1-1) + (p2-1) ]
            it.buton["text"] = it.char
            nrClick += 1
            click["text"] = "Numar incercari: " + str(nrClick)
        raspuns = Label( root, text = "Raspunsul s-a aflat din " + str(nrClick) + " incercari!")
        raspuns.grid(row = 15, columnspan= 12)
        for it in ButtonsList:
            if it.char == 'b':
                it.buton.configure( text = it.char , fg = 'blue' )
            else:
                it.buton["text"] = it.char
                
linie1 = 0
linie2 = 0
zona = 0
nrClick = 0
ButtonsList = []
        
root = Tk()
root.title( "Matrice" )
root.geometry( "300x400" )

click = Label(root, text="Numar incercari: " + str(nrClick))
click.grid(row=11, columnspan = 6)
l1 = Label( root, text="Linie orizontala: " )
l2 = Label( root, text="Linie verticala: " )
l3 = Label( root, text ="Zona: ")
l1.grid(row = 12, columnspan= 4)
l2.grid(row = 13, columnspan= 4)
l3.grid(row = 14, columnspan= 4)

e1 = Entry(root)
e1.grid(row = 12, column = 4, columnspan = 5)
e2 = Entry(root)
e2.grid(row = 13, column = 4, columnspan = 5)
e3 = Entry(root)
e3.grid(row = 14, column = 4, columnspan = 5)

e1.bind("<Return>", evaluate1)
e2.bind("<Return>", evaluate2)
e3.bind("<Return>", evaluate3)

        
raspuns = Label( root, text="Mai ai de aflat o linie!")


root.mainloop() 
