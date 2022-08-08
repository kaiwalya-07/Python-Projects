import random
names=input("Give me names seperated by comma\n")
names_ne=names.split(",")
print(names_ne)
x=len(names_ne)
random_name=random.randint(0,x-1)
print(f"{names_ne[random_name]} will buy a meal today")


#ALTERNATIVE METHOD TO THIS IS
#person_paying=random.choice(names_ne)
#print(person_paying)