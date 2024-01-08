#Help me write a program that will translate english sentences into morse code.

# I want to be able to type in a sentence and have it translated into morse code.

setence = input("Enter a sentence: ")

#create the english to morse code dictionary

morse_code = { 
                'A':'.-', 'B':'-...',
                'C':'-.-.', 'D':'-..', 'E':'.',
                'F':'..-.', 'G':'--.', 'H':'....',
                'I':'..', 'J':'.---', 'K':'-.-',
                'L':'.-..', 'M':'--', 'N':'-.',
                'O':'---', 'P':'.--.', 'Q':'--.-',
                'R':'.-.', 'S':'...', 'T':'-',
                'U':'..-', 'V':'...-', 'W':'.--',
                'X':'-..-', 'Y':'-.--', 'Z':'--..',
                ' ':'/',
            }

#loop through the sentence and convert each letter to morse code

for letter in setence:
    print(morse_code[letter.upper()], end=" ")
print("\nThis is your sentence: '{}' in morse code.".format(setence))



