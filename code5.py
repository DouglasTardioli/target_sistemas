def inverter_string(s):
    invertida = ""
    for letra in s:
        invertida = letra + invertida
    return invertida

string_original = input("Digite uma palavra: ")
string_invertida = inverter_string(string_original)
print(f"String invertida: {string_invertida}")