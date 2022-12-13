
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
 

name1 = name1.lower()
name2 = name2.lower()

t = name1.count('t') + name2.count('t')
r = name1.count('r') + name2.count('r')
u = name1.count('u') + name2.count('u')
e = name1.count('e') + name2.count('e')

l = name1.count('l') + name2.count('l')
o = name1.count('o') + name2.count('o')
v = name1.count('v') + name2.count('v')
e = name1.count('e') + name2.count('e')

true = t + r + u + e
love = l + o + v + e
 

true_love = int(str(true) + str(love))
 
if true_love < 10 or true_love >= 90:
    if true_love < 10: 
        print(f"Your love score is {true_love}, you both are lousy lovers")
    elif true_love >= 90:
        print(f"Your love score is {true_love}, you both are crazy amazing lovers")


elif true_love > 50 :
    print(f"Your love score is {true_love}, you both are great lovers. Meant to be together forever !!")
elif true_love >= 40 and true_love <= 50:
    
    print(f"Your score is {true_love}, you are alright together.")

else:
    print(f"Your score is {true_love}.")
