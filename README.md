## Ohtu miniprojekti boilerplate

Lue [täältä](https://ohjelmistotuotanto-hy.github.io/flask/) lisää.

## Linkkejä

[Backlog](https://github.com/orgs/valovalovalo/projects/1)
[Definition of Done](https://github.com/valovalovalo/miniprojekti/wiki/Definition-Of-Done)
[Coverageraportti](https://maza.kapsi.fi/miniprojekticoverage/)

## Asentaminen

Vaatimuksena Python >=3.10.0, Poetry ja PostgreSQL-tietokanta.

Konfiguroi PostgreSQL-tietokanta ja täydennä sen tiedot .env -tiedostoon.

Seuraavat komennot asentavat sovelluksen riippuvuudet ja alustaa tietokannan:

```
poetry install
poetry shell
python src/db_helper.py
```

## Käyttäminen

Sovellus käynnistetään seuraavasti:

```
poetry shell
python src/index.py
```

Sovellus löytyy osoitteesta localhost:5001

## Lisenssi
Tämä projekti on lisensoitu CC BY NC
