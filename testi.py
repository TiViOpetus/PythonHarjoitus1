# ENSIMMÄINEN HARJOITUS MUUTTUJAT, NÄPPÄIMISTÖ JA NÄYTTÖ

# Määritellään muuttujat ja kysytään arvot käyttäjältä

first_name = input('Mikä on etunimesi? ')
favourite_place = input('Mikä on suosikkipaikkasi? ')
nickname = input('Mikä on lempinimesi? ')
year_of_birth = input('Minä vuonna olet syntynyt? ')

# Tulostetaan tiedot ruudulle
print(first_name, 'olet syntynyt', year_of_birth)

# Luodaan lista viikonpäivistä
viikonpaivat = ['maanantai', 'tiistai', 'keskiviikko', 'torstai', 'perjantai', 'lauantai', 'sunnuntai']
print('viikon ensimmäinen päivä on', viikonpaivat[0])