import main.DB_connector as DB
def massiv():
    menuData = DB.take_meals()
    return menuData