def enumerate_list(lista):
	new_lista = []
	index = 0
	for  string in lista:
		if string:
			new_lista.append(f"{index}. {string}")
			index += 1
	return new_lista

print(enumerate_list(["Red", "Green", "Blue", "", "Yellow"]))

def enumerate_backwards(lista):
	new_lista = []
	index = 0
	for string in lista:
		if string:
			new_lista.append(f"{index}. {string[::-1]}")
			index += 1
	return new_lista
print(enumerate_backwards(["Red", "Green", "Blue", "", "Yellow"]))
