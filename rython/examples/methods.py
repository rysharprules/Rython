def print_item(name, price_in_pennies = 100):
  formatted_price = '£{:.2f}'.format(price_in_pennies / 100.0)
  print('Item: ' + name)
  print('Price: ' + formatted_price)

print_item('Milk', 85)
print_item('Coffee', 249)
print_item('Orange Juice', 110)
print_item('Eggs') # default price
print_item(price_in_pennies = 1999, name = 'Jamesons') # keyword arguments (unordered)
print_item('Cat Food', price_in_pennies = 149) # mix of positional and named arguments

def multiply(a, b) -> int: # return type hint
    return a * b

