from Computadora import Computadora
from Monitor import Monitor
from Orden import Orden
from Teclado import Teclado
from raton import Raton

Monitor1=Monitor("LG","USB")
Teclado1=Teclado("LG",12)
Raton1=Raton("LG","usb")
Computadora1=Computadora("Acer Aspire 3",Monitor1,Teclado1,Raton1)

Monitor2=Monitor("Acer",30)
Teclado2=Teclado("LG","USB")
Raton2=Raton("LG","USB")
Computadora2= Computadora("Apple",Monitor2,Teclado2,Raton2)

teclado3=Teclado("Gamer","Bluetooth")
raton3=Raton("Gamer","Bluetooth")
monitor3=Monitor("Gamer",34)
Computadora3=Computadora("Samsumg",teclado3,raton3,monitor3)

listaComputadoras1=(Computadora1,Computadora2)
listaComputadoras2=(Computadora2,Computadora3)
orden1=Orden(listaComputadoras1)
orden2=Orden(listaComputadoras2)

print(orden1)
print(orden2)
