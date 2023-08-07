# Muhammed Burhan LeetSpeakify: English to Leetspeak Translator

def uppercase(my_string):
    # Replace lowercase letters with uppercase letters
    upper_case = ""
    for char in my_string:
        if ord (char) >= 97 and ord(char) <= 122:
            upper_case = upper_case + chr(ord(char) - 32)
        else:
            upper_case = upper_case + char
    return upper_case

def acronym(my_string):
    # Using spliting of lists to split the phrase into smaller words in order to write them as an acronym.
    new_string = ""
    string_list = my_string.split()
    list_length = len(string_list)
    for i in range (list_length):
        if string_list[i] == "BE" and string_list[i+1] == "BACK" and string_list[i+2] == "LATER":
            string_list[i] = "BBL"
            string_list[i+1] = ""
            string_list[i+2] = ""
        if string_list[i] == "AWAY" and string_list[i+1] == "FROM" and string_list[i+2] == "KEYBOARD":
            string_list[i] = "AFK"
            string_list[i+1] = ""
            string_list[i+2] = ""
        if string_list[i] == "HOPE" and string_list[i+1] == "THIS" and string_list[i+2] == "HELPS":
            string_list[i] = "HTH"
            string_list[i+1] = ""
            string_list[i+2] = ""
        if string_list[i] == "I" and string_list[i+1] == "KNOW":
            string_list[i] = "IK"
            string_list[i+1] = ""
    for j in (string_list):
        new_string = new_string + j
        if j == "":
            new_string = new_string + " "
    return new_string

def homo(my_string):
    # Creating the homoglyphs for the acronym letters in this function.
    new_string = ""
    string_list = list(my_string)
    for j in range(len(string_list)):
        if string_list[j] == "A":
            string_list[j] = "@"
        if string_list[j] == "B":
            string_list[j] = "|3"
        if string_list[j] == "H":
            string_list[j] = "|-|"
        if string_list[j] == "K":
            string_list[j] = "|<"
    for i in string_list:
        new_string = new_string + i
    
    return new_string


def main():
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~+''' # Punctuation variable used to store all the punctuation
    my_string = input("Please enter a phrase: ")   # Asks the user for a string
    no_punctuation = ""   # This removes all punctuation from the string
    for char in my_string:
        if char not in punctuations:
            no_punctuation = no_punctuation + char

    no_punctuation = uppercase(no_punctuation)     # Printing out the acronyms, homoglyphs, and the strings
    print(no_punctuation)
    no_punctuation = acronym(no_punctuation)
    print(no_punctuation)
    no_punctuation = homo(no_punctuation)
    print(no_punctuation)
   
main()