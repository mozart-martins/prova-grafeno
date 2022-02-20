input = [
    { "name": "Maria Neusa de Aparecida", "cpf": "97905796671", "state": "Sao Paulo", "value": "1234" },
    { "name": "Ricardo Fontes", "cpf": "44010762900", "state": "Rio Grande do Sul", "value": "567" }
]


# Calcula quantas chaves de primeiro nível existem
def how_many_keys():
    response = 0
    for i in range(1, 10):
        if get_key(i) is not None:
            response += 1

    return response


# Captura o nome do campo
# get(1)
# return cpf
def get_key(index):
    current_index = 0
    file = open("format-1.yaml", "r")
    for line in file.readlines():
        if ":" in line and line[:1] != " ":
            current_index += 1
            if current_index == index:
                return line[:len(line)-2]
            if current_index > index:
                raise Exception("Chave inexistente no arquivo.")


# Captura o valor de uma propriedade
# get_property_value(" align: 11\n")
# return 11
def get_property_value(item):
    return item[item.index(":")+1:].strip()


# Captura os valores propriedades / chave
# get_values(yml_file, "cpf")
# return ['11', 'left', 'spaces']
def get_values(key):
    file = open("format-1.yaml", "r")
    response = []
    lines = file.readlines()
    index = lines.index(key + ":\n")
    response.append(get_property_value(lines[index+1]))
    response.append(get_property_value(lines[index+2]))
    response.append(get_property_value(lines[index+3]))
    return response


# Captura N caracteres de um valor
def get_chars(text, length, align, char):

    if char == "spaces":
        char = " "
    if char == "zeroes":
        char = "0"

    response = text[:length]

    if align == "left":
        if len(response) == 0:
            return "".ljust(length, char)
        if len(response) < length:
            response = response.ljust(length, char)
    
    if align == "right":
        if len(response) == 0:
            return "".rjust(length, char)
        if len(response) < length:
            response = response.rjust(length, char)

    return response


def remove_extra_fill(text, length, chars):
    
    for i in range(length):
        if chars == "spaces":
            if text[0:1] == " ":
                text = text[1:]
        if chars == "zeroes":
            if text[0:1] == "0":
                text = text[1:]

    return text



# Metodo que soluciona a questão 3
def solucao(args):
    response = {}
    qtd_keys = how_many_keys()
    string_start = 0

    for prop in range(1, qtd_keys+1):
        key = get_key(prop)
        values = get_values(key)
        response[key] = remove_extra_fill(args[string_start:(string_start + int(values[0]))], int(values[0]), values[2])
        string_start += int(values[0])

    return response





print(solucao(("97905796671Maria Neusa de00001234")))
print(solucao(("44010762900Ricardo Fontes00000567")))