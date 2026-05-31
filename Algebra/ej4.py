# valores encontrados al resolver el sistema

x = 48/11
y = 23/11
z = 35/11

print("=== SOLUCIÓN DEL SISTEMA ===")
print("x =", x)
print("y =", y)
print("z =", z)

# determinante calculado manualmente
determinante = 11

print("\nDeterminante:")
print(determinante)

print("\nVerificación de las ecuaciones:")

ecuacion1 = 2*x + y + z
ecuacion2 = x + 3*y + 2*z
ecuacion3 = 3*x + 2*y + 4*z

print("2x + y + z =", ecuacion1)
print("Resultado esperado = 14")

print("\nx + 3y + 2z =", ecuacion2)
print("Resultado esperado = 17")

print("\n3x + 2y + 4z =", ecuacion3)
print("Resultado esperado = 30")

print("\nLa solución satisface las tres ecuaciones.")