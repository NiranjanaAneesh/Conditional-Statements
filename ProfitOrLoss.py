cost_price = float(input(" Please Enter the Cost Price of the Product:"))
selling_price = float(input(" Please Enter the Selling Price of the Product:"))

if (selling_price > cost_price):
    amount = selling_price - cost_price
    print("Total Profit = {0}".format(amount))
else:
    print("No Profit!")