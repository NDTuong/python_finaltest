import json


# Set all the number of materials to 0
def set_default(datafile):
    data = {"banhmy": {"price": 1000, "number": 0}, "gio": {"price": 2500, "number": 0},
            "xucxich": {"price": 4000, "number": 0}, "com": {"price": 1500, "number": 0},
            "trung": {"price": 1500, "number": 0}, "my": {"price": 2000, "number": 0},
            "pate": {"price": 3000, "number": 0}, "rau": {"price": 1000, "number": 0},
            "cha": {"price": 2000, "number": 0}}
    try:
        File = open(datafile, "w+")
        json.dump(data, File, indent=4)
        File.close()
    except:
        print("Cannot set")
        return False
    return True


# Add to the Storage
def add():
    # return True of False tuong ung thanh cong hay khong
    try:
        datafile = "data/foodStorage.json"  # Change datafile here
        with open(datafile, "r") as File:
            data = json.load(File)
            add_list = input("Enter the additional items eg:gio 1,trung 2,com 3,banhmy 4,xucxich 5 : ").split(",")
            for item in add_list:
                add = item.split()
                material = add[0]
                number = int(add[1])
                data.get(material)["number"] += number
        with open(datafile, "w") as File:
            json.dump(data, File, indent=4)
            print("Add Successfully!")
    except:
        print("Add Unsuccessfully!!!")
        return False
    return True


# Check if food storage have enough material for requirement
def check(food_storage, request):
    try:
        with open("data/recipe.json") as r:
            recipe = json.load(r)
    finally:
        r.close()
    over = {}
    boo = True
    lacks = {}
    count = 0
    for food in request.keys():
        materials = recipe[food][1]
        not_enough = 0
        for m in materials.keys():
            temp_not_enough = 0
            number = food_storage[m]["number"]
            number -= materials[m] * request[food]
            if number < 0:
                temp = int(-number / recipe[food][1][m])
                if temp != int(temp):
                    temp = int(temp) + 1
                if not_enough < temp:
                    not_enough = int(temp)
                    temp_not_enough = int(temp)
                if m not in lacks.keys():
                    lacks[m] = 0
                lacks[m] += - number
                boo = False
                food_storage[m]["number"] -= materials[m] * (request[food] - temp_not_enough)
            if not_enough == 0:
                food_storage[m]["number"] -= materials[m] * request[food]
        count += not_enough
        over[food] = not_enough
    return boo, over, lacks, count


# Update Storage
def update(data):
    # return true of false tuong ung thanh cong hay khong
    datafile = "data/foodStorage.json"
    try:
        with open(datafile, "w") as write:
            json.dump(data, write, indent=4)
    except:
        print("Order fail....")

