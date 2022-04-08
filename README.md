# Lukuvinkki

[![CI](https://github.com/PaulusParssinen/ohtu-miniprojekti/actions/workflows/ci.yml/badge.svg)](https://github.com/PaulusParssinen/ohtu-miniprojekti/actions/workflows/ci.yml)


## Alustus ja ohjelman suoritus


Asenna riippuvuudet komennolla:

```
poetry install
```

Käynnistä sovellus seuraavalla komennolla:

```
poetry run invoke start
```

Voit alustaa tietokannan halutessasi uudelleen komennolla:

```
poetry run invoke reset-database
```

## Ohjelman testaus

Yksikkötestit voi suorittaa komennolla:

```
poetry run invoke test
```

Robot Frameworkilla toteutetut integraatio-testit voi suorittaa komennolla:

```
poetry run invoke robot
```

Pylint suoritus onnistuu komennolla:

```
poetry run invoke lint

```

Testaavuuskattavuuden suoritus onnistuu seuraavalla komennolla:

```
poetry run invoke coverage-report
```

Testaavuuskattavuusraportti avautuu seilameen myös seuraavalla komennolla:

```
poetry run invoke view-report

```

## Dokumentaatio

[Käyttöohje](https://github.com/PaulusParssinen/ohtu-miniprojekti/blob/master/dokumentaatio/kayttoohje.md)

[Backlog](https://github.com/PaulusParssinen/ohtu-miniprojekti/projects/1)

[Työaikakirjanpito](https://docs.google.com/spreadsheets/d/1A-ZcTPfodWB2oIwpxf0ftId64tXmp-Jd7OyfNQiHnw4/edit#gid=1003565531)

[Definition of done](https://github.com/PaulusParssinen/ohtu-miniprojekti/blob/master/dokumentaatio/definition_of_done.md)



