import string
import random

def get_strength():
    level = input('How strong of a password would you like to generate: Weak (no special characters), Medium, or Max? \n')
    if level.lower() == 'weak':
        return 7
    elif level.lower() == 'medium':
        return 11
    elif level.lower() == 'max':
        return 16
    else:
        print('Please pick one of the three options')
        main()

def main():
    characters_weak = list(string.ascii_letters + string.digits)
    characters = list(string.ascii_letters + string.digits + string.punctuation)
    
    level = get_strength()

    password = ''.join(random.sample(characters, k=level))
    print(password)

    option = input('Would you like to run the program again? Type yes or anything else to exit \n')
    if option.lower() == 'yes':
        main()
    
main()
