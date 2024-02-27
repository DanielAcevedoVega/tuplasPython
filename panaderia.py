menu = dict({
    "Pan": {
    "Producto":list([
        {"nombre": "Pan de trigo", "valor": 2500},
        {"nombre": "Pan de baguette", "valor": 2500},
        {"nombre": "Pan integral", "valor": 2500},
        {"nombre": "Pan de avena", "valor": 2500},
        {"nombre": "Pan de maíz", "valor": 2500},
        {"nombre": "Pan de nueces", "valor": 2500},
        {"nombre": "Pan de pasas", "valor": 2500},
        {"nombre": "Pan de queso", "valor": 2500},
        {"nombre": "Pan de yuca", "valor": 2500},
        {"nombre": "Pan tajado", "valor": 2500}
        ]),
          "Promociones":list([
              {"codigo":0, "nombre": "Compre 5", "valor": 10000},
              {"codigo":1, "nombre": "Compre 2", "valor": 11000}
              ])
    },
    "Postres": {
    "Producto": list([
        {"nombre": "Gelatina condensada", "valor": 2500},
        {"nombre": "Croissant", "valor": 2500},
        {"nombre": "Donut", "valor": 2500},
        {"nombre": "Magdalena", "valor": 2500},
        {"nombre": "Hojaldra de chocolate", "valor": 2500},
        {"nombre": "Eclair", "valor": 2500},
        {"nombre": "Brownie", "valor": 2500},
        {"nombre": "Torta de chocolate", "valor": 2500},
        {"nombre": "Torta de fresa", "valor": 2500},
        {"nombre": "Torta de frutas", "valor": 2500}
        ]),
            "Promociones":list([
                {"codigo":0, "nombre": "Compre 5", "valor": 10000},
                {"codigo":1, "nombre": "Compre 5", "valor": 10000}
                ]) 
        },
    "Galletas": {
    "Producto": list([
        {"nombre": "Galleta de avena", "valor": 2500},
        {"nombre": "Galleta de chocolate", "valor": 2500},
        {"nombre": "Galleta de jengibre", "valor": 2500},
        {"nombre": "Galleta de almendra", "valor": 2500},
        {"nombre": "Galleta de mantequilla", "valor": 2500},
        {"nombre": "Galleta de cacahuete", "valor": 2500},
        {"nombre": "Galleta de avellana", "valor": 2500},
        {"nombre": "Galleta de coco", "valor": 2500},
        {"nombre": "Galleta de limón", "valor": 2500},
        {"nombre": "Galleta de vainilla", "valor": 2500}
        ]), 
            "Promociones":list([
                {"codigo":0, "nombre": "Compre 5", "valor": 10000},
                {"codigo":1, "nombre": "Compre 5", "valor": 10000}
                ])
        }
})
print("###### Bienvenido a mi panaderia ######")
print("Seleccione la categoria: ")
listaCategoria = list(menu.keys())
for i,val in enumerate(menu.keys()):
    print(f"        {i}. {val}")
opcionCategoria = int(input())
datosCategoria = menu.get(listaCategoria[opcionCategoria])
productosCategoria = datosCategoria["Producto"]
promocionCategoria = datosCategoria["Promociones"]

print(f"Usuario usted selecciono la categoria {listaCategoria[opcionCategoria]} ")

while True:
    n = int(input("Ingrese la cantidad que deseas comprar: "))
    if n >= 1:
        break
productos_seleccionados = []

print("Seleccione el numero del producto: ")
for i,val in enumerate(productosCategoria):
    nombre = val["nombre"]
    valor = val["valor"]
    print(f"        {i}. {nombre} con el precio de ${valor}")

for _ in range(n):
    seleccion_producto = int(input())
    producto_elegido = productosCategoria[seleccion_producto]
    productos_seleccionados.append(producto_elegido)

precio_total = sum(producto["valor"] for producto in productos_seleccionados)

print("Productos seleccionados: ")
for producto in productos_seleccionados: 
    print(f'{producto["nombre"]} - ${producto["valor"]}')

print(f"Precio total: ${precio_total}")