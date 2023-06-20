#This is the Encode Decode program

alphabet = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
restart = True
while (restart == True):
  direction = input(
    "Type 'Encode' to Encrypt the Mesage ,'Decode' to Decrypt the message:\n"
  ).lower()
  text = input("Type your message\n").lower()
  shift = int(input("Type the shift number :\n"))
  shift = shift % 25

  def caesor(user_direction, user_starttext, user_shift):
    end_text = ""

    for char in user_starttext:
      if char in alphabet:
        position = alphabet.index(char)
        if user_direction == 'encode':
          new_position = position + shift
        else:
          new_position = position - shift
        new_letter = alphabet[new_position]
        end_text = end_text + new_letter
      else:
        end_text = end_text + char

    if user_direction == 'encode':
      print("Your Encrypted Message is :", end_text)
    else:
      print("Your Decrypted code is :", end_text)

  caesor(user_direction=direction, user_starttext=text, user_shift=shift)

  restart = input(
    "Type 'Yes' if you want to continue the process otherwise type 'no':\n "
  ).lower()
  if restart == 'yes':
    restart = True
  else:
    restart = False
