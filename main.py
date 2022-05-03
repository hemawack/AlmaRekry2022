# Tuodaan matplotlib.pyplot-kirjasto
import matplotlib.pyplot as plt

# Lisätään kirjastosta löytyvä valmis tyyli grafiikkaan
plt.style.use('ggplot')

# Lisätään datat.
# Datasetit 2 & 3 on toteutettu indeksoimalla (2015 = 100) Tilastokeskuksen aineisto muutamalla klikkauksella excelissä
# ja copypastettamalla saadut luvut tähän. Saman voisi tietysti toteuttaa # myös tyylikkäämmin esim. hakemalla datat
# suoraan csv-tiedostosta ja sitten indeksoimalla datat suoraan pythonissa laskufunktiolla, mutta näin suppealla
# aineistolla ei maksa vaivaa.

# Luodaan vuosiakseli, jota käytetään myöhemmin kaavion x-akselina
data_vuodet = (2015, 2016, 2017, 2018, 2019, 2020)
# Datasetti 1: 112l -- Vanhojen osakeasuntojen hintaindeksi (2015=100) ja kauppojen lukumäärät, vuositasolla, 2015-2021
# Lähde: https://pxweb2.stat.fi:443/PxWeb/sq/4eac1320-9e83-464c-a102-f3be756a1a71
data_asuntojenHinnat = (100, 100.3, 101.9, 102.5, 103.2, 104.7)
# Datasetti 2: 113n -- Asuntokuntien velat ja rakenne suuralueittain, vuoden 2020 rahassa, 2002-2020
# Lähde: https://pxweb2.stat.fi:443/PxWeb/sq/ec34833a-3097-4e4d-9860-bc37c52948a9
data_kokonaisvelkaantuminen = (100.0, 102.2, 104.2, 104.8, 107.0, 110.7)
# Datasetti 3: 12ij -- Kotitalouden tulot asunnon hallintasuhteen mukaan, 1987-2020
# Lähde: https://pxweb2.stat.fi:443/PxWeb/sq/f71e63bc-5fc3-4979-b191-f3ef690e8820
data_tulot = (100, 100.7, 101.5, 102.2, 101.7, 100.3)

# Luodaan kaavio, johon viivat piirretään
fig, kaavio = plt.subplots()

# Piirretään viivat kaavioon
kaavio.plot(data_vuodet, data_asuntojenHinnat, label='Vanhojen osakeasuntojen hintakehitys', marker='o', linewidth='4')
kaavio.plot(data_vuodet, data_kokonaisvelkaantuminen, label='Kotitalouksien velkaantuminen', marker='o', linewidth='4')
kaavio.plot(data_vuodet, data_tulot, label='Omistusasunnossa asuvien kotitalouksien tulot', marker='o', linewidth='4')

# Lisätään kaavioon tarvittavat tekstikentät
plt.title('Asuntojen hinnat ovat nousseet ja kotitaloudet velkaantuneet')
plt.xlabel('Vuosi')
plt.ylabel('Indeksoitu muutos (2015 = 100)')
plt.text(2015.1, 108.1, 'Lähde: Tilastokeskus')

# Lisätään kuvaukset dataseteille
plt.legend()

# Tulostetaan kaavio ruudulle
plt.show()

