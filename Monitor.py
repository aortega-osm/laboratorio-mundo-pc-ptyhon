class Monitor:
    contador_monitor =0
    def __init__(self,marca,tamaño):
        Monitor.contador_monitor +=1
        self._id_monitor=Monitor.contador_monitor
        self._marca=marca
        self._tamaño=tamaño

    def __str__(self):
        return f"[Id monitor:{self._id_monitor}],[Marca:{self._marca}],[Tamaño:{self._tamaño}]"

