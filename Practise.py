alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
direction = direction.lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(text, shift, direction):
    cipher = ""
    if direction == "decode":
        shift *= -1
    for i in text:
        index = alphabet.index(i)
        index += shift
        cipher += alphabet[index]
    print(f"The {direction} text is {cipher}")
caesar(text, shift, direction)

