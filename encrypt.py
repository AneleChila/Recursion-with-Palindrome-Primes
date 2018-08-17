'''
Anele Chila
2015/05/09
Encryption program
'''

characters = input("Enter a message:\n")
temp = ''                  
def encrypt(characters,temp):  
    """
    encryts a message by assigning it to the next character
    after itself. If letter is z it assigns it back to
    a to keep it in the letter range
    """
    if len(characters)==0:
        return temp
    
    else:
        if characters[0] == "z":
            temp += 'a'
            return encrypt(characters[1:], temp)
        elif not ord('a')<= ord( characters[0] ) <=ord('z'): #check if a letter is not in the alphbetical range:
            temp+= characters[0:1]
            return encrypt (characters[1:], temp) 
        
        else:
            temp+= chr(ord(characters[0])+1)
            return encrypt(characters[1:],temp)
        
print("Encrypted message:\n",encrypt(characters,temp),sep="")