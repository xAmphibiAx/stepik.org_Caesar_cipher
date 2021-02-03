eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

print('Программа шифровки / дешифровки текста по методу Цезаря')
k = int(input('Введите шаг сдвига для шифровки ( >0 ) или дешифровки ( <0 ) \n').strip())


def ceasar(inp):
    out = ''
    for i in range(len(inp)):
        if inp[i] in eng_lower_alphabet:
            out += eng_lower_alphabet[(eng_lower_alphabet.find(inp[i]) + k) % 26]
        elif inp[i] in eng_upper_alphabet:
            out += eng_upper_alphabet[(eng_upper_alphabet.find(inp[i]) + k) % 26]
        elif inp[i] in rus_lower_alphabet:
            out += rus_lower_alphabet[(rus_lower_alphabet.find(inp[i]) + k) % 32]
        elif inp[i] in rus_upper_alphabet:
            out += rus_upper_alphabet[(rus_upper_alphabet.find(inp[i]) + k) % 32]

        else:
            out += inp[i]
    return out


inpu = input('Введите текст для шиврования/дешифрования: \n')
print(ceasar(inpu))
