# Harjoitus, jossa tehdään luokkia ja olioita

# MODULIEN JA KIRJASTOJEN LATAUKSET

# LUOKKIEN MÄÄRITTELY

# Määritellään lainaajaluokka, joka ei peri mitään
class Lainaaja:

    # Uuden olion luonti (constructor) -> olion luontimetodi
    def __init__(self, opiskelijanumero, etunimi, sukunimi):

        # Ominaisuudet: self viittaa tulevaan olioon, jonka nimi ei vielä tiedossa
        self.opiskelijanumero = opiskelijanumero
        self.etunimi = etunimi
        self.sukunimi = sukunimi

    # Olion metodit -> mitä olio osaa tehdä
    def tulosta_opiskelijanumero(self):
         print('opiskelijanumero on',self.opiskelijanumero)

    def tulosta_kaikki_tiedot(self):
         print('Opiskelijanumero:',self.opiskelijanumero,'\n' 'Etunim:', self.etunimi, '\n' 'Sukunimi:', self.sukunimi)
   



# VARSINAINEN OHJELMA

# Luodaan lainaaja-olio Lainaaja-luokasta

lainaaja1 = Lainaaja(123456, 'Mauri', 'Hutikka')

# Testataan lainaaja1-oliota
print('Lainaaja1 on',lainaaja1.etunimi, lainaaja1.sukunimi)

lainaaja1.tulosta_opiskelijanumero()
lainaaja1.tulosta_kaikki_tiedot()

        
        