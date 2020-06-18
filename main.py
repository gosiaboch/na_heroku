from flask import Flask, render_template
import datetime

app = Flask(__name__) #dzięki temu dalej nie musimy pisać Flask tylko zmieniamy nazwę na app

#pierwszy kontroler/handler www.mojastrona.pl @ to adnotacja app nazwa aplikacji route gdy właczy to co zapisane w nawiasie to urochumi się funkcja ktora jest nizej

#www.mojastrona.pl/
@app.route("/")
def index():
    tekst = "Witaj użytkowniku!!!"
    aktualna_data = datetime.datetime.now()
    imiona = ["Adam", "Rafał", "Monika", "Ewa"]

    return render_template("index.html", text = tekst, data = aktualna_data, tablica = imiona)

@app.route("/about")
def about():
    return render_template("about.html")

#Jinja2

if __name__ == "__main__":
    app.run()