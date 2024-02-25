'''
Menu:
1. Insert number and ** it by 3
2. Insert 4 IPs to a list and print it
3. Insert 4 Entries to DNS dictionery and print it
4. check if the string is polindrom
if it is not 1-4 ' then choose again
'''

from time import sleep
print('''
Menu:
1. Insert number and ** it by 3
2. Insert 4 IPs to a list and print it
3. Insert 4 Entries to DNS dictionery and print it
4. check if the string is polindrom
''')


option=input("Select the relevant option from the menu:\n")
#int(option)
if option != int:
    print("print digits only")
elif option!=1 or option!=2 or option!=3 or option!=4:
    print("please enter only 1-4")
    option = input("Select the relevant option from the menu:\n")
elif (option==2):
    my_list=[]
    my_list.append(input("add 1st IP:\n"))
    my_list.append(input("add 2nd IP:\n"))
    my_list.append(input("add 3rd IP:\n"))
    my_list.append(input("add 4th IP:\n"))
    print("1: " + my_list[0] + "\n2: " + my_list[1] + "\n3: " + my_list[2] + "\n4: " + my_list[3])


elif (option==1):
    number=int(input("Enter a number:\n"))
    number=number**3
    print("The sum is: " + str(number))

elif (option==3):
    DNS={}
    DNS["www.google.com"]=input("DNS www.google.com\n")
    DNS["www.walla.com"] =input("DNS www.walla.com\n")
    DNS["www.youtube.com"] =input("DNS www.youtube.com\n")
    DNS["www.zip.com"] =input("DNS www.zip.com\n")
    print(DNS)

elif (option==4):
    check=input("please enter a name\n")
    polindrom=check[::-1]
    if (check == polindrom):
        print("this is polindrom!!")
    else:
        print("this is not polindrom!")















