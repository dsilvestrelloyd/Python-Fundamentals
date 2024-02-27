sentence = input("Please enter a phrase or sentence: ")

alternating_sentence = sentence.split()
lower_or_upper = True
word = ""
changed_sentence = []


for crazy in alternating_sentence:
     
    for letter in crazy:
        if letter.isalpha() == True:

            if lower_or_upper == True:
                word += letter.lower()
                print(word)
                lower_or_upper = False
            else:
                word += letter.upper()

                lower_or_upper = True 
        else:
            word += letter
            print(word)
            

    changed_sentence.append(word)
    word = ""

        
changed_sentence = " ".join(changed_sentence)
print(changed_sentence)


# defining a function to take the parameter sentence
def capital_vs_lower(sentence):

    # define an empty string variable before their use in a loop
    new_sentence = ""
    
    for i in sentence:

        # conditional to check is if the current character in the variable i is equal to an uppercase character 
        if i == i.upper():
        
        # concatenate variable new_sentence with the current value of i converted to lowercase
            new_sentence += i.lower()
            
        # conditional to check is if the current character in variable i is equal to a lowercase character    
        elif i == i.lower(): 
            # concatenate variable new_sentence with the current value of i converted to uppercase
            new_sentence += i.upper()

        # else condition is for any blank spaces, numbers or special characters, basically any non-alphabetic characters  
        else: 
        # concatenate variable new_sentence with the current value of i 
            new_sentence += i
    
    return new_sentence

