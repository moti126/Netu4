'''
create five dictonery with 5 name and money
sum the money of first and last and print them
add new name of the sum of money you calculate
cheack if mordi is inside '''

my_dict = {"yakov": 94, "sonya": 69, "boris": 89, "mordechai": 93, "daniela": 95}
sum_dict=my_dict["yakov"]+my_dict["daniela"]
my_dict.update({"new" : sum_dict})
print(my_dict)

print("mordi" in my_dict)

