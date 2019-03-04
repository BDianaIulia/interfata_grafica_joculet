###modul de implementare al algoritmului in vederea rezolvarii jocului
#Algoritmul implementat foloseste logica Cautarii binare pentru a scoate un timp cat mai bun de cautare.
#Ideea algoritmului incepe prin a interoga fiecare colt pana il gaseste pe cel potrivit( in care primiste ca raspuns 'b' ),
#urmand sa puna intrebari pe margini( pe linia orizontala si pe cea verticala ), la pozitii aflate prin injumatatire.


import math         #modul din care importam functia ceil()




#Clasa ce instantiaza matricea jocului
class Matrice:
    
#Functie de initiere. Parametrii sunt cele 2 lini trasate de jucator si zona in
    #care se afla valori de 'b'
#Zona 1 corespunde colutului din stanga sus, iar urmatoarele zone se parcurg
    #in sensul acelor de ceasornic
#Prima linie e cea orizontala, iar cea de-a doua e verticala
    
    def __init__( self, linie1, linie2, zona ): 
        self.linie1 = linie1
        self.linie2 = linie2
        self.zona = zona

#Functie care retureaza valoarea aflata la pozitia celor 2 indici, in functie
    #de liniile trase si zona aleasa
#Daca zona <= 2, inseamna ca ne aflam in partea de sus a matricii, deci daca primul indice are
        #valoare mai mare decat prima linie, se afla in zona gresita. Altfel, ne aflam in
        #partea de jos a matricii, iar orice prim indice mai mic sau egal ca linia1 duce tot intr-o zona gresita
#Daca zona % 2 == 1, inseamna ca e numar impar, deci ne aflam in partea din stanga a matricii. In acest caz, daca cel
        #de-al doilea indice e mai mare ca si linia2, depaseste zona buna. Altfel, ne aflam in partea dreapta, iar orice
        #valoare mai mica sau egala primeste raspunsul 'a'
#Daca nu a intrat pe nici o ramificatie al if-urilor, inseamna ca zona e buna si putem returna 'b'
    def find( self, pozitie1, pozitie2 ):
        if self.zona <= 2:  
            if pozitie1 > self.linie1:
                return 'a'
        else:
            if pozitie1 <= self.linie1:
                return 'a'

        if self.zona % 2 == 1:
            if pozitie2 > self.linie2:
                return 'a'
        else:
            if pozitie2 <= self.linie2:
                return 'a'

        return 'b'


    

#Clasa cu rolul de a ajuta calculatorul in a-si crea intrebarile. O instanta are rolul de a contoriza o suprafata
    #necunoscuta din matricea joc. Pe parcurs ce se afla din raspunsuri, submatricea se injumatateste pana devine 0( caz in care
    #inseamna ca am cucerit toata matricea joc )
class subMatrice:

#Functie de initializare. Are ca si parametrii cele 4 colturi ale subMatricii. 
    def __init__( self, iMin, jMin, iMax, jMax ):
        self.iMin = iMin
        self.iMax = iMax
        self.jMin = jMin
        self.jMax = jMax

#Functie cu rolul de a returna pozitiile coturilor matricii, in functie de numarul coltului la care se afla
#Daca este mai mic de 2, inseamna ca ne aflam in partea de sus a matricii, deci primul indice e numarul randului minim.
    #Altfel, ne aflam in partea de jos, iar indicele primeste numarul randului maxim.
#Daca numarul coltului este impar, suntem pozitionati in partea din stanga a matricii, deci cel de-al doilea indice
    #primeste coloana minima. Altfel, primeste numarul coloanei maxime( ne aflam in partea din dreapta )
    def colt( self, nrColt ):
        if nrColt <= 2:
            pozitie1 = self.iMin
        else:
            pozitie1 = self.iMax

        if nrColt % 2 == 1 :
            pozitie2 = self.jMin
        else:
            pozitie2 = self.jMax
        return (pozitie1 , pozitie2)


#Functie care returneaza un intreg , care reprezinta pozitia de pe mijloc a liniei submatricii.
    #Functia ceil are scopul de a rotunzi in sus valoarea float a mediei dintre coloana minima si coloana maxima
    def mijloc_linie( self ):
        return int( math.ceil( float( self.jMin + self.jMax ) / 2 ) )
    

#Functie care returneaza un intreg , care reprezinta pozitia de pe mijloc a coloanei submatricii.
    #Functia ceil are scopul de a rotunzi in sus valoarea float a mediei dintre linia minima si linia maxima
    def mijloc_coloana( self ):
        return int( math.ceil( float( self.iMin + self.iMax ) / 2 ) )
    

#Functie de micsorare a ariei de cautare. In functie de raspunsul pe care ni l-a oferit utilizatorul, de zona in care am
    #gasit primul 'b' si pozitia de pe linie aflata cu functia mijloc_linie(), injumatatim submatricea vertical, pentru a
    #ne lua noi segmente de cautare. Acest lucru il facem prin modificarea capetelor submatricii.
#Daca ne aflam in stanga, iar raspunsul e 'a', vrem sa scapam de jumatatea din dreapta pentru ca stim ca are doar 'a'.
    #Daca am gasit 'b', inseamna ca toata partea din stanga contine 'b' si nu ne mai trebuie deocamdata.
#Altfel, daca ne aflam in dreapta, iar raspunsul e 'a', toata partea din stanga nu ne intereseaza( are doar 'a' ).
    #Daca raspunsul e 'b', inseamna ca stim ca partea din dreapta are doar 'b' si o inlaturam.
    def injumatatire_matrice_linie( self, pozitia, zona, raspuns ):
        if zona % 2 == 1 :
            if raspuns == 'a':
                self.jMax = pozitia - 1
            else:
                self.jMin = pozitia + 1

        else:
            if raspuns == 'a':
                self.jMin = pozitia + 1
            else:
                self.jMax = pozitia - 1


#Functie de micsorare a ariei de cautare. In functie de raspunsul pe care ni l-a oferit utilizatorul, de zona in care am
    #gasit primul 'b' si pozitia de pe coloana aflata cu functia mijloc_coloana(), injumatatim submatricea orizontal, pentru a
    #ne lua noi segmente de cautare. Acest lucru il facem prin modificarea capetelor submatricii.
#Daca ne aflam in partea de sus, iar raspunsul e 'a', vrem sa scapam de jumatatea de jos pentru ca stim ca are doar 'a'.
    #Daca am gasit 'b', inseamna ca toata partea din stanga contine 'b' si nu ne mai trebuie deocamdata.
#Altfel, daca ne aflam in partea de jos, iar raspunsul e 'a', toata partea de sus nu ne intereseaza( are doar 'a' ).
    #Daca raspunsul e 'b', inseamna ca stim ca partea de jos are doar 'b' si o inlaturam.
    def injumatatire_matrice_coloana( self, pozitia, zona, raspuns ):
        if zona <= 2 :
            if raspuns == 'a':
                self.iMax = pozitia - 1
            else:
                self.iMin = pozitia + 1

        else:
            if raspuns == 'a':
                self.iMin = pozitia + 1
            else:
                self.iMax = pozitia - 1
            
        

    

#Clasa ce instantiaza logica jucatorului calculator.
class Calculator:

#Functie de initializare. Creaza o lista in care se vor atasa intrebarile puse pe parcursul jocului,
    #numarul de intrebari pe care le pune, contor pentru numarul de "lovituri" corecte, o instanta
    #a clasei subMatice( initial primeste aceeasi dimensiune cu matricea jocului ) , o lista in care se memoreaza
    #numarul coltului(zona cu 'b'), alaturi de pozitia acestuia, si o lista in care se memoreaza cele 2 raspunsuri finale:
    #indicii la care a tras jucatorul cele 2 linii.
    def __init__ (self):
        self.setIntrebari = []                              #lista vida
        self.numarIntrebari = 0
        self.puncteNimerite = 0
        self.sub_matrice = subMatrice( 1, 1, 10, 10 )       #submatrice initiala, cu i si j minime = 1 , iar i si j maxime = 10
        self.colt = [ 0, 0, 0 ]                             #[ nr_colt(zona), i_colj, j_colt ]
        self.raspuns = [ 0 , 0 ]                            #[linie_orizontala, linie_verticala]


#Functie cu rolul de a procesa o noua intrebare( o pozitie din matrice ). La fiecare intrebare procesata se incrementeaza
    #contorul numarului de intrebari puse.
#Daca puncteNimerite = 0( nu s-a aflat inca in ce zona se afla 'b' ), intrebam pozitiile din colturile matricii pana gasim
    #prima varianta corecta. Altfel trecem la pasul urmator.
#Daca nu a fost inca gasita valoarea liniei verticale, intrebam de pozitia din mijlocul liniei submatricei. Altfel trecem la pasul urmator.
#Daca nu a fost inca gasita valoarea liniei orizontale, intrebam de pozitia din mijlocul coloanei submatricei.
    def fabrica_intrebari(self):
        self.numarIntrebari += 1
        
        if self.puncteNimerite == 0:
            (pozitie1, pozitie2) = self.sub_matrice.colt( self.numarIntrebari )
            return (pozitie1, pozitie2)

        if self.raspuns[1] == 0 :
            pozitie1 = self.colt[1]
            pozitie2 = self.sub_matrice.mijloc_linie()
            return (pozitie1, pozitie2)
        
        if self.raspuns[0] == 0 :
            pozitie1 = self.sub_matrice.mijloc_coloana()
            pozitie2 = self.colt[2]
            return (pozitie1, pozitie2)

        

#Functie cu rolul de a adauga in lista de raspunsuri, intrebarea precedenta si de a modifica submatricea.
    #Parametrii reprezinta ceidoi indici ai intrebarii si raspunsul dat de utilizator pentru aceasta pozitie.
#Daca am nimerit 'b', incrementam contorul pentru puncte nimerite si, daca ne aflam la primul pas, cel in care cautam coltul( e prima
    #data cand nimerim ), salvam numarul coltului( adica zona, coincide cu numarul de intrebari puse ) si pozitia acestuia.
#Daca am trecut de pasul cautarii coltului( puncteNimerite > 1 ), incepem sa cautam binar pe marginile matricii.
#Daca inca nu s-a aflat linia verticala, injumatatim domeniul de cautare. Daca ajungem ca submatricea sa aiba stanga mai mare ca dreapta,
    #la pozitia unde e memorata coloana maxima se afla linia verticala trasa.
#Daca inca nu s-a aflat linia orizontala, injumatatim domeniul de cautare. Daca ajungem ca submatricea sa aiba linia de sus mai mare ca linia de jos,
    #la pozitia unde e memorata linia maxima se afla linia orizontal trasa.
    def adaugareRaspuns( self, pozitie1, pozitie2, raspuns ):
        self.setIntrebari.append( ( pozitie1, pozitie2, raspuns ) )
        if raspuns == 'b' :
            if self.puncteNimerite == 0 :
                self.colt[0] = self.numarIntrebari
                ( self.colt[1] , self.colt[2] ) =  self.sub_matrice.colt( self.colt[0] )
                
            self.puncteNimerite += 1

        if self.puncteNimerite >= 1:
            if self.raspuns[0] == 0 and self.raspuns[1] != 0 :          #conditie care se indeplineste abia dupa aflarea pozitiei liniei verticale
                self.sub_matrice.injumatatire_matrice_coloana( pozitie1, self.colt[0], raspuns )

            if( self.sub_matrice.iMin > self.sub_matrice.iMax ):
                self.raspuns[0] = self.sub_matrice.iMax 

            if self.raspuns[1] == 0 :
                self.sub_matrice.injumatatire_matrice_linie( pozitie2, self.colt[0], raspuns )

            if( self.sub_matrice.jMin > self.sub_matrice.jMax ):
                self.raspuns[1] = self.sub_matrice.jMax 
            
