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
              {"codigo":0, "nombre": "Descuento por cantidad", "cantidadMinima": 5, "descuento": 2000},
              {"codigo":1, "nombre": "Combo", "valor": 1500}
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
                {"codigo":0, "nombre": "Descuento por cantidad", "cantidadMinima": 3, "descuento": 500},
                {"codigo":1, "nombre": "Combo especial", "valor": 1200}
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
                {"codigo":0, "nombre": "Descuento por cantidad", "cantidadMinima": 8, "descuento": 1100},
                {"codigo":1, "nombre": "Combo especial", "valor": 600}
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
    print(f"        {i+1}. {nombre} con el precio de ${valor}")

for _ in range(n):
    seleccion_producto = int(input())-1
    producto_elegido = productosCategoria[seleccion_producto]
    productos_seleccionados.append(producto_elegido)

precio_total = sum(producto["valor"] for producto in productos_seleccionados)

print("Productos seleccionados: ")
for producto in productos_seleccionados: 
    print(f'{producto["nombre"]} - ${producto["valor"]}')
    

print(f"Precio total: ${precio_total}")