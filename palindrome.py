'''
Anele Chila
Palindrome
08 May 2016
'''
def pal(phrase):
    """
    function to determine whether a sub_phrase 
    is a pal or not
    """
    if len(phrase) != 0:
        array = phrase.split(" ")#store phrase in a list
        number = 0 # to count the number of times a pal appears
    else:
        print()
        
    #define function called invert to invert a sub_phrase:
    def invert(sub_phrase):
        """
        function to invert a sub_phrase
        """
        if len(sub_phrase) == 0:
            return sub_phrase
        else:
            return invert(sub_phrase[1:]) + sub_phrase[0] #recursive function to invert sub_phrase
    number = 0        
    def look_at_(array,number,position=0): 
        """
        function to check if any of the reversed sub_phrases in a list
        are palindromes
        """
    
        if position<len(array):
            if len(array[position])<=1:
                pass
            else:
                if array[position]==invert(array[position]):
                    number += 1
            return look_at_(array,number,position+1)
            
        return number
                            
    if len(phrase)!=0:
        if look_at_(array,0,0)>0:
            return "Palindrome!"
        else:
            return "Not a palindrome!"
    else:
        return 
phrase = input("Enter a string:\n")
print(pal(phrase))