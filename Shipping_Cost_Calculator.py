#Shipping Cost Cakculator
##Input package weight and shipping rate

weight = float(input("Enter the package weight in Kgs: "))
rate = float(input("Enter the shipping rate per Kgs: "))

## Calculate Shipping Cost
shipping_cost = weight * price

print(f"Shipping Cost: {shipping_cost} USD")
