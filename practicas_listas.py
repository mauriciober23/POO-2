notas= [10,8,9,5]
print(notas)
notas.append(20)
notas.insert(1,10)
print(notas[1])
print(len(notas))
print(notas[-1])
print(notas[0])
print(notas[-2])
print(sum(notas))
print(max(notas))
print(min(notas))
notas.remove(9)
notas.sort()
print(notas)
print(notas[2:])
print(notas[:2])
print(notas[::-1])


#tuplas

meses= ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
print(meses[0])
print(meses[-1])

#diccionario

estudiante={
    "cedula": "0107945529",
    "nombre": "Andersson",
    "correo": "mauriciober23@gmail.com",
    "telefono": "0990854589",
    "notas": [10,8,9,5],
}
print(estudiante.get("nombre"))
print(estudiante.keys())


#conjuntos

conjunto_a={1,1,5,4,6,8}
conjunto_b={1,9,6,5,4}
print(conjunto_a & conjunto_b)
print(conjunto_a | conjunto_b)
