###modul principal aplicatie joc
#acest modul doar apeleaza datele din modulele <generator.py> si <functii.py>

import generator        #modul pentru generare posibile cazuri
import functii as f     #modul care implementeaza algoritmul


#Daca se doreste a se baga input de la tastatura:
'''linie1 = input( "linie1: ")
linie2 = input( "linie2: ")
zona = input( "zona: ")
my = Matrice( linie1, linie2, zona )'''


#cream 5 teste
#datele necesare le luam din modulul de generator( cele 2 linii si zona in care se afla b)
#rezultatele le punem in fisiere text
n = 5  
while n:
    File = open( 'test' + str(n) , 'w' )
    
    linie1, linie2, zona = generator.generator_input()
    File.write( "liniile: {} {} \n".format( linie1, linie2 ) )
    File.write( "zona: {} \n".format(zona) )
    
    utilizator = f.Matrice( linie1, linie2, zona )      #instanta a player-ului 
    calculator = f.Calculator()                        #instanta a calculatorului


#cat timp nu s-au gasit ambele raspunsuri (cele 2 linii trasate),
#calculatorul proceseaza intrebari( interogheaza o pozitie din matrice),
#iar utilizatorul raspunde
    while calculator.raspuns[0] == 0 or calculator.raspuns[1] == 0:
        (p1, p2) = calculator.fabrica_intrebari()
        File.write( "{} {} \n".format( p1, p2 ) )
        File.write( "{} \n".format( utilizator.find( p1, p2 ) ) )
        calculator.adaugareRaspuns( p1, p2, utilizator.find( p1, p2 ) )

#scriem raspunsurile gasite
    File.write( "\nRaspunsul este: {} {}".format( calculator.raspuns[0] ,
                                                  calculator.raspuns[1] ) )
    n -= 1
