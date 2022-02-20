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


# Metodo que soluciona a questão 2
def solucao(args):
    response = ""
    qtd_keys = how_many_keys()

    for register in range(len(args)):
        for prop in range(1, qtd_keys+1):
            values = get_values(get_key(prop))
            response += get_chars(args[register].get(get_key(prop)), int(values[0]), values[1], values[2]) 
        response += "\n"
    return response





print(solucao(input))

