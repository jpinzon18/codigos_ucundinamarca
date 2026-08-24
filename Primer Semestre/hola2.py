def aplicar_descuento(precio, porcentaje=0.10):
    return precio * (1 - porcentaje)


precios_originales = [100.0, 250.0, 500.0, 80.0]


precios_con_descuento = list(
    map(lambda p: aplicar_descuento(p, 0.15), precios_originales)
)

print(f"Lista original (sin cambios): {precios_originales}")
print(f"Nueva lista con descuento:   {precios_con_descuento}")