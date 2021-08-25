import random as r

def mad_lib():
    verb = input("Enter a verb:")
    Scary = input("Enter a plural_noun:")
    food = input("Enter a food:")
    x = r.randint(1,3)

    if x <=1 :
        print("I " + verb + " away")
    elif x <=2 :
        print("I ran away from "+ Scary)
    else:
        print("I love eating " + food)




mad_lib()