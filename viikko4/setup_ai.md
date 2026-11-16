Agentti suoritti pyydetyn ensimmäisellä promptilla ja suoritti automaattisesti testit. Testasin myös itse ja toimivat. Agentti kuitenkin pyytämättä poisti kaksi käyttämätöntä importtia:

```
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
```

Testit vaikuttavat kuitenkin toimivan samalla tavalla ilman importteja, joten kenties ne olivat oikeasti turhia. En joutunut tekemään itse mitään. Testien toiminnallisuus ei muuttunut ja koodi on nyt helpompaa lukea.