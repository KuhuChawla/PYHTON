# Python program to check if year is a leap year or not

year = 300

# To get user input, un-comment code below

# year = input("Year: ")
# if not year.isnumeric():
#     exit("Invalid number")
# year = int(year)

if not year%100 == 0 and year%4 == 0 or year % 400 == 0:
    print(f"{year} Is a leap year")
else:
    print(f"{year} Is not a leap year")
