# AI-generert med Claude Code

# Import henter inn kode fra andre filer eller pakker slik at vi kan bruke den her.
# Flask er rammeverket som gjør Python om til en nettapplikasjon.
# render_template ber Flask finne en HTML-mal i templates/-mappen og sende den til nettleseren.
from flask import Flask, render_template

# Vi importerer kantine-ordboken fra filen kantinedata.py.
from kantinedata import kantine

# Flask(__name__) oppretter selve nettapplikasjonen.
# __name__ forteller Flask hvilken Python-fil den kjører fra, slik at den finner riktige mapper.
app = Flask(__name__)


# En rute (route) kobler en nettadresse til en Python-funksjon.
# @app.route("/") betyr at denne funksjonen kjøres når noen åpner forsiden ("/").
@app.route("/")
def index():
    # render_template laster inn HTML-malen "index.html" fra templates/-mappen.
    # kantine=kantine sender ordboken vår til malen, slik at HTML-en kan bruke dataene.
    return render_template("index.html", kantine=kantine)
