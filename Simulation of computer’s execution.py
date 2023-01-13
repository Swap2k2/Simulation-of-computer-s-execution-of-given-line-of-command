from typing import Tuple

# To open the input file and check the statements

lines = [] # initalise to empty list
with open('input_file.txt') as f:
    lines = f.readlines() # read all lines into a list of string

# Defined Intermediate lists to be used   
DATA_ = []      #main list
D1 = []     
D2 = []




def helper_a(list,k): 
      # helper function to check the presence of type of k in list
    z1=False

    for i in list:  # looping through the list

        if type(i)==type(k):    # condition for the common type check

            if i==k:
                z1=True
                break

    return z1

def helper1(x):
    # index 
    if x in D1:
        k = D1.index(x)
        return str(DATA_[D2[k]])

    else:
        return ('Error')



def findindex(list,k):   # Helper function   # to check the validiy of inputs 

    if helper_a(list,k)==False: # check if k is in list or not 
        return ('Value not found')

    else:

        index=0 # initialisation

        for i in range (0,len(list)):       #looping

            if type(list[i])==type(k):  # matching the type of element in list with type of k

                if list[i]==k:  # if found go for next one
                    index+=i
                    break

        return index # finally return the index 

# list of operators 
op = ['/','+','and','or','not','-','==','>','>=','<=','*','<']



n = len(lines)  # length of list 'lines'
         
# Using loop to traverse via the list of line 
for i in range (0,n):

    lines[i].strip()    # Removing Spaces from the line 
    token_=lines[i].split(" ")

    # Using loop to traverse via the list of tokens fromed out of a line
    for i in range(2,len(token_)):  # starting the loop from right side of comparing operator

        if (token_[i].strip().isnumeric() or token_[i].strip()=='True' or token_[i].strip()=='False') :

            if token_[i].strip().isnumeric():   # condition for numeric token

                if helper_a(DATA_,int(token_[i].strip()))==False:   #check if token is in DATA_ or not
                    DATA_.append(int(token_[i].strip()))    # if not then append to DATA_

            # check if the token is bool or not 
            else:
                if (str(token_[i].strip())=='True' or str(token_[i].strip())=='False') and helper_a(DATA_,bool(token_[i].strip())):
                    DATA_.append(bool(token_[i].strip()))   #appending token to DATA_
            continue

        elif helper_a(op,token_[i].strip()):    # checking if token is one of the operations 
            continue        # if it is an operation then move onto the next token

        else:
            a=helper1(token_[i].strip())        # removing spaces from the token
            token_[i]=a

    z1 =' '.join(token_[2:])    # joining the list of tokens to form a single string in order to evaluate the RHS 

    if helper_a(DATA_,eval(z1)) == False:   # RHS exist in DATA_ or not 
        DATA_.append(eval(z1))  # If does not exist then append

    if helper_a(D1,token_[0]) == False:     # token_[0] in D1 or not
        D1.append(token_[0])        # if not then append token_[0]
        D2.append(findindex(DATA_,(eval(z1))))  # finally appending indexx of the tuple of variable and it's values' index 

    elif helper_a(D1,token_[0]):
        D2[findindex(D1,(token_[0]))]=findindex(DATA_,(eval(z1)))


DATA = DATA_.copy()

for i in range (0,len(D1)): # appending the elements to final list DATA from D1(the list of indexes tuple)
    DATA.append((D1[i],D2[i]))


for i in range (0,len(DATA)):       # finally printing the values of variables ## Looping for each variable 
    if isinstance(DATA[i],tuple) == True :  # checking the tuple and adding from it only
        print(DATA[i][0] , '=' , DATA[DATA[i][1]]) # finally printing the variables



## Making GARBAGE list 

GARBAGE = []

# helper function to find the element in the list ## used from the notes 
def binsearch (L, first, last, k):        # Time complexity is O(logn) where n is the number of elements of list L
# INPUT L is a list of elements from an ordered set (e.g. integers)
# INPUT integer indexes first and last are the
# first and last index of the search range
# INPUT k is the integer we try to find in list L
# OUTPUT True, if k is present in L.
# False if k is not present in L.
# ASSUME that L is sorted, i.e. the elements of L are in non-decreasing
# order from first to last
    if last < first:
        return False # Search range is empty
    else:
        mid = (first + last)//2 # mid-point of search range
        if (k == L[mid]):
            return True # k is present at mid
        elif (k < L[mid]): # Can avoid searching above mid
            return binsearch (L,first,mid-1,k)
        else: # Can avoid searching below mid
            return binsearch (L,mid+1,last,k)
    return False
def inlist(S,e) :   
    if binsearch(S, 0, len(S)-1, e) == True : # Time cmplexity is equal to T(binsearch)
        return True
    else :
        return False
for i in range (0,len(DATA)):
    if isinstance(DATA[i] , tuple) == False:        # checking the values in DATA which is not in tuple
        if inlist(D2,DATA[i]) == False :    # if DATA[i] not in D2 then append to GARBAGE as is of no use
            GARBAGE.append(DATA[i])

print('GARBAGE' , '=' , GARBAGE)       # finally printing the garbage values 


            
            
        
        
        
    
            
        
        
