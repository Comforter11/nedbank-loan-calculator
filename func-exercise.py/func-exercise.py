# Exercise 1
def distance_from_zero(num):

    if num.isdigit():
        if len(num.split(",")) > 1:
            return abs(float(num))
            return abs(int(num))
        return "Nope"

number = input("Please enter a number:")

print(distance_from_zero(number))

# Exercise 2
def leap_year(a):
    if a%4==0 or (a%100==0 and a%400==0):
        return True
    else:
        return False

year= int(input("Enter a year:"))

if (leap_year(year) ==True):
    print(year,"is leap year!")
else:
    print("False")
