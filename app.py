from functools import wraps
from bottle import run, template, request, redirect, response, get, post
from Services.vaje_service import VajeService
from Services.auth_service import AuthService


service = VajeService()
auth = AuthService()


def cookie_required(f):
    """
    Dekorator, ki zahteva veljaven piškotek. Če piškotka ni, uporabnika preusmeri na stran za prijavo.
    """
    @wraps(f)
    def decorated( *args, **kwargs):
        cookie = request.get_cookie("uporabnik")
        print("Cookie:", cookie)
        if cookie:
            return f(*args, **kwargs)
        return template('prijava', naslov="Prijava", sporocilo="Za dostop do strani se morate prijaviti.")
        
    return decorated


@get('/')
@cookie_required
def domov():
    username = request.get_cookie("uporabnik")
    return template('domov', naslov="Domača stran", username=username, sporocilo="Dobrodošli na domači strani!")

@get('/vaje')
@cookie_required
def stran_vaje():
    vaje = service.dobi_vaje()
    return template('vaje', naslov="Baza vaj", vaje=vaje)

@post('/dodaj')
def dodaj_vajo():
    ime = request.forms.get('ime')
    opis = request.forms.get('opis')
    tip = request.forms.get('tip')
    
    service.dodaj_vajo(ime, opis, tip)
    redirect('/vaje')

@post('/prijava')
def prijava():
    """
    Prijavi uporabnika v aplikacijo. Če je prijava uspešna, ustvari piškotke o uporabniku in njegovi roli.
    Drugače sporoči, da je prijava neuspešna.
    """
    username = request.forms.get('username')
    password = request.forms.get('password')

    print("Username:", username)
    print("Password:", password)

    if not auth.obstaja_uporabnik(username):
        return template("prijava", naslov="Prijava", sporocilo="Uporabnik s tem imenom ne obstaja")

    prijava = auth.prijavi_uporabnika(username, password)
    if prijava:
        response.set_cookie("uporabnik", username)
        response.set_cookie("rola", prijava.role)
        
        # redirect v večino primerov izgleda ne deluje
        redirect('/')

        # Uporabimo kar template, kot v sami "index" funkciji

        # transakcije = service.dobi_transakcije()        
        # return template('transakcije.html', transakcije = transakcije)
        
    else:
        return template("prijava", naslov="Prijava", sporocilo="Neuspešna prijava. Napačno geslo ali uporabniško ime.")

@get('/odjava')
def odjava():
    response.delete_cookie("uporabnik")
    response.delete_cookie("rola")
    redirect('/')

@get('/ustvari_racun')
def ustvari_racun():
    return template('ustvari_racun', naslov="Ustvari račun", sporocilo="Vnesite podatke za ustvarjanje računa.")

@post('/ustvari_racun')
def ustvari_racun_post():
    username = request.forms.get('username')
    password = request.forms.get('password')

    if auth.obstaja_uporabnik(username):
        return template('ustvari_racun', naslov="Ustvari račun", sporocilo="Uporabnik s tem imenom že obstaja.")
    
    auth.dodaj_uporabnika(username, "uporabnik", password)
    return template('prijava', naslov="Prijava", sporocilo="Uspešno ste ustvarili račun. Sedaj se lahko prijavite.")

@get('/uporabniki')
@cookie_required
def uporabniki():
    uporabniki = auth.repo.dobi_uporabnike()
    print("Uporabniki:", uporabniki)
    return template('uporabniki', naslov="Uporabniki", uporabniki=uporabniki)


if __name__ == '__main__':
    # Morda lahko damo ta app stran
    run(host='localhost', port=8080, debug=True)
