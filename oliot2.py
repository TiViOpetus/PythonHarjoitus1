# Harjoitus, jossa tehdään luokkia ja olioita

# MODULIEN JA KIRJASTOJEN LATAUKSET

# LUOKKIEN MÄÄRITTELY

# Määritellään Henkilö-luokka (yliluokka superclass / parent class), joka määrittelee yleiset ominaisuudet

class Henkilo:
    def __init__(self, etunimi, sukunimi, osasto):
        self.etunimi = etunimi
        self.sukunimi = sukunimi
        self.osasto = osasto

# Opiskelija-luokka (aliluokka subclass / child class), perii Henkilö-luokan ominaisuudet
class Opiskelija(Henkilo):
    def __init__(self, etunimi, sukunimi, osasto, opiskelijanumero):
        super().__init__(etunimi, sukunimi, osasto)
        self.opiskelijanumero = opiskelijanumero

# Opettaja-luokka, perii Henkilo-luokan, ominaisuutena työhuone, esim. A228
class Opettaja(Henkilo):
    def __init__(self, etunimi, sukunimi, osasto, tyohuone):
        super().__init__(etunimi, sukunimi, osasto)
        self.tyohuone = tyohuone

# VARSINAINEN OHJELMA

# Luodaan opiskelija-olio

opiskelija1 = Opiskelija('Jakke', 'Jäynä', 'ICT', 123456)

# Testataan oliota
print('Opiskelija', opiskelija1.etunimi, opiskelija1.sukunimi, 'opiskelee', opiskelija1.osasto,'-osastolla')
                
# Luodaan opettaja-olio
opettaja1 = Opettaja('Mari', 'Lounavaara', 'ICT', 'A228') 

# Testataan opettajaa
print(opettaja1.etunimi, 'työskentelee huoneessa',opettaja1.tyohuone)