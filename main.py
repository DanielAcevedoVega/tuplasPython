# tuplas Informacion, direccion, cursos, experencia laboral

print("""###Almacenamiento de datos###
Ingrese su informacion, nombre, edad, altura""");

nombre = input("Ingrese el nombre: ");
edad = input("Ingrese la edad: ");
altura = input("Ingrese la altura: ");
informacion = tuple((nombre, edad, altura));

direccion = input("Ingrese la direccion de su residencia: ");
varDir = (direccion)

while True: 
    n = int(input("Cuantos cursos tienes?: "))
    if n>=1:
        break;
nombre_cursos = []
for i in range(n):
    nombre_curso = input(f"Ingresa el curso {i+1}: ")
    nombre_cursos.append(nombre_curso)

tupla_cursos = tuple(nombre_cursos)

exp = input("¿Tienes alguna experiencia laboral?(s/n): ")
if exp == "s":
    experiencia = input("Escriba tu experiencia laboral: ")
else:
    experiencia = "no aplica"

expLaboral = (experiencia)

print("###### Su informacion es ######")
print(f"""Nombre: {informacion[0]} Edad: {informacion[1]} Altura: {informacion[2]} Direccion: {varDir}""")

print("Los cursos que tiene son: ")
for curso in tupla_cursos:
    print(f"- {curso}")

print(f"Experiencia laboral: {expLaboral}")


