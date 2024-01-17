class Fabricante:
    def __init__(self, fabricante) -> None:
        self.fabricante = fabricante
        

class Motor:
    def __init__(self, motor):
        self.motor= motor
        
        

class Carro:
    def __init__(self, carro):
        self.carro = carro
        self._motor = None
        self._fabricante = None
        
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
         self._motor = valor
    
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
         self._fabricante = valor


ford_mustang = Carro('Mustang')
ford = Fabricante("Ford")
ford_mustang.fabricante = ford
v8_turbo = Motor('V8 turbo')
ford_mustang.motor = v8_turbo

print(f'O fabricante {ford.fabricante} produz o "{ford_mustang.carro}" com motorização {v8_turbo.motor}')

m3_coupe= Carro('M3 coupe')
BMW = Fabricante("BMW")
m3_coupe.fabricante = BMW
print()
print(f'O fabricante {BMW.fabricante} produz a "{m3_coupe.carro}" com motorização {v8_turbo.motor}')