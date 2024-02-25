# The program will calculate your shopping cart

Tomato=3
cucumber=2
cola=5
chiken=20
#vat=

BTomato=(int(input("How much Tomato you take?")))
BTomato=BTomato*Tomato

Bcucumber=(int(input("How much cucumber you take?")))
Bcucumber=Bcucumber*cucumber

Bcola=(int(input("How much cola you take?")))
Bcola=Bcola*cola

Bchiken=(int(input("How much kilo chiken you take?")))
Bchiken=Bchiken*chiken
Vat=int(BTomato+Bcucumber+Bcola+Bchiken*0.17)
print("youre bill without VAT is: " + str(BTomato+Bcucumber+Bcola+Bchiken) + "\nYoure Bill with VAT is: " + str(BTomato+Bcucumber+Bcola+Bchiken+Vat))




