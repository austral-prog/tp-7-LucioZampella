
def index_of_by_index(color, colors, index):
    for i in range(index, len(colors)):
        if colors[i] == color:
            return i
    return -1

colores = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]

print(index_of_by_index("Black", colores, 1))
print(index_of_by_index("Black", colores, 4))
print(index_of_by_index("Green", colores, 2))

def index_of_empty(lista):
    color = ""
    for index, i in enumerate(lista):
        if color == lista[index]:
            return index
    return -1
print(index_of_empty(["Red", "Green", "", "", "Pink", "", "Black"]))
print(index_of_empty(["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]))

def index_of(color, colors):
    for index, i in enumerate(colors):
        if color == colors[index]:
            return index
    return -1
print(index_of("White", ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]))


def put(word, lista):
    color = ""
    for index, i in enumerate(lista):
        if color == lista[index]:
            lista[index] = word
            return lista
    return -1
print(put("Blue",["Red", "Green", "", "", "Pink", "", "Black"] ))
print(put("Blue",["Red", "Green", "Pink","Black"] ))


def remove(word, lista):
    for index, i in enumerate(lista):
        if word == lista[index]:
            lista[index] = ""
            return lista
    return -1

print(remove("Black", ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]))
print(remove("Gray", ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]))
