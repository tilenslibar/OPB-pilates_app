from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from datetime import datetime

# V tej datoteki definiramo vse podatkovne modele, ki jih bomo uporabljali v aplikaciji
# Pazi na vrstni red anotacij razredov!


@dataclass_json
@dataclass
class vaja:
    id: int = field(default=0)
    ime: str = field(default="")
    opis: str = field(default="")
    tip: str = field(default="")
    link: str = field(default="")  # Dodatno si shranimo še link do repozitorija z vajo
    user_id: int = field(default=0)

@dataclass_json
@dataclass
class vajaDto:
    ime: str = field(default="")
    opis: str = field(default="")
    tip: str = field(default="")
    link: str = field(default="")
    username: str = field(default="")

@dataclass_json
@dataclass
class trening:
    id: int = field(default=0)
    ime: str = field(default="")

@dataclass_json
@dataclass
class treningDto:
    id: int = field(default=0)
    ime: str = field(default="")
    vaje: list = field(default_factory=list)  # Seznam vaj, ki so del treninga


# OD TU NAPREJ JE SKOPIRANO IZ GITHUB REPOZITORIJA OPB_STRUKTURA_PROJEKTA

@dataclass_json
@dataclass
class transakcija:
    id : int = field(default=0)  # Za vsako polje povemo tip in privzeto vrednost
    racun : int = field(default=0)
    cas: datetime=field(default=datetime.now()) 
    znesek: float=field(default=0)
    opis: str=field(default="")


# Za posamezno entiteto ponavadi ustvarimo tudi tako imenovan
# DTO (database transfer object) objekt. To izhaja predvsem iz tega,
# da v sami aplikaciji ponavadi želimo prikazati podatke drugače kot so v bazi.
# Dodatno bi recimo želeli narediti kakšen join in vzeti podatek oziroma stolpec iz druge tabele
@dataclass_json
@dataclass
class transakcijaDto:
    id : int = field(default=0)
    emso : str = field(default="")  # dodatno si shranimo še emso osebe
    oseba : str = field(default="")  # dodatno si shranimo še ime osebe (kot ime + priimek)
    racun : int = field(default=0)
    cas: datetime=field(default=datetime.now()) 
    znesek: float=field(default=0)
    opis: str=field(default="")


@dataclass_json
@dataclass
class oseba:
    emso : str = field(default="")  # Za vsako polje povemo tip in privzeto vrednost
    ime : str = field(default="")
    priimek : str = field(default="")
    rojstvo: str = field(default="") 
    ulica : str = field(default="")
    posta : int = field(default=0)

@dataclass_json
@dataclass
class racun:    
    stevilka : int = field(default=0)
    lastnik : str = field(default="")



@dataclass_json
@dataclass
class osebaDto:    
    emso : str = field(default="")  
    ime : str = field(default="")
    priimek : str = field(default="")
    rojstvo: str = field(default="") 
    ulica : str = field(default="")
    posta : int = field(default=0)
    stevilka_racuna: int = field(default=0)

    


@dataclass_json
@dataclass
class Uporabnik:
    id: int = field(default=0)
    username: str = field(default="")
    role: str = field(default="")
    password_hash: str = field(default="")
    last_login: str = field(default="")

@dataclass
class UporabnikDto:
    username: str = field(default="")
    role: str = field(default="")
    last_login: str = field(default="")
