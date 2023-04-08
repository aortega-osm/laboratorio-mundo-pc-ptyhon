from Monitor import Monitor
from raton import Raton
from Teclado import Teclado

class Computadora:
    contador_computadora=0
    def __init__(self,nombre,monitor,teclado,raton):
        Computadora.contador_computadora +=1
        self._id_computadora=Computadora.contador_computadora
        self._nombre=nombre
        self._monitor=monitor
        self._teclado=teclado
        self._raton=raton

    def __str__(self):
        return f"""
Id:{self._id_computadora}
Nombre:{self._nombre}, 
Monitor:{self._monitor}
Teclado:{self._teclado}
Raton:{self._raton}
"""

