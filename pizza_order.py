from re import M


print("welcome to python pizza deliveries!")
size = input("What pizza size do you want? S, M or L:")
# wants_pepperoni = input("do you want pepperoni on your pizza? y or n:")
# extra_cheese = input("do you want extra cheese? y or n: ")

bill = 0
if size == "s":
    bill += 10
    
elif size == "m":
    bill += 15

elif size =="l":
    bill += 20

wants_pepperoni = input("do you want pepperoni on your pizza? y or n:")
if wants_pepperoni == "y":
    bill += 5
    print(f"your final bill is {bill}")

wants_extra_cheese = input("do you want extra cheese? y or n: ")
if wants_extra_cheese == 'y':
    bill += 1
    print(f"your final bill is {bill}")
else:
    print("type try again")

