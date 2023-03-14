from math import *
print("Hello!!!! here I am again :(")
variables
a = 20
Name = "Shubhi Dewangan"
print(a,type(a))
print(Name,type(Name))
Navi=Nishi=Shubhi=Lokka=24
print(Shubhi)
Education,year="B.tech",2024
print("Hey! I am doing my",Education,"from SSTC \n My year of graduation is",year) 
print(ceil(34.7498))
print(floor(38.69))
print(factorial(12))
print("average")
cents = int(input('How many cents do you need to give out? '))

# Do computations
quarters = cents // 25
cents = cents % 25
dimes = cents // 10
cents = cents % 10
nickels = cents // 5
pennies = cents % 5

# Print results
print('Your change is')
if quarters > 1:
  print(str(quarters)+' quarters')
elif quarters == 1:
  print('1 quarter')

if dimes > 1:
  print(str(dimes)+' dimes')
elif dimes == 1:
  print('1 dime')

if nickels == 1:
  print('1 nickel')

if pennies > 1:
  print(str(pennies)+' pennies.')
elif pennies == 1:
  print('1 penny.')
s = int(input("Enter your salary: "))
y = int(input("Enter your year of sevice: "))
n = (s)*0.05
if (y<5):
    print("sorry you are new to us so no bonus")
else:
    print("congratulations, your new salary will be",n+s)
print("WELCOME TO OUR STORE")
q1=int(input("enter the amount of product: "))
q2=int(input("enter the amount of product: "))
q3=int(input("enter the amount of product: "))
sum = q1+q2
if (sum<1000):
    print("Your bill is ",sum)

elif (sum>1500):
    print("You got a 15% discount yay!, and your bill is ",sum-(0.15*sum))
else :
    print("you get a discount of 20%,so the amount you have to pay is ",sum-(0.2*sum))