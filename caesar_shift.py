alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
direction = direction.lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(text, shift, direction):
    cipher = ""
    if direction == 'encode':
        for i in text:
            index = alphabet.index(i) + shift
            if index >= len(alphabet):
                index -= len(alphabet)
            cipher += alphabet[index]
        print(cipher)
    elif direction == 'decode':
        for i in text:
            index = alphabet.index(i) - shift
            if index < 0:
                index += len(alphabet)
            cipher += alphabet[index]
        print(cipher)
caesar(text, shift, direction)

