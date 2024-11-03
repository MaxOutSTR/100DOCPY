import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(text, shift, encode_or_decode):
  result = ""

  if encode_or_decode == "decode":
    shift *= -1

  for index in range(len(text)):
    letter = text[index]
    if letter in alphabet:
      new_index = (alphabet.index(letter) + shift) % len(alphabet)
      new_letter = alphabet[new_index]
      result += new_letter
    else:
      result += letter

  return result

again = True
while again:
  direction = input("Enter 'decode' to decrypt, or 'encode' to encrypt: ")
  text = input("Enter the message: ")
  shift = int(input("Enter the shift value: "))

  print(caesar(text, shift, direction))

  choice = input("Would you like to go again?(yes/no): ")

  if choice.lower() != "yes":
    again = False