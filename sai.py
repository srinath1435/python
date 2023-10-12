from datetime import date
yearofBirth = input('please enter the date of the year')
dater =int(yearofBirth)
currentyear = date.today().year
age = currentyear-dater
print("Your age is:",age)
 
 
