'''create a list with 4 details about you : name age mail and phone and print to the screen
then create aaother list with to ips' then add 3 more ips,
pop the 3rd ip and then print how many ips we have and print them'''

my_details=["mordechai", 30, "mordi@walla.com", "052511511"]
print("Youre Name is: " + my_details[0] + "\nYoure age is: " + str(my_details[1]) + "\nYoure mail is: " + my_details[2] + "\nYoure phone is: " + str(my_details[3]))
ip_list=['192.168.1.1', '192.168.1.2']
print(ip_list)
ip_list.append('192.168.1.254')
ip_list.append('192.168.1.255')
ip_list.append('192.168.1.3')
print("my ip list is: ")
for i in ip_list:
    print(i)

print("now i remove 3rd ip...")
ip_list.pop(2)

print("my new ip list is: ")
for i in ip_list:
    print(i)


print("length of list is:" + str(len(ip_list)))



