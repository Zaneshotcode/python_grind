
total = float(input("what was the total bill? $"))
tip = int(input("how much tip would you like to give? 10, 12, or 15? % "))
splits = int(input("how many people split"))
each_pay = round(float((tip / 100 + total)/ splits), 2)
print(each_pay)
