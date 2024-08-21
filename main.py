import random
import sys

start_up_sequence = True
while(start_up_sequence):

# initial start up, prompts user for their choice
  correct_response = True
  while(correct_response):
    user_input = int(input('''
--Password Generator--
1: Generate Password
2: Exit The Program
Your Choice: 
                    '''))
    if user_input == 1:
      print("Password Generation in progress")
      correct_response = False
    elif user_input == 2:
      print("You have chosen to exit the program, Have a good day!")
      sys.exit()
    else:
      print("Please enter a correct input")
      continue

  # asking for user inputs regarding password generation
  password_length = int(input('Provide Password Length'))
  upper_case = input('Upper Case Letters?:(y/n)')
  digits = input('Digits?:(y/n)')
  special_chars = input('Special Characters:(y/n)')

  for var in [upper_case,digits,special_chars]:
    if var == 'y':
      var = True
    else:
      var = False
  
  # lists of potential characters
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  digits_list = '0123456789'
  special_char_list = '!@#$%&*^|()_+'

  if (upper_case, digits, special_chars):
    character_list = alphabet.upper() + digits_list + special_char_list + alphabet
    generated_password = ''.join(random.sample(character_list, password_length))

  elif (upper_case, digits):
    character_list = alphabet.upper() + digits_list + alphabet
    generated_password = ''.join(random.sample(character_list, password_length))

  elif (upper_case, special_chars):
    character_list = alphabet.upper() + special_char_list + alphabet
    generated_password = ''.join(random.sample(character_list, password_length))

  elif (digits, special_chars):
    character_list = digits_list + special_char_list + alphabet
    generated_password = ''.join(random.sample(character_list, password_length))

  elif (digits):
    character_list = digits_list + alphabet
    generated_password = ''.join(random.sample(character_list, password_length))

  elif (special_chars):
    character_list = special_char_list + alphabet
    generated_password = ''.join(random.sample(character_list, password_length))
  
  elif(upper_case):
    character_list = alphabet.upper() + alphabet
    generated_password = ''.join(random.sample(character_list, password_length))

  else:
    character_list = alphabet
    generated_password = ''.join(random.sample(character_list, password_length))
    


  print("Your New Password: " + generated_password)


