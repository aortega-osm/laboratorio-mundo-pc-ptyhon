from DispositivoEntrada import DispositivoEntrada
class Raton (DispositivoEntrada):
    contador = 0
    def __init__(self,marca,tipo_entrada):
        Raton.contador += 1
        self._id_raton=Raton.contador
        super().__init__(marca,tipo_entrada)

    def __str__(self):
        return f"[Id raton={self._id_raton}],[Marca={self._marca}],[Tipo de entrada={self._tipo_entrada}]"

