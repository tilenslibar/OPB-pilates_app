import psycopg2, psycopg2.extensions, psycopg2.extras
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE) # se znebimo problemov s šumniki
import Data.auth_public as auth
import datetime
import os

from Data.models import transakcija, oseba, osebaDto, racun, transakcijaDto, Uporabnik, vaja, vajaDto, treningDto, trening
from typing import List

# Preberemo port za bazo iz okoljskih spremenljivk
DB_PORT = os.environ.get('POSTGRES_PORT', 5432)

## V tej datoteki bomo implementirali razred Repo, ki bo vseboval metode za delo z bazo.

class Repo:
    def __init__(self):
        # Ko ustvarimo novo instanco definiramo objekt za povezavo in cursor
        self.conn = psycopg2.connect(database=auth.db, host=auth.host, user=auth.user, password=auth.password, port=DB_PORT)
        self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        print("Povezava z bazo vzpostavljena")

    def dobi_vaje(self):
        self.cur.execute("""
            SELECT v.ime, v.opis, v.tip, v.link, u.username
            FROM vaje v
            LEFT JOIN uporabniki u
            ON v.user_id = u.id
        """)

        vaje = [vajaDto.from_dict(v) for v in self.cur.fetchall()]
        return vaje

    def dodaj_vajo(self, v: vaja):
        print("Dodajam vajo:", v.ime)
        
        self.cur.execute("""
            INSERT INTO vaje(ime, opis, tip, link, user_id)
            VALUES (%s, %s, %s, %s, %s)
        """, (v.ime, v.opis, v.tip, v.link, v.user_id))
        self.conn.commit()

    def dobi_treninge(self):
        self.cur.execute("""
            SELECT t.id AS trening_id, t.ime AS trening_ime, v.ime AS ime, v.opis AS opis, v.tip AS tip, v.link AS link
            FROM treningi t
            LEFT JOIN trening_vaja tv ON t.id = tv.trening_id
            LEFT JOIN vaje v ON tv.vaja_id = v.id
            ORDER BY t.id;
        """)

        treningi = self.cur.fetchall()

        print("TRENINGI", treningi)
        print("TRENINGI END")

        treningi_dto = {}
        for row in treningi:
            id = row['trening_id']
            if id not in treningi_dto:
                if row['ime'] is not None:
                    treningi_dto[id] = treningDto(id=row['trening_id'], ime=row['trening_ime'], vaje=[vaja.from_dict(row)])
                else:
                    treningi_dto[id] = treningDto(id=row['trening_id'], ime=row['trening_ime'], vaje=[])
            else:
                treningi_dto[id].vaje.append(vaja.from_dict(row))

        return treningi_dto.values()

    def dodaj_vajo_treningu(self, trening_id: int, vaja_ime: str):
        # Najprej pridobimo ID vaje po imenu
        self.cur.execute("""
            SELECT id FROM vaje WHERE ime = %s
        """, (vaja_ime,))
        
        vaja_id = self.cur.fetchone()[0]

        # Sedaj dodamo povezavo med treningom in vajo
        self.cur.execute("""
            INSERT INTO trening_vaja(trening_id, vaja_id)
            VALUES (%s, %s)
        """, (trening_id, vaja_id))
        
        self.conn.commit()

    def dodaj_trening(self, ime: str):
        print("Dodajam trening:", ime)
        
        self.cur.execute("""
            INSERT INTO treningi(ime)
            VALUES (%s)
        """, (ime,))
        self.conn.commit()

    # OD TUKAJ NAPREJ JE SKOPIRANO IZ GITHUB REPOZITORIJA OPB_STRUKTURA_PROJEKTA
    
    def dobi_transakcije(self) -> List[transakcija]:
        self.cur.execute("""
            SELECT id, racun, cas, znesek, opis
            FROM transakcija
            Order by cas desc
        """)
        
        # rezultate querya pretovrimo v python seznam objektov (transkacij)
        transakcije = [transakcija.from_dict(t) for t in self.cur.fetchall()]
        return transakcije
    
    def dobi_transakcijo(self, id) -> transakcija:
         self.cur.execute("""
            SELECT id, racun, cas, znesek, opis
            FROM transakcija
            Where id = %s
        """, (id,))
         
         t = transakcija.from_dict(self.cur.fetchone())
         return t

    
    def dobi_transakcije_dto(self) -> List[transakcijaDto]:
        self.cur.execute("""
            SELECT t.id, o.emso, o.ime || ' ' || o.priimek as oseba, t.racun, t.cas, t.znesek, t.opis
            FROM transakcija t 
            left join racun r on t.racun = r.stevilka
            left join oseba o on o.emso = r.lastnik
            Order by t.cas desc
        """)

        transakcije = [transakcijaDto.from_dict(t) for t in self.cur.fetchall()]
        return transakcije
    
    def dobi_osebe(self) -> List[oseba]:
        self.cur.execute("""
            SELECT emso, ime, priimek, rojstvo, ulica, posta
            FROM oseba
        """)
        
        # rezultate querya pretovrimo v python seznam objektov (transkacij)
       # tt = [t for t in self.cur.fetchall()]
        osebe = [oseba.from_dict(t) for t in self.cur.fetchall()]
        return osebe
    
    def dobi_osebo(self, emso: str) -> oseba:
        self.cur.execute("""
            SELECT emso, ime, priimek, rojstvo, ulica, posta
            FROM oseba
            WHERE emso = %s
        """, (emso,))
         
        o = oseba.from_dict(self.cur.fetchone())
        return oseba

    def dobi_osebe_dto(self) -> List[osebaDto]:
        self.cur.execute("""
            SELECT emso, ime, priimek, rojstvo, ulica, posta, racun.stevilka as stevilka_racuna
            FROM oseba
            left join racun on racun.lastnik = oseba.emso 
                         
        """)
        
        # rezultate querya pretovrimo v python seznam objektov (transkacij)
       # tt = [t for t in self.cur.fetchall()]
        osebe = [osebaDto.from_dict(t) for t in self.cur.fetchall()]
        return osebe
    
    def dobi_racun(self, emso: str) -> racun:
        self.cur.execute("""
            SELECT stevilka, lastnik
            FROM racun
            WHERE lastnik = %s
        """, (emso,))
         
        r = racun.from_dict(self.cur.fetchone())
        return r
    
    def dobi_transakcije_oseba(self, emso : str) -> List[transakcija]:
        racun = self.dobi_racun(emso)
        self.cur.execute("""
            SELECT id, racun, cas, znesek, opis
            FROM transakcija
            WHERE racun = %s
        """, (racun.stevilka,))
        
        # rezultate querya pretovrimo v python seznam objektov (transkacij)
        transakcije = [transakcija.from_dict(t) for t in self.cur.fetchall()]
        return transakcije
    
    def dodaj_transakcijo(self, t : transakcija):
        self.cur.execute("""
            INSERT into transakcija(znesek, racun, cas, opis)
            VALUES (%s, %s, %s, %s)
            """, (t.znesek, t.racun, t.cas, t.opis))
        self.conn.commit()

    def posodobi_transakcijo(self, t : transakcija):
        self.cur.execute("""
            Update transakcija set znesek = %s, racun = %s, cas=%s, opis = %s where id = %s
            """, (t.znesek, t.racun, t.cas, t.opis, t.id))
        self.conn.commit()

    def dodaj_uporabnika(self, uporabnik: Uporabnik):
        print("dodajam uporabnika", uporabnik.username)
        
        self.cur.execute("""
            INSERT into uporabniki(username, role, password_hash, last_login)
            VALUES (%s, %s, %s, %s)
            """, (uporabnik.username,uporabnik.role, uporabnik.password_hash, uporabnik.last_login))
        self.conn.commit()


    def dobi_uporabnika(self, username:str) -> Uporabnik:
        self.cur.execute("""
            SELECT id, username, role, password_hash, last_login
            FROM uporabniki
            WHERE username = %s
        """, (username,))
         
        u = Uporabnik.from_dict(self.cur.fetchone())
        return u
    
    def dobi_uporabnike(self):
        self.cur.execute("""
            SELECT username, role, password_hash, last_login
            FROM uporabniki
        """)
         
        uporabniki = [Uporabnik.from_dict(u) for u in self.cur.fetchall()]
        return uporabniki
    
    def posodobi_uporabnika(self, uporabnik: Uporabnik):
        self.cur.execute("""
            Update uporabniki set last_login = %s where username = %s
            """, (uporabnik.last_login,uporabnik.username))
        self.conn.commit()

    def izbrisi_vajo(self, ime: str):
        self.cur.execute("""
            DELETE FROM vaje WHERE ime = %s
        """, (ime,))
        self.conn.commit()

    def dobi_vajo(self, ime: str):
        self.cur.execute("""
            SELECT * FROM vaje WHERE ime = %s
        """, (ime,))
        v = self.cur.fetchone()
        if v:
            return vaja.from_dict(v)
        return None

    def posodobi_vajo(self, staro_ime: str, novo_ime: str, opis: str, tip: str, link: str):
        self.cur.execute("""
            UPDATE vaje SET ime=%s, opis=%s, tip=%s, link=%s WHERE ime=%s
        """, (novo_ime, opis, tip, link, staro_ime))
        self.conn.commit()

    def izbrisi_trening(self, trening_id: int):
        self.cur.execute("""
            DELETE FROM treningi WHERE id = %s
        """, (trening_id,))
        self.conn.commit()

    def dobi_trening(self, trening_id: int):
        self.cur.execute("""
            SELECT * FROM treningi WHERE id = %s
        """, (trening_id,))
        t = self.cur.fetchone()
        if t:
            return trening.from_dict(t)
        return None

    def posodobi_trening(self, trening_id: int, novo_ime: str):
        self.cur.execute("""
            UPDATE treningi SET ime=%s WHERE id=%s
        """, (novo_ime, trening_id))
        self.conn.commit()

    def izbrisi_vajo_iz_treninga(self, trening_id: int, vaja_ime: str):
        self.cur.execute("""
            SELECT id FROM vaje WHERE ime = %s
        """, (vaja_ime,))
        vaja_id = self.cur.fetchone()[0]
        self.cur.execute("""
            DELETE FROM trening_vaja WHERE trening_id = %s AND vaja_id = %s
        """, (trening_id, vaja_id))
        self.conn.commit()
