#accepts the users input
letter = input("Enter you words for an alternate magic: ")
#uses split method to capture word list of the input
letter_list = letter.split(" ")
#writes a function to perform the task
#the function takes a str or list of string 
def alternate_magic(letter):
    new_list = []
    new = str()
    count = 0
    for each_charc in letter:
        #converts the str with even index to lower case str 
        if count % 2 == 0:
            new += each_charc.lower()
            new_list.append(each_charc.lower()) 
           

        else:
            #converts the str with odd index to upper case str 
            new += each_charc.upper()
            new_list.append(each_charc.upper())
            
        count += 1
    return new," ".join(new_list)
#prints the alternating characters    
print (f"I present to you the alternating character:  {alternate_magic(letter)[0]}")
#prints the alternating words   
print (f"I present to you the alternating word:  {alternate_magic(letter_list)[1]}")  