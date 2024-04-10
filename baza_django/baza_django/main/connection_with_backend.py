import main.DB_connector as DB
from main.DB_connector import serch_meals

def massiv_main():

    menuData = DB.take_meals()

    return menuData


def massiv_poiska(inp):
    suggestions_list = serch_meals(inp)
    return suggestions_list[:10]


def massiv_recipe(index):
    recipe_info = DB.take_meal("meals", "id", index)
    return recipe_info


def find_dishes_starting_with(inp):
    suggestions_list = serch_meals(inp)

    data = []
    for i in suggestions_list:

        tmp = DB.take_meals_search(i)
        for j in tmp :

            data.append(tmp[0])
    return data
