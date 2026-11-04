Toteuttiko agentti metodin top_goal_scorers docstringin mukaisesti ja luokan muun koodin tyyliin?

Kyllä, koodi vastasi sekä docstringia että aikaisemmin kirjoittamaa koodiani


Pitikö agentin selitys Pylint-varoituksesta paikkansa?

Pylint varoituksen selitys oli järkevä


Tekikö agentti toimivan ratkaisun, ja testit?

Itse ratkaisu oli toimiva sekä testit oli koodattu oikein ilman nettiyhteyden hyödyntämistä. Kuitenkin ne oli  sijoitettu väärään paikkaan ja __init__.py tiedosto puuttui, jolloin testejä ei voitu suorittaa. Botti sai tämän korjattua kun kopioin sille materiaalista ohjeet nimeämisen suhteen.


Eroaako testeissä joku siitä miten testejä tehtiin edellisellä viikolla?

Jokaisessa testissä tehdään uudet luokkien instanssit, vaikka tämä ei käsittääkseni tarpeellista
"""
    players = make_players()
    reader = StubReader(players)

    stats = PlayerStats(reader)

"""
(Viime viikolla oli erillinen setUp funktio)

Sen lisäksi testeissä useita assert lausekkeita



Löysikö Pylint agentin koodista virheitä?

Yksi too-many-statements error


Mitä muuta opit?

Opin alustamaan ja asentamaan opencoden
