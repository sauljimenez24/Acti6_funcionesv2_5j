print("funciones vercion 2")
print("Saul Jimenez")
# zona de listas tuplas set y diccionario
crush=["1- sofia yañez ", "2 Alisha Lehmann", "scarlet johansson"]
ropamarcas={"Adidas" ,"Nike" , "Gucci"}
marcadecarros=(" MUstang", "Corvette", "Audi")
musica = {
  "Santa ": "raw alejandro",
  "lansamiento ": " 24 abril",
  "año ": 2025
}


# zona de funciones
def verlista(amores):
    for unamor in amores:
        print(unamor)

# tuplas
def vertupla(ropa):
    for unaropa in ropa:
        print(unaropa)

# sets
def versets(car):
    for unacar in car:
        print(unacar)

# Diccionario
def verdiccionario(m):
    for unam in m:
        print(unam)

print("imprime crosh de una lista")
verlista(crush)
print("imprime ropa de una tupla")
vertupla(ropamarcas)
print("imprime carros de una sets")
versets(marcadecarros)
print("imprime crosh de una diccionario")
verdiccionario(musica)

