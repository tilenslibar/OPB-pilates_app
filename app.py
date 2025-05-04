from bottle import Bottle, run, template

app = Bottle()

# Seznam vaj
vaje = [
    {"ime": "Dvig trupa", "opis": "", "tezavnost": "", "vrsta": "krepitev"},
    {"ime": "Zaklon", "opis": "", "tezavnost": "", "vrsta": "krepitev"},
]

@app.route('/')
def domov():
    return template('domov', naslov="Domača stran", sporocilo="Dobrodošli na domači strani!")

@app.route('/vaje')
def stran_vaje():
    return template('vaje', naslov="Baza vaj", vaje=vaje)

if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True)
