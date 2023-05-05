print("ingresa a tu boleta.com")
print("verificar conciertos en bogota:")
print("¿verificar si el concierto es de salsa?")
print("(si)")
print("(no)")

verificar = input("-").strip().lower

if verificar =="si":
    print("buscar silla en platea:")
elif verificar =="no":
    print("aviso:no,hay conciertos disponibles de salsa")

print("verificar el precio")   
print("¿supera los dos millones de pesos?")
print("(no)")
print("(si)")

verificar = input("-").strip().lower

if verificar =="si":
    print("no compra")
elif verificar =="no":
    print("elige el servicio de bebidas")

print("elige el metodo de pago")
print("comprar")
print("fin")
quit








