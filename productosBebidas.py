productos = tuple((
    "Coca-Cola", 
    "Pepsi", 
    "Sprite", 
    "Fanta", 
    "7UP", 
    "Mountain Dew", 
    "Dr Pepper", 
    "Schweppes", 
    "Mirinda", 
    "Lift"))
precios = tuple((
    4500, 
    3750, 
    3000, 
    3600, 
    5250, 
    6000, 
    5400, 
    3900, 
    4200, 
    4800))
print("Menu de seleccion de productos")

for i,val in enumerate(productos): 
    print(f"""      {i}. {val} ${precios[i]}""")
opcion = int(input())

print(f"Usuario usted seleccion el producto {productos[opcion]} con un valor de ${precios[opcion]}")
dinero = int(input("Ingrese la cantidad de dinero disponible: "))

vueltos = dinero - precios[opcion] 
if dinero >= precios[opcion]:
    print(f"Usuario usted compro el prodcuto {productos[opcion]} con un valor de ${precios[opcion]}, sus vueltos son ${vueltos}")
else:
    print(f"Usuario el producto que desea comprar {productos[opcion]} con un valor de ${precios[opcion]}, le falta un total de ${-vueltos} ")

#Hacer un menu y tiene que dar una categoria despues tiene que mostar los productos y 
#luego que el usario elija cuantos quiere 3 categorias 10 productos y 2 promociones por categoria
#Hacerlo con diccionarios 