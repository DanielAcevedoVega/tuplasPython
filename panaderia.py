menu = dict({
    "Pan": {
    "Producto":list([
        {"nombre": "Pan de trigo", "valor": 2500},
        {"nombre": "Pan de baguette", "valor": 3000},
        {"nombre": "Pan integral", "valor": 2000},
        {"nombre": "Pan de avena", "valor": 2500},
        {"nombre": "Pan de maíz", "valor": 4000},
        {"nombre": "Pan de nueces", "valor": 5000},
        {"nombre": "Pan de pasas", "valor": 4500},
        {"nombre": "Pan de queso", "valor": 3000},
        {"nombre": "Pan de yuca", "valor": 3800},
        {"nombre": "Pan tajado", "valor": 1500}
        ]),
          "Promociones":list([
              {"nombre": "Descuento por cantidad", "cantidadMinima": 5, "descuento": 0.96}
              ])
    },
    "Postres": {
    "Producto": list([
        {"nombre": "Gelatina condensada", "valor": 1700},
        {"nombre": "Croissant", "valor": 2500},
        {"nombre": "Donut", "valor": 2000},
        {"nombre": "Magdalena", "valor": 1500},
        {"nombre": "Hojaldra de chocolate", "valor": 1000},
        {"nombre": "Brazo reina", "valor": 2000},
        {"nombre": "Brownie", "valor": 3600},
        {"nombre": "Torta de chocolate", "valor": 3200},
        {"nombre": "Torta de fresa", "valor": 3200},
        {"nombre": "Torta de frutas", "valor": 3500}
        ]),
            "Promociones":list([
                {"nombre": "Descuento por cantidad", "cantidadMinima": 3, "descuento": 0.93}
                ]) 
        },
    "Galletas": {
    "Producto": list([
        {"nombre": "Galleta de avena", "valor": 1000},
        {"nombre": "Galleta de chocolate", "valor": 1200},
        {"nombre": "Galleta de jengibre", "valor": 1200},
        {"nombre": "Galleta de almendra", "valor": 1500},
        {"nombre": "Galleta de mantequilla", "valor": 1000},
        {"nombre": "Galleta de mani", "valor": 1200},
        {"nombre": "Galleta de avellana", "valor": 1300},
        {"nombre": "Galleta de coco", "valor": 1700},
        {"nombre": "Galleta de limón", "valor": 1200},
        {"nombre": "Galleta de vainilla", "valor": 1200}
        ]), 
            "Promociones":list([
                {"nombre": "Descuento por cantidad", "cantidadMinima": 6, "descuento": 0.97}
                ])
        }
})
print("###### Bienvenido a mi panaderia ######")
print("Seleccione la categoria: ")
listaCategoria = list(menu.keys())
for i,val in enumerate(menu.keys()):
    print(f"        {i+1}. {val}")
opcionCategoria = int(input())-1
datosCategoria = menu.get(listaCategoria[opcionCategoria])
productosCategoria = datosCategoria.get("Producto")
promocionCategoria = datosCategoria.get("Promociones")

print(f"Usuario usted selecciono la categoria {listaCategoria[opcionCategoria]} ")

while True:
    n = int(input("Ingrese la cantidad que deseas comprar: "))
    if n >= 1:
        break
productosSeleccionados = []

print("Seleccione el numero del producto: ")
for i,val in enumerate(productosCategoria):
    nombre = val["nombre"]
    valor = val["valor"]
    print(f"        {i+1}. {nombre} con el precio de ${valor}")

for _ in range(n):
    seleccionProducto = int(input())-1
    productoElegido = productosCategoria[seleccionProducto]
    productosSeleccionados.append(productoElegido)

precioTotal = sum(producto["valor"] for producto in productosSeleccionados)

promocionProductos = list()
for promocion in promocionCategoria:
        cantidadMinima = promocion["cantidadMinima"]
        descuento = promocion["descuento"]
        if n >= cantidadMinima:
            print(f"Tienes un descuento por la cantidad de productos comprado que es {n}")
            precioTotal *= descuento
        
print("Productos seleccionados: ")
for producto in productosSeleccionados: 
    print(f'{producto["nombre"]} - ${producto["valor"]}')

print(f"Precio total:  ${precioTotal}")

dinero = int(input("Ingrese la cantidad de dinero disponible: "))
vueltos = dinero - precioTotal 
if dinero >= precioTotal:
    print(f"Usuario sus vueltos son ${vueltos}")
else:
    print(f"Usuario le falta un total de ${-vueltos} ")

