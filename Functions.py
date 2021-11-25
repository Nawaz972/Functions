# Program based on functions
str=input("Please enter the string: ")        # Reading the string
def most_frequent(string):                   # Defining the most_frequent function 
    d=dict()
    for key in string:
        if key not in d:
            d[key]=1
        else:
            d[key]+=1
    return d                                       # Returning the frequency of the words of string
print(most_frequent(str))                  # Printing the frequency of the string