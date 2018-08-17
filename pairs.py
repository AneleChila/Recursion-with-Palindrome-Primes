'''
Anele Chila
Pairs
08 May 2016
'''
sub_phrases = input("Enter a message:\n")
position = 0 #initialise position counter

def pair(sub_phrases,position):
    if len(sub_phrases)==0 or len(sub_phrases)==1:
        return 0 #return zero if the word is o or 1 character long
    elif sub_phrases[0] == sub_phrases[1]:
        position = position + 1#Increment the position to move to the next character:
        answer = pair (sub_phrases[2:],position)+(2-1) #recursive step that increases the value returned by the function everytime a pair is found
        return answer
    else:
        answer = pair(sub_phrases[1:],position)
        return answer
        
print("Number of pairs:",pair(sub_phrases, position))
