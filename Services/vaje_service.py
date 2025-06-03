from Data.repository import Repo
from Data.models import vaja

# class TransakcijeService:
#     def __init__(self) -> None:
#         # Potrebovali bomo instanco repozitorija. Po drugi strani bi tako instanco 
#         # lahko dobili tudi kot input v konstrukturju.
#         self.repo = Repo()

#     def dobi_osebe(self) -> List[oseba]:
#         return self.repo.dobi_osebe()
    
#     def dobi_osebe_dto(self) -> List[osebaDto]:
#         return self.repo.dobi_osebe_dto()
    
#     def dobi_transakcije(self) -> List[transakcija]:
#         return self.repo.dobi_transakcije()
    
#     def dobi_transakcijo(self, id) -> transakcija:
#         return self.repo.dobi_transakcijo(id)
    
#     def dobi_transakcije_dto(self) -> List[transakcijaDto]:
#         return self.repo.dobi_transakcije_dto()


class VajeService:
    def __init__(self) -> None:
        # Potrebovali bomo instanco repozitorija. Po drugi strani bi tako instanco 
        # lahko dobili tudi kot input v konstrukturju.
        self.repo = Repo()

    def dobi_vaje(self):
        return self.repo.dobi_vaje()
    
    
    def dodaj_vajo(self, ime: str, opis: str, tip: str):
        v = vaja(ime=ime, opis=opis, tip=tip)
        
        return self.repo.dodaj_vajo(v)