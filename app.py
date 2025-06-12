from functools import wraps
from bottle import run, template, request, redirect, response, get, post, static_file
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
@cookie_required
def dodaj_vajo():
    ime = request.forms.get('ime')
    opis = request.forms.get('opis')
    tip = request.forms.get('tip')
    link = request.forms.get('link')
    username = request.get_cookie("uporabnik")

    user = auth.repo.dobi_uporabnika(username)
    # print("Uporabnik:", user)

    service.dodaj_vajo(ime, opis, tip, link, user.id)
    redirect('/vaje')

@post('/prijava')
def prijava():
    """
    Prijavi uporabnika v aplikacijo. Če je prijava uspešna, ustvari piškotke o uporabniku in njegovi roli.
    Drugače sporoči, da je prijava neuspešna.
    """
    username = request.forms.get('username')
    password = request.forms.get('password')

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


@get('/treningi')
@cookie_required
def treningi():
    treningi_dto = service.dobi_treninge()
    print("Treningi:", treningi_dto)
    vaje = service.dobi_vaje()

    return template('treningi', naslov="Treningi", treningi=treningi_dto, vse_vaje=vaje)

@post('/dodaj_vajo_treningu/<trening_id:int>')
@cookie_required
def dodaj_vajo_treningu(trening_id):
    vaja_ime = request.forms.get('vaja_ime')
    print("Dodajam vajo treningu", trening_id, vaja_ime)

    service.dodaj_vajo_treningu(trening_id, vaja_ime)
    redirect('/treningi')

@post('/dodaj_trening')
@cookie_required
def dodaj_trening():
    ime = request.forms.get('ime')
    print("Dodajam trening:", ime)

    service.repo.dodaj_trening(ime)
    redirect('/treningi')

@post('/izbrisi_vajo')
@cookie_required
def izbrisi_vajo():
    ime = request.forms.get('ime')
    service.izbrisi_vajo(ime)
    redirect('/vaje')

@get('/uredi_vajo')
@cookie_required
def uredi_vajo_get():
    ime = request.query.get('ime')
    vaja = service.dobi_vajo(ime)
    return template('uredi_vajo', vaja=vaja)

@post('/uredi_vajo')
@cookie_required
def uredi_vajo_post():
    staro_ime = request.forms.get('staro_ime')
    novo_ime = request.forms.get('ime')
    opis = request.forms.get('opis')
    tip = request.forms.get('tip')
    link = request.forms.get('link')
    service.posodobi_vajo(staro_ime, novo_ime, opis, tip, link)
    redirect('/vaje')

@post('/izbrisi_trening')
@cookie_required
def izbrisi_trening():
    trening_id = request.forms.get('trening_id')
    service.izbrisi_trening(int(trening_id))
    redirect('/treningi')

@get('/uredi_trening')
@cookie_required
def uredi_trening_get():
    trening_id = request.query.get('trening_id')
    trening = service.dobi_trening(int(trening_id))
    return template('uredi_trening', trening=trening)

@post('/uredi_trening')
@cookie_required
def uredi_trening_post():
    trening_id = request.forms.get('trening_id')
    novo_ime = request.forms.get('ime')
    service.posodobi_trening(int(trening_id), novo_ime)
    redirect('/treningi')

@post('/izbrisi_vajo_iz_treninga')
@cookie_required
def izbrisi_vajo_iz_treninga():
    trening_id = request.forms.get('trening_id')
    vaja_ime = request.forms.get('vaja_ime')
    service.izbrisi_vajo_iz_treninga(int(trening_id), vaja_ime)
    redirect('/treningi')

@get('/views/<filename:path>')
def serve_static(filename):
    return static_file(filename, root='./views')


if __name__ == '__main__':
    # Morda lahko damo ta app stran
    run(host='localhost', port=8080, debug=True)
