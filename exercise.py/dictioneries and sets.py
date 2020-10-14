# Task 1

a_string = "Comforter"
a_character = "o"

print(a_character)

a_string =  a_string.count('o') # counting the character "o" in the given string.

print("The count of 'o' is", a_string)

#or
a_string =(str(input("Please enter a string:" )))
a_character =(str(input("Please enter a character:")))
len(a_string)
print("It appears in your string",a_string.count(a_character),"times")

#Task 2

num = int(input("Please enter any number"))
num_words = {0:'zero', 1:'one', 2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
for num in str(num):

    print(num_words[int(num)], end=" ")

#Task 3

colour_set =("black","white","red","purple","silver")
print(colour_set)
#update set
colour_set.add("emerald")
print((colour_set.add)("colour_set"))

