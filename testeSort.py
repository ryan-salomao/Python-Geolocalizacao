enderecos = {
    "Rua Silva": 3.5, #Km
    "Rua Rocha": 2.8, #Km
    "Rua Limoeiro": 5.2, #Km
}

enderecos_lista = enderecos.items()

def criterio(lista):
    return lista[1]

enderecos_ordenados = (sorted(enderecos_lista, key=criterio))
print(enderecos_ordenados)

""" 
for endereco in enderecos_lista:
    print(endereco[0])
    print(endereco[1])

print("\n")
print(sorted(enderecos_lista, key=lambda x:x[1]))
""" 

"""
#template projeto

for endereco, distancia in enderecos_ordenados:
    print(endereco, distancia, "Km")
""" 