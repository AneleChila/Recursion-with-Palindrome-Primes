'''
Anele Chila
Pal-primes
08 May 2016
'''
import sys
sys.setrecursionlimit (30000)

def palindromeprimes(M,N,lst):
    def pr_num(point,end = 1):
        if end == point:
            return True
        else:
            if point % end == 0 and end != 1:
                return False
            else:
                return pr_num(point, end + 1)   
            
    def reverse(sub_phrase):
        if sub_phrase == "":
            return sub_phrase
        else:
            return reverse(sub_phrase[1:]) + sub_phrase[0]    
        
    if M >=N:
        if pr_num(M,1):
            if M==int(reverse(str(M))):
                lst.append(M)
        palindromeprimes (M-1,N,lst)
lst = []
N = eval(input("Enter the starting point N: \n"))
M = eval(input("Enter the ending point M: \n"))
print ("The palindromic primes are:")  

palindromeprimes(M,N,lst)

array1 = sorted(lst)
def printlst(array1,pos=0):
    if pos<len(array1):
        print(array1[pos])
        return printlst(array1,pos+1)
printlst(array1,0)