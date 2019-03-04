###modul de generare posibile cazuri pentru joc

import random       #modul din care luam functia randint()


#generam 2 linii random, cu valorile intre 2 si 9
#generam o zona random intre 1 si 4
#returnam cele 3 valori generate
def generator_input():
    linie1 = random.randint( 2, 9 )
    linie2 = random.randint( 2, 9 )
    zona = random.randint( 1, 4 )
    return (linie1, linie2, zona )
