print("bienvenidos a la isla del tesoro, tu mision sera encontrar el tesoro")
print("derecha,izquierda o arriba:")
elegir = input("elige una de las direcciones").strip().lower()

if elegir == "derecha":
    print("caiste dentro del agujero")
    print("fin")
    quit()

elif elegir == "izquierda":
    print("nadar o esperar")
    print("nadar")
    print("esperar")

elif elegir == "arriba":
    print("game over")
    print("fin")

else:
     print("debes elegir una opcion")
     print("fin")
     quit()

pare = input().strip() .lower()   

if pare == "nadar":
    print("atacado por una tribu")
    print("fin")
    quit

elif pare == "esperar":
    print("escoge una")
    print("prender fosforo")
    print("seguir")
    print("suicidarse")

elif pare == "suicidarse":
    print("game over")
    print("fin")

else: 
    print("debes elegir una opcion")
    print("fin")
    quit()

opcion = input().strip().lower()

if opcion == "prender fosforo":
    print("la tribu te vio y ahora va a asesinarte")
    print("fin")
    quit()

elif opcion == "seguir":
    print("escoje un camino")
    print("camino 1")
    print("camino 2")
    print("camino misterioso")

else:
    print("debes elegir una opcion")
    print("fin")
    quit()

puerta = input().strip().lower()

if puerta == "camino 1":
    print("devorado por bestias")
    print("game over")
    quit()

elif puerta == "camino misterioso":
    print("eres quemado")
    print("game over")
    quit()

elif puerta == "camino 2":
      print("felicidades")
      quit()

else:
    print("debes elgir una opcion")    
    print("game over") 
    quit()

 
















