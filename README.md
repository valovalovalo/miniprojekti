[![GHA workflow badge](https://github.com/valovalovalo/miniprojekti/workflows/CI/badge.svg)](https://github.com/valovalovalo/miniprojekti/actions)
[![codecov](https://codecov.io/gh/valovalovalo/miniprojekti/graph/badge.svg?token=DIS78IN4YX)](https://codecov.io/gh/valovalovalo/miniprojekti)
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
