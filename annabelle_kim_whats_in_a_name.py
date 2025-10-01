'''
Author: Annabelle Kim
Due date: 9/30/2025
Bugs: Limited numbrer of titles(not all titles can be checked for, only a certain a selected few)
Bonus: Build a Menu, Title/distinction
Sources: Mr. Campbell and Ms. Marciano
Log: 1.0
'''

import time 
import random


def reverse(string):
    '''
    Description:
        Reverses the name given
    Args:
        string (str): the name that the user gives
    Returns:
        prints: the reverse of the name
    '''
    reversestring = string[::-1]
    print (reversestring)

def vowels(word):
    '''
    Description:
        counts the number of vowels in the name
    Args:
        word (str): the name that the user gives
    Returns:
        prints: the subtotal count of each vowel
    '''
    name = str.lower(word)
    a_count=0
    e_count=0
    i_count=0
    o_count=0
    u_count=0
    for character in name:
        if character in ["a"]:
            a_count += 1
        elif character in ["e"]:
            e_count += 1
        elif character in ["i"]:
            i_count += 1
        elif character in ["o"]:
            o_count += 1
        elif character in ["u"]:
            u_count += 1
    print(f"a = {a_count}")
    print(f"e = {e_count}")
    print(f"i = {i_count}")
    print(f"o = {o_count}")
    print(f"u = {u_count}") 

def consonant(word):
    '''
    Description:
        counts the number of consonants in the user's name
    Args:
        word (str): the name that the user gives
    Returns:
        prints: the total number count of consonants
    '''
    consonant_count=0
    for character in word:
        if character in ["q","w","r","t","y","p","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]:
            consonant_count += 1
    print (consonant_count)


def hyphen(full_name):
    '''
    Descrption:
        Checks to see if there is a hyphen in the name
    Args:
        full_name (str): the name that the user gives
    Returns:
        returns: boolean - True or False
    '''
    if "-" in full_name:
        return True
    else:
        return False

def palindrome(full_name):

    '''
    Desciption:
        Finds if the first name is a palindrome
    Args:
        full_name (str): the full name that the user gives
    Returns:
        returns: boolean - the reverse of the name
    '''

    first= first_name(full_name)

    if first == first[::-1]:
        return True
    else:
        return False

def get_names(fullname):
    names = []
    name = ''

    #Code will run through all of the letters in the given name. It will add every letter into a string, but if the code hits a space the code will add the letters up to this point in a list and will reset the "name" string into a blank string, and run through the code again.

    for letter in fullname:
        if letter == ' ':
            names.append(name)
            name = ''
        else:
            name += letter
    names.append(name)
    return names

def first_name(name):

    '''
    Description:
        Finds the first name
    Args:
        name (str): the full name that the user gives
    Returns:
        returns: the first name
    '''

    names = get_names(name)
    return names[0]

def middle_name(name):

    '''
    Description:
        Finds the middle name(s)
    Args:
        name (str): the full name that the user gives
    Returns:
        returns: the middle name(s)
    '''

    names = get_names(name)
    return ' '.join(names[1:-1])

def last_name(name):

    '''
    Description:
        Finds the last name
    Args:
        name (str): the full name that the user gives
    Returns:
        returns: the last name
    '''

    names = get_names(name)
    return names[-1]


def lowercase(name):

#ord returns the numeral value of an element from the use of the ascii table. The uppercase letters are in the range of 65-90. By adding each letter value by 32, it will turn the uppercase numeral values, into the lowercase numeral values. The numeral values will then be changed back into characters through the use of the function "char". The code will add the values all together to make the new name.


    '''
    Description:
        Makes the full name lowercase
    Args:
        name (str): the full name that the user gives
    Returns:
        returns: the full name in all lowercase
    '''

    name_out = " "
    for letter in name:
        if ord(letter)>64 and ord(letter)<91:
            num = ord(letter)
            num = num+32
            letter = chr(num)
            name_out = name_out + letter
        else:
            name_out = name_out + letter
    return name_out

def uppercase(name):

    '''
    Description:
        Makes the full name uppercase
    Args:
        name (str): the full name that the user gives
    Returns:
        returns: returns the name in all uppercase
    '''

    #ord returns the numeral value of an element from the use of the ascii table. The lowercase letters are in the range of 97-122. By subtracting each letter value by 32, it will turn the lowercase numeral values, into the uppercase numeral values. The numeral values will then be changed back into characters through the use of the function "char". The code will add the values all together to make the new name.

    name_out = " "
    for letter in name:
        if ord(letter)>96 and ord(letter)<123:
            num = ord(letter)
            num = num-32
            letter = chr(num)
            name_out = name_out + letter
        else:
            name_out = name_out + letter
    return name_out

def title(word):
    full = str.lower(word)
    split_name = full.split(" ")
    for string in split_name:
        if string in ["dr.", "sir", "esq", "ph.d"]:
            return True
        else:
            return False

def gen_random(name):

    '''
    Description:
        Create a random name (mix up the letters)
    Args:
        string (str): the name that the user gives
    Returns:
        prints: the new random name of mixed up letters
    '''

    length = len(name)
    char_list = list(name)
    sorted_string = "".join(random.sample(char_list, length))
    print(sorted_string)
    
def initials(name):

    '''
    Description:
        Gets the intials of the full name
    Args:
        name (str): the full name that the user gives
    Returns:
        prints: the intitals
    '''

    names = name.split()
    initials = ""

    for n in names:
        initials += n[0].upper() + ". "
    print (initials)

def main():

    full_name = input("Insert your full name (first middle and last): ")

    while True:
        option = input("""
What would you like to do?

1. Reverse name
2. Count the vowels
3. Count the consonants
4. Convert name to all lowercase
5. Convert name to all uppercase
6. Get Initials
7. Return first name
8. Return middle name
9 Return last name
10. Is there a hyphen
11. Is name a palindrome
12. Generate random name
13. Check for title in name
                    
""")
        if option == "1":
            reverse(full_name)
            time.sleep(1)
        elif option == "2":
            vowels(full_name)
            time.sleep(1)
        elif option == "3":
            consonant(full_name)
            time.sleep(1)
        elif option == "4":
            print(lowercase(full_name))
            time.sleep(1)
        elif option == "5":
            print(uppercase(full_name))
            time.sleep(1)
        elif option == "6":
            initials(full_name)
            time.sleep(1)
        elif option == "7":
            print(first_name(full_name))
            time.sleep(1)
        elif option == "8":
            print(middle_name(full_name))
            time.sleep(1)
        elif option == "9":
            print(last_name(full_name))
            time.sleep(1)
        elif option == "10":
            print(hyphen(full_name))
            time.sleep(1)
        elif option == "11":
            print(title(full_name))
            time.sleep(1)
        elif option == "12":
            gen_random(full_name)
            time.sleep(1)
        elif option == "13":
            print(title(full_name))
            time.sleep(1)

main()