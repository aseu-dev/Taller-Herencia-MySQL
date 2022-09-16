import re

class Vehiculo:
    def __init__(self, color: str, ruedas: int) -> None:
        self.color = color
        self.ruedas = ruedas
    def getRuedas(self) -> int:
        return self.ruedas
    def getAtributos(self) -> str:
        return f'Es {self.color} y tiene {self.ruedas} ruedas'
    def getVarName(self) -> str:
        objeto = globals()
        varname = f'{[char for char in objeto if objeto[char] is self]}'
        return re.sub(r'[^\w]','',varname)
    
class Coche(Vehiculo):
    def __init__(self, color: str, ruedas: int, velocidad: float, cilindrada: any) -> None:
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def getAtributos(self) -> str:
        return f'Es {self.color} y tiene {self.ruedas} ruedas, tiene una velocidad maxima de {self.velocidad} y una cilindrada de {self.cilindrada}'

class Camioneta(Coche):
    def __init__(self, color: str, ruedas: int, velocidad: float, cilindrada: any, carga: float) -> None:
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga
    def getAtributos(self) -> str:
        return f'Es {self.color} y tiene {self.ruedas} ruedas, tiene una velocidad maxima de {self.velocidad} y una cilindrada de {self.cilindrada} ademas de que permite una carga maxima de {float(self.carga)}Kg'
    
class Bicicleta(Vehiculo):
    def __init__(self, color: str, ruedas: int, tipo: str) -> None:
        super().__init__(color, ruedas)
        self.tipo = tipo
    def getAtributos(self) -> str:
        return f'Es {self.color} y tiene {self.ruedas} ruedas, es un bicicleta {self.tipo}'

class Motocicleta(Bicicleta):
    def __init__(self, color: str, ruedas: int, tipo: str, velocidad: float, cilindrada: any) -> None:
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def getAtributos(self) -> str:
        return f'Es {self.color} y tiene {self.ruedas} ruedas, es una motocicleta {self.tipo}, tiene una velocidad maxima de {float(self.velocidad)}Km/h y una cilindrada de {self.cilindrada}'

def catalogar(vehiculos: list, ruedas: int = None) -> None:
    if ruedas != None:
        count = 0
        lista = []
        for vehiculo in vehiculos:
            if vehiculo.getRuedas() == ruedas:
                count += 1
                lista += [f'La clase del objeto {vehiculo.getVarName()} es {type(vehiculo).__name__}; {vehiculo.getAtributos()}']
        cantidad = f'Se han encontrado {count} vehiculos con {ruedas} ruedas: ' if count else f'Se han encontrado {count} vehiculos con {ruedas} ruedas'
        print(cantidad)
        if count:
            for text in lista:
                print(text)
        return

    for vehiculo in vehiculos:
        print(f'La clase del objeto {vehiculo.getVarName()} es {type(vehiculo).__name__}; {vehiculo.getAtributos()}')
       
vehiculo1 = Vehiculo(
    color = 'Azul',
    ruedas = 4
)
coche1 = Coche(
    color = 'Negro',
    ruedas = 4,
    velocidad = 120.0,
    cilindrada = 20
)
camioneta1 = Camioneta(
    color = 'Blanco',
    ruedas = 4,
    velocidad = 70.0,
    cilindrada = 30,
    carga = 80
)
bicicleta1 = Bicicleta(
    color = 'rojo',
    ruedas = 2,
    tipo = 'urbana'
)
motocicleta1 = Motocicleta(
    color = 'Negro',
    ruedas = 2,
    tipo = 'urbana',
    velocidad = 120,
    cilindrada = 20
)
vehiculos = [vehiculo1, coche1, camioneta1, bicicleta1, motocicleta1]
catalogar(vehiculos, 1)
