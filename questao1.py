


input = [
    { "name": "Maria Neusa de Aparecida", "cpf": "97905796671", "state": "Sao Paulo", "value": "1234" },
    { "name": "Ricardo Fontes", "cpf": "44010762900", "state": "Rio Grande do Sul", "value": "567" }
]


def get_eleven_chars(text):
    response = text[:11]
    if len(response) == 0:
        return '           '
    if len(response) < 11:
        response = response.ljust(11)
    return response


def solucao(args):
    response = ""

    for i in range(len(args)):
        response += "\n" + get_eleven_chars(args[i].get("name")) 
        response += get_eleven_chars(args[i].get("cpf")) 
        response += get_eleven_chars(args[i].get("state")) 
        response += get_eleven_chars(args[i].get("value"))

    return response



print(solucao(input))