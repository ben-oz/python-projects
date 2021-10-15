TEXT_START = """
###  This program converts decimal numbers to Roman Numerals ###
(To exit the program, please type 'exit')
"""
TEXT_ASK_INPUT = "Please enter a number between 1 and 3999, inclusively: "
TEXT_EXIT = "Exiting the program\n...Bye...\n" 


print(TEXT_START)

while True:
    user_input = input(TEXT_ASK_INPUT)
    if user_input.lower() == "exit":
        print(TEXT_EXIT)
        break
    
    else:
        try:
            user_input = int(user_input)
        
        except ValueError:
            print("Not a valid input! Please Enter a decimal number\n")
        
        else:
            if not 1 <= user_input <= 3999:
                print("Not a valid input! Please enter a number between 1-3999 inclusively\n")
            
            else:
                print("..... Converting ......")
                letters = {
                    1000: 'M',
                    500: 'D',
                    100: 'C',
                    50: 'L',
                    10: 'X',
                    5: 'V',
                    1: 'I'
                }
                divisors = letters.keys()
                letter_counts = []
                in_roman = []
                remainder = user_input
                for divisor in divisors:
                    quotient = remainder // divisor
                    letter_counts.append(quotient)
                    [in_roman.append(letters[divisor]) for _ in range(quotient)]
                    remainder = remainder % divisor
                in_roman_string = ''.join(in_roman)
                
                special_numbers = {
                   'DCCCC': 'CM',
                   'CCCC': 'CD',
                   'LXXXX': 'XC',
                   'XXXX': 'XL',
                   'VIIII': 'IX',
                   'IIII': 'IV'
                }
                result = ''
                for k, v in special_numbers.items():
                    result = in_roman_string.replace(k ,v)
                
                print(f"\n{user_input} in Roman Numerals is: {result}")
