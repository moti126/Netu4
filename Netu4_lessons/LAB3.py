'''
ליצור 3 משתנים
1: שם מלא
2: אימייל
3: גיל
בסוף להדפיס הכל
לאחר מכן להדפיס את השם מהסוף להתחלה ולהדפיס באותו סטרינג את הגיל כפול 3
לבסוף לבדוק האם הש נמצא בתוך הסטרינג הבא:
idan ben dudu yuval shimon yael gal adam shahar yana
'''

FullName=input("what is you're full name? ")
EmailAddress=input("What is you're Email Adress: ")
Age=int(input("What is you're age? "))
print("You're Name is: " + FullName + "\nYou're Email is: " + EmailAddress + "\nYou're Age is: " + str(Age))

print("Now i will print the name from the end to start and three times you're age. \nUpside down name: " + FullName[::-1] + "\nNew Age: " + str(Age*3))

print(FullName in "idan ben dudu yuval shimon yael gal adam shahar yana")