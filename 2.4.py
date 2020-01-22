with open('recipes.txt', encoding='utf-8') as f:
    cook_book = {}
    while True:
        dish = f.readline().strip()
        cook_book[dish] = []
        person = f.readline().strip()
        i = 0
        while i < int(person):
            ingredients = f.readline().strip().split(' | ')
            cook_book[dish].append({'ingredient_name': ingredients[0], 'quantity': int(ingredients[1]),
                                    'measure': ingredients[2]})
            i += 1
        if f.readline() == '\n':
            continue
        else:
            break
# print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    ingredients_dict = {}
    dish_ingredients = []
    if type(dishes) == list:
        for dish in dishes:
            for key, value in cook_book.items():
                if dish == key:
                    dish_ingredients.append(value)
    else:
        for key, value in cook_book.items():
            if dishes == key:
                dish_ingredients.append(value)
    for ingredient in dish_ingredients:
        for ingr in ingredient:
            ingr_name = ingr['ingredient_name']
            ingredients_dict[ingr_name] = ingr
            del ingr['ingredient_name']
            ingr['quantity'] = ingr['quantity'] * person_count
    print(ingredients_dict)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 3)
