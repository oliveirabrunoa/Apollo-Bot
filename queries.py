import sqlite3

def get_connection():
    #database settings
    connection = sqlite3.connect("bot_database.db")
    connection.execute("PRAGMA foreign_keys = ON")
    return connection

def close_connection(connection):
    connection.commit()                     
    connection.close()
    return

def get_icons():
    connection = get_connection()
    icons = connection.execute(f"SELECT * FROM Icon").fetchall()
    close_connection(connection)
    return icons

#LIST
def get_list_user(author_id):
    connection = get_connection()
    users =  connection.execute(f"SELECT id FROM UserBot where id_discord={author_id}")
    user_id = users.fetchone()[0]
    if user_id:
        lists_users = connection.execute(f"SELECT * FROM List where owner_id={user_id}").fetchall()
        close_connection(connection)
        return lists_users
    return "Ocorreu um erro ao consultar a lista"

def create_list_user(list_name, author_id):
    connection = get_connection()
    users =  connection.execute(f"SELECT id FROM UserBot where id_discord={author_id}")
    user_id = users.fetchone()[0]
    connection.execute(f"INSERT INTO List (name, owner_id) VALUES ('{list_name}',{user_id})");   
    close_connection(connection)
    return

def delete_list_user(list_id, author_id):
    connection = get_connection()
    users =  connection.execute(f"SELECT id FROM UserBot where id_discord={author_id}")
    user_id = users.fetchone()[0]
    lists_users = connection.execute(f"SELECT * FROM List where id={int(list_id)} AND owner_id={user_id}")
    if lists_users.fetchone():
        connection.execute(f"DELETE FROM List where id={int(list_id)} AND owner_id={int(user_id)}");  
        close_connection(connection)
        return True
    close_connection(connection)
    return False

#TASK
def add_task_list_user(list_id, author_id, tasks):
    connection = get_connection()
    users =  connection.execute(f"SELECT id FROM UserBot where id_discord={author_id}")
    user_id = users.fetchone()[0]
    lists_users = connection.execute(f"SELECT * FROM List where id={int(list_id)} AND owner_id={user_id}")
    if lists_users.fetchone() and user_id:
        for task_item in tasks:
            connection.execute(f"INSERT INTO Task (desc, list_id, icon_status ) VALUES ('{task_item}',{int(list_id)},{1})");        
        close_connection(connection)
        return True
    return

def delete_task_list_user(list_id, author_id, task_id):
    connection = get_connection()
    users =  connection.execute(f"SELECT id FROM UserBot where id_discord={author_id}")
    user_id = users.fetchone()[0]
    lists_users = connection.execute(f"SELECT * FROM List where id={int(list_id)} AND owner_id={user_id}")
    if lists_users.fetchone() and user_id:
        connection.execute(f"DELETE FROM Task where list_id={int(list_id)} AND id={int(task_id)}");  
        close_connection(connection)
        return True
    return    

def all_task_list_user(list_id, author_id):
    connection = get_connection()
    users =  connection.execute(f"SELECT id FROM UserBot where id_discord={author_id}")
    user_id = users.fetchone()[0]
    lists_users = connection.execute(f"SELECT * FROM List where id={int(list_id)} AND owner_id={user_id}").fetchone()
    if lists_users and user_id:
        all_tasks_list = connection.execute(f"SELECT * FROM Task where list_id={int(list_id)}").fetchall()
        close_connection(connection)
        return {'list_name': lists_users[1] ,'tasks_list':all_tasks_list}
    return  

