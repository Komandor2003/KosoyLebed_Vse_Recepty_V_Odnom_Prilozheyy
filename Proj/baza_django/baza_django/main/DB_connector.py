import mysql.connector

meals = {'id' : 0, 'name' : 1, 'image' : 2, 'description' : 3, 'fullDescription' : 4, 'totalWeight' : 5,
         'calories' : 6, 'mealTime' : 7, 'containsMeat' : 8, 'seafood' : 9, 'healthy' : 10,
         'drink' : 11, 'difficulty' : 12, 'mealRecipe' : 13, 'recipeSteps' : 14}
class connection():

    def __init__(self, host, user, password, database):
        self.connect = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database)

    def select_all(self, table):

        try:
            cursor = self.connect.cursor()
            query = f'SELECT * FROM {table}'
            cursor.execute(query)
            results = cursor.fetchall()
            cursor.close()
            return results
        except Exception as err:
            cursor.close()
            print(err)
            return 0

    def select_group(self, table, param, val):

        try:
            cursor = self.connect.cursor()
            query = f'SELECT * FROM {table} WHERE {param} = %s'
            cursor.execute(query, [str(val)])
            results = cursor.fetchall()
            cursor.close()
            return results
        except Exception as err:
            cursor.close()
            print(err)
            return 0
    def select_for_search(self, table, param , val):

        try:
            cursor = self.connect.cursor()
            query = f'SELECT * FROM {table} WHERE {param} LIKE %s LIMIT 10'
            cursor.execute(query,  (val + '%',))
            results = cursor.fetchall()
            cursor.close()
            return results
        except Exception as err:
            cursor.close()
            print(err)
            return 0

    def write(self, table, params, vals):

        try:
            cursor = self.connect.cursor()
            param_string = ', '.join(params)
            value_placeholders = ', '.join(['%s'] * len(vals))
            query = f'INSERT INTO {table} ({param_string}) VALUES ({value_placeholders})'
            cursor.execute(query, vals)
            self.connect.commit()
            cursor.close()
            return True
        except Exception as err:
            cursor.close()
            return [False, err]

    def edit(self, table, params, vals):

        try:
            cursor = self.connect.cursor()
            param_string = ', '.join(params)
            value_placeholders = ', '.join(['%s'] * (len(vals) - 1))
            query = f'UPDATE {table} SET   {param_string} = {value_placeholders} WHERE id = %s'
            cursor.execute(query, (*vals, ))
            self.connect.commit()
            cursor.close()
            return True
        except Exception as err:
            cursor.close()
            print(err)
            return False


conn = connection(host='127.0.0.1',
                  user='root',
                  password='1111',
                  database='KosoyLebed')


# print("соединение с базой данных установлено")

def take_meals(table = "meals"):
    tmp_all = conn.select_all(table=table)
    response = []
    for tmp in tmp_all:
        response.append({"name" : tmp[meals['name']], "image" : tmp[meals['image']],
                         "description" : tmp[meals['description']], "totalWeight" : tmp[meals['totalWeight']],
                         "calories" : tmp[meals['calories']], "mealTime" : tmp[meals['mealTime']],
                         "containsMeat" : tmp[meals['containsMeat']], "seafood" : tmp[meals['seafood']],
                         "healthy" : tmp[meals['healthy']], "drink" : tmp[meals['drink']],
                         "difficulty" : tmp[meals['difficulty']]})
    print(response)
    return response


def take_meal(table = "meals", param = "id", val = 0):

    tmp = conn.select_group(table=table, param=param, val=val)

    tmp = tmp[0]

    ingredients = tmp[meals['mealRecipe']]
    ingredients = ingredients.split("/")

    mT = tmp[meals['mealTime']]
    mT = mT.split()

    mS = tmp[meals['recipeSteps']]
    mS = mS.split("/")
    # mS = mS[:-1] #-1 только в тестовой версии, так как не правильно создана запись в БД
    mS_tmp = []
    for i in mS:
        if i == "":
            break
        i_tmp = i.split("_")
        mS_tmp.append({"text" : i_tmp[0], "image" : i_tmp[1],})

    response = {"mealRecipe":{"Название" : tmp[meals['name']], "image" : tmp[meals['image']],
                         "Описание" : tmp[meals['fullDescription']], "Ингредиенты" : ingredients,
                         "totalWeight" : tmp[meals['totalWeight']],
                         "calories" : tmp[meals['calories']], "mealTime" : mT,
                         "containsMeat" : tmp[meals['containsMeat']], "seafood" : tmp[meals['seafood']],
                         "healthy" : tmp[meals['healthy']], "drink" : tmp[meals['drink']],
                         "difficulty" : tmp[meals['difficulty']], "Шаги" : mS_tmp}}

    return response


def new_meal(table, params, vals):
    return conn.write(table=table, params=params, vals=vals)


def edit_meal(table, params, vals):
    return conn.edit(table=table, params = params, vals=vals)

def serch_meals(input):
    tmp = conn.select_for_search(table= "meals", param = "name", val=input)
    tmp = tmp[0]
    return (tmp[meals['name']])