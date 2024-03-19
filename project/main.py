import mysql.connector


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

    def write(self, table, param, vals):

        vals_q = ("%s" for i in range(len(vals)))
        try:
            cursor = self.connect.cursor()
            query = f'INSERT INTO {table} {param} VALUES {vals_q}'
            cursor.execute(query)
            self.connect.commit()
            cursor.close()
            return True
        except Exception as err:
            cursor.close()
            print(err)
            return False

    def edit(self, table, params, vals, par, val):

        vals_q = ("%s" for i in range(len(vals)))
        try:
            cursor = self.connect.cursor()
            query = f'UPDATE {table} SET {params} VALUES {val_q} WHERE {par} = %s'
            data_to_insert = [val]
            cursor.execute(query, data_to_insert)
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

def take_meals(table="test"):
    return conn.select_all(table=table)


def take_meal(table, params, vals):
    return conn.select_group(table=table, param=params, val=vals)


def new_meal(table, params, vals):
    return conn.write(table=table, param=params, vals=vals)


def edit_meal():
    return conn.edit(table=table, param=params, vals=vals)


def roulet():
    tmp = conn.select_all(table=table)
    return tmp[1]