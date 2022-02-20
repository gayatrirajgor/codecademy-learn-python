#create lists
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']

prices = [2, 6, 1, 3, 2, 7, 2]

#count no of occurrences of 2
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

#find length 
num_pizzas = len(toppings)

print(f'We sell {num_pizzas} different kinds of pizza!')

#create 2D list
pizza_and_prices = [[2, 'pepperoni'], [6, 'pineapple'], [1, 'cheese'], [3, 'sausage'], [2, 'olives'], [7, 'anchovies'], [2, 'mushroom']]

#sort in ascending order
pizza_and_prices.sort()

#store elements
cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]

#remove last item
pizza_and_prices.pop()
print(pizza_and_prices)

#add new item
pizza_and_prices.insert(4 ,[2.5, 'peppers'])
print(pizza_and_prices)

#slice list
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)