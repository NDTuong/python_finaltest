import foodStorage
import recipe
import request
from os import path
import json

if not path.exists("data/foodStorage.json"):
    new_file = open("data/foodStorage.json", "x")
    foodStorage.set_default("data/foodStorage.json")
if not path.exists("data/recipe.json"):
    new_file = open("data/recipe.json", "x")

while True:
    print("******* Food Management *******")
    print("1. Update food Storage \n2. Add new dish \n3. Order \n4. Exit \nChoice one option: ")
    choice = input()
    if choice == "1":
        foodStorage.add()
    if choice == "2":
        recipe.input_recipe()
    if choice == "3":
        try:
            with open("data/foodStorage.json") as fs:
                food_storage = json.load(fs)
        finally:
            fs.close()
        order = request.input_request()
        if order:
            sort_order = request.sort_request_by_profit(order)
            boo, over, lacks, count = foodStorage.check(food_storage, sort_order)
            foodStorage.update(food_storage)
            if not boo:
                print("lack of food: ", over)
                print("not enough materials: ", lacks)
                s = request.suggest(food_storage, count)
                print("you can choose: ", s, " instead")
            else:
                print("Order success...")
    if choice == "4":
        break
    if choice not in ["1", "2", "3", "4"]:
        print("please choice 1,2, or 3")
