print("huevo frito")
print("encender la estufa")
print("colocar el sarten")

colocar = input("-").strip().lower()

if colocar == "aceite":
    print("bien")
elif colocar == "agua":
    print("bien")   

print("¿romper el huevo en el sarten ya lo hiciste (si) o (no)?")    

rompo = input("_").strip().lower()

if rompo == "si":
    print("vamos bien")
elif rompo == "no":
    print("como lo vas a romper")
    print("volver al inicio")
    quit()

else:
    print("elige (si) o (no) para fritarlo") 
    print("volver al inicio")

saco = input("_").strip().lower()

if saco == ("si"):
    print("echale la sal")  
    print("buen provecho")
elif saco == ("no"):
    print("se le va a quemar") 
else:
    print("eleige (si) o (no) para terminar el huevo")    
    print("volver a empezar")
    quit()    






