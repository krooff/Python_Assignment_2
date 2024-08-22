year = int (input("Please Enter the Four Digit Year You're Interested to Know About."))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):

    print("This year is a Leap Year!")

else:

    print("Looks like this year is not a Leap Year.")