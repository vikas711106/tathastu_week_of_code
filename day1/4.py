cost_price=int(input("Enter the cost number:"))
selling_price=int(input("Enter selling price:"))
if((selling_price-cost_price)>0):
    print("Profit=",selling_price-cost_price)
else:
    print("Loss is occur")
profit=(5*cost_price)/100
print("Profit increse after increses 5%:",profit+selling_price)
