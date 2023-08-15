#Printing Random Satements
print("\n")
print("Hello World!")
print("My name is Taneshka Mehta, This is a simple python code")
print("\n")


#Input Function
name = input("What is your name?:")
print("\n")
age = input("What is your age?:")
print("\n")
print("The name entered is", name, "and the age entered is", age)
print("\n")
print("The mentioned age is {0}".format(age))
print("\n")

#Python Variables
x = 10
y = 50.20
n1 = "Taneshka Mehta"
n2 = "RISHABH DAHIYA"
b = True
print("\n")
print("My name is ", n1)
print("My friend's name is ", n2)
print("\n")
print(x,y,n1,n2,b)
print(type(x))
print(type(y))
print(type(n1))
print(type(n2))
print(type(b))
print("\n")
print(n1.isupper())
print(n1.islower())
print(n1.isalpha())
print(n2.isupper())
print(n2.islower())
print(n2.isalpha())
print("eshk" in n1)
print(n2[2])
print(n1[2:])
print(n1==n2)
print(n2.swapcase())
print("\n")

print("This code contains basic python commands \n It is quite intresting")
print("\n")
print("This \t is test \t for \t tab")
print("\n")

for i in range (1, 15):
    print("Number {0} -- square is {1} and cube is {2}".format(i, i**2, i**3))
print("\n")

#Data Type - List, Tuple, Set, Dictionary
lst = [10,20,30,40,50,60]
tpl = (1,2,'Taanu',True,'rst')
s = {50,100,150,200,250}
d = {}
diction = {
    '101': 'T',
    '102': 'S',
    '103':'R',
    '104':'Q'
    }
print(lst)
print(tpl)
print(s)
print(diction)
print(len(lst))
print(min(lst))
print(max(lst))
print(lst + [70,80,90,100])
print("\n")

#Function
def sum(x,y):
    sum = x+y
    return sum

print(sum(10,20))
print(sum(1920305, 3451238))

