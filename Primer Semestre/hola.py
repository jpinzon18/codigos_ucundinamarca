class CuentaBancaria:

    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self._saldo = saldo_inicial 

    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: ${self._saldo}")

    def obtener_saldo(self):
        return self._saldo


mi_cuenta = CuentaBancaria("Juan", 1000)
print(f"Cuenta de {mi_cuenta.titular} creada con ${mi_cuenta.obtener_saldo()}")


mi_cuenta.depositar(500)