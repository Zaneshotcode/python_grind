height = int(input("what is your height in cm?"))

if height >= 120:
    print("you can ride rollercoaster")
    age = int(input("what is your age?"))
    if age <= 12:
        bill = 5
        print("please pay 5")
    elif age <= 18:
        bill = 7
        print("pay 7")
    else:
        bill = 12
        print("please pay 12")
    
    wants_photo = input("do you want picture? type y/n")
    if wants_photo == 'y':
        #add 3 to their bill 
        bill += 3
    print(f'your final bill is {bill}')
else:
    print("sorry you cant")