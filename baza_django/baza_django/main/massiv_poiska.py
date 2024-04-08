from main.DB_connector import serch_meals

def massiv_poiska(inp):
    print(inp)
    suggestions_list = serch_meals(inp)
    print("!!!!")
    return suggestions_list
