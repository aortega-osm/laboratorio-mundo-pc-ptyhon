from DispositivoEntrada import DispositivoEntrada
class Teclado (DispositivoEntrada):
    contador_teclados=0
    def __init__(self,marca,tipo_entrada):
       Teclado.contador_teclados +=1
       self._id_teclados=Teclado.contador_teclados
       self._marca=marca
       self._tipo_entrada=tipo_entrada

    def __str__(self):
        return f"[Id:{self._id_teclados}],[Marca:{self._marca}],[Tipo de entrada:{self._tipo_entrada}]"

