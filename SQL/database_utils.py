import mysql.connector, inspect

def add_item_to_database(name, serving_size, serving_unit, calories, protein, carbs, fat, sugar, saturated_fat):
    arg_inspect=inspect.getargvalues(inspect.currentframe())
    args = list(arg_inspect.locals.values())   # Get all of the input data (preset in correct order)
    
    my_db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="GoHokies25!",
        database="nutrition_info"
    )
    temp_cursor = my_db.cursor()
    
    temp_cursor.execute("SELECT item_id, MAX(item_id) FROM id_fetch GROUP BY item_id")
    id_num = temp_cursor.fetchall()[0][-1] + 1
    
    temp_cursor.execute(f"INSERT INTO id_fetch (item_name, item_ID) VALUES (\'{args[0]}\', {id_num})")
    
    insert_statement = "INSERT INTO macro_calculator_info (item_id, serving_size, serving_unit, calories, protein, carbs, fat, sugar, saturated_fat) VALUES ("
    args[0] = id_num
    for i in range(len(args)):
        insert_statement += f'{args[i]}, ' if i != 2 else f'\'{args[i]}\', '
    
    insert_statement = insert_statement[:-2] + ")"
    temp_cursor.execute(insert_statement)

    my_db.commit()

    temp_cursor.close()
    my_db.close()

def print_all_ids():
    my_db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="GoHokies25!",
        database="nutrition_info"
    )
    temp_cursor = my_db.cursor()
    temp_cursor.execute("SELECT * FROM id_fetch")
    for x in temp_cursor.fetchall():
        print(x)
    
        temp_cursor.close()
    my_db.close()

def print_all_macros():
    my_db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="GoHokies25!",
        database="nutrition_info"
    )
    temp_cursor = my_db.cursor()
    temp_cursor.execute("SELECT * FROM macro_calculator_info")
    for x in temp_cursor.fetchall():
        print(x)
    
    temp_cursor.close()
    my_db.close()


# FORMATTED IN
#   ID, SERVING_SIZE, SERVING_UNIT, CALS, PROTEIN, CARBS, FAT, SUGAR, SATURATED_FAT
#add_item_to_database("Heinz Ketchup", 1, "Tbsp", 10, 0, 1, 0, 1, 0)
print_all_ids()
print("-" * 80)
print_all_macros()