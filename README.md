# Nettside for Akademiets skolekantine

Dette prosjektet skal lages med Flask, HTML og CSS.

Nettsiden skal inneholde:
- En hjemmeside med kantinas navn og en kort beskrivelse.
- Ukens meny med varmretter fra mandag til fredag.
- Faste varer med navn, priser og bilder.
- Kontaktinformasjon til kantina.

## Kilder

- Prosjektbeskrivelsen fra skolen: brukt til å finne kravene til nettsiden.

## Bruk av kunstig intelligens

### Claude Code (Anthropic)

Følgende filer og deler er laget med Claude Code:

- `kantinedata.py` – heile filen, inkludert ordboken med kantinas navn og beskrivelse.
- `app.py` – heile filen, inkludert Flask-oppsett, rute og render_template-kall.
- `templates/base.html` – heile filen, inkludert HTML-struktur, navigasjon, content-blokk og footer.
- `templates/index.html` – heile filen, inkludert arv fra base.html og visning av kantinadata.