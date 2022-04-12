# lists to test
spam = ['apples', 'bananas', 'tofu', 'cats']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'] 

# comma code function
def input_list(myList):
    s = '' # creates an empty string vector
    last = myList[len(myList) - 1] # gets the last value from the list
    length = int(len(myList)) - 1 # gets the length of the list
    newList = myList[0:length] # creates a new list without the last value from the list
    for words in newList:
        s += words + ', ' # putting the values from the list as a string seperated by commas
    print(s + ' and ' + last) # prints the final string with the last value added to it

input_list(spam)
input_list(alphabet)


