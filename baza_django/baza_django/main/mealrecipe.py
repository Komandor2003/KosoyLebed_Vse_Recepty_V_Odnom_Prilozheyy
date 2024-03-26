import main.DB_connector as DB

def massiv_recipe(index):
    # print("id : ", id)
    recipe_info = DB.take_meal("meals", "id", index)
    return recipe_info
