alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = ""
def encrypt(text, shift):
    output = ""
    for letters in text:
        if alphabet.index(letters) < 21:
            output = output + (alphabet[alphabet.index(letters) + shift])
        else:
            output = output + (alphabet[alphabet.index(letters) - 26 + shift])
    print(output)



def decrypt(text, shift):
    output = ""
    for letters in text:
        if (alphabet.index(letters)-shift) < 0:
            output = output + (alphabet[alphabet.index(letters) - shift]+26)
        else:
            output = output + (alphabet[alphabet.index(letters) - shift])
    print(output)
    

while(direction != 0):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    if direction == "encode":
        encrypt(text, shift)
    else:
        decrypt(text, shift)
