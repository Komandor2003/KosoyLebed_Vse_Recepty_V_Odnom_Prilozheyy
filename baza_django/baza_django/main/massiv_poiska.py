from main.DB_connector import serch_meals

def massiv_poiska(inp):
    suggestions_list = serch_meals(inp)
    return suggestions_list
