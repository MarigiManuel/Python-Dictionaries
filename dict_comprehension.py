old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}
new_price = {}
for key, value in old_price.items():
    if value > 2:
        new_price[key] = value * 1.5
    else:
        new_price[key] = value

print(new_price)

# And the following code uses dictionary comprehension

new_price = {key : value *1.5 if value > 2 else value for (key, value) in old_price.items()}
    
print(new_price)