def rot13(text: str, shift: int):
    result = ""
    for char in text:
        result += (chr((ord(char) + shift - 97) % 26 + 97),chr((ord(char) + shift - 65) % 26 + 65))[char.isupper()]
    return result
rot13("Hello", 0)

text = "Hello"

print(text)
shift = 5
chiper = rot13(text, shift)
dechiper = rot13(chiper, -shift)

print(text, shift, chiper, dechiper)