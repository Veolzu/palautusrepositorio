Päätyikö agentti toimivaan ja hyvään ratkaisuun
Miten varmistit, että ratkaisu toimii?
Tekikö agentti testit, ja olivatko ne hyviä?
Oliko koodi selkeää
Opitko jotain uutta agentin tekemää koodia lukiessasi


Agentti päätyi toimivaan ja (vähintäänkin tarpeeksi hyvään) ratkaisuun. Jotain säätöä oli testien pyörittämisessä: agentti oli rakentanut robot testit sen varaan, että ne suoritetaan itselle aikasemmin tuntemattomilla vivuilla, joita ilman testit eivät pyörineet. Tästä kysyessä agentti kuitenkin muutti rakenteen, jotta testit pyörivät normaalilla `uv run robot ...`. Testasin sovellusta sekä agentin tekemillä testeillä sekä "tutkivalla testaamisella" (Exploratory testing): käynnistin sovelluksen ja yritin rikkoa sen. Agentti teki ihan hyvät testit, kaikille ns. "perus" ominaisuuksille (kaikenkaikkiaan 7 robot testiä). Koodi oli suhteellisen selkeää, mutta jouduin kysymään sitä selittämään jotain asioita (Esim. testit hyödynsivät flask kirjaston omaa `test_client()` mikä oli itselle tuntematon). Opin esimerkiksi test_clientista sekä enemmän robot frameworkin testeissä käytettävästä syntaxista:
`${page}=    Create Warehouse    Main storage    100`, jossa muuttujaksi voi tallentaa näin tuloksia muista keywordeista.