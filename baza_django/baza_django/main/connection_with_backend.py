import main.DB_connector as DB
from main.DB_connector import serch_meals

def massiv_main():
    menuData = DB.take_meals()
    return menuData


def massiv_poiska(inp):
    suggestions_list = serch_meals(inp)
    return suggestions_list


def massiv_recipe(index):
    recipe_info = DB.take_meal("meals", "id", index)
    return recipe_info


def find_dishes_starting_with(inp):
    data = [
        {'index': 0, 'name': 'Фруктовый салат', 'image': '0000000.jpg',
         'description': 'Свежий салат с яблоками, бананами, апельсинами и грушами.', 'totalWeight': 450,
         'calories': 200, 'mealTime': 'утро вечер', 'containsMeat': 0, 'seafood': 0, 'healthy': 1, 'drink': 0,
         'difficulty': 'Легкий'},
        {'index': 1, 'name': 'Салат Цезарь', 'image': '0000001.jpg',
         'description': 'Классический салат Цезарь с курицей, сыром Пармезан и хрустящими крутонами.',
         'totalWeight': 350, 'calories': 350, 'mealTime': 'обед', 'containsMeat': 1, 'seafood': 0, 'healthy': 0,
         'drink': 0, 'difficulty': 'Средний'},
        {'index': 2, 'name': 'Борщ', 'image': '0000002.jpg',
         'description': 'Традиционный украинский борщ с говядиной, свеклой, картофелем и свежей зеленью.',
         'totalWeight': 400, 'calories': 300, 'mealTime': 'обед', 'containsMeat': 1, 'seafood': 0, 'healthy': 1,
         'drink': 0, 'difficulty': 'Средний'},
        {'index': 3, 'name': 'Секс на пляже', 'image': '0000003.jpg',
         'description': 'Освежающий коктейль с персиковым и апельсиновым соками, водкой и малибу.', 'totalWeight': 200,
         'calories': 250, 'mealTime': 'вечер', 'containsMeat': 0, 'seafood': 0, 'healthy': 0, 'drink': 1,
         'difficulty': 'Легкий'},
        {'index': 4, 'name': 'Паста карбонара', 'image': '0000004.jpg',
         'description': 'Итальянская паста карбонара с гуанчиале, сливочным соусом, пармезаном и яйцами.',
         'totalWeight': 350, 'calories': 600, 'mealTime': 'обед', 'containsMeat': 1, 'seafood': 0, 'healthy': 0,
         'drink': 0, 'difficulty': 'Средний'}
    ]
    result = []
    for dish in data:
        if dish['name'].startswith(inp):
            result.append(dish)
    return result
