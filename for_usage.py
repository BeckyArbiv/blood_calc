foods = ["apples", "bamamas", "cherries", "donuts", "eggplant"]
amounts = [11, 22, 33, 44, 55]


# for food in foods:
# 	print(food)
    
# for i, food in enumerate(foods):
#     print("{} - {}".format(amounts[i],food))


# for amount, food, liked in zip(amounts,foods, like):
#     print("{}-{}-{}".format(amount,food, liked))

def fruit_inventory(FOOD):
    for i, food in enumerate(foods):
        if foods[i] == FOOD:
            answer = amounts[i]
            break
    return answer
        
    
            
print(fruit_inventory("eggplant"))

def get_inventory(fruit_to_check):
    foundindex = foods.index(fruit_to_check)
    return amounts[foundindex]

print(get_inventory("apples"))