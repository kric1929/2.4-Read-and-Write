from pprint import pprint


def cook_book_dict():
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
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = cook_book_dict()
    ingredients_dict = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredients in cook_book[dish]:
                if ingredients['ingredient_name'] not in ingredients_dict:
                    ingredients_dict[ingredients['ingredient_name']] = ingredients
                else:
                    ingredients_dict[ingredients['ingredient_name']]['quantity'] += ingredients['quantity']
    for key, value in ingredients_dict.items():
        del value['ingredient_name']
        value['quantity'] *= person_count
    pprint(ingredients_dict)


get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)
