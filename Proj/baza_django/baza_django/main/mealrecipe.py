import main.DB_connector as DB
def massiv_recipe():
    recipe_info = DB.take_meal()
    return recipe_info
