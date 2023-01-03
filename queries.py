import sqlite3
import numbers

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
    list_icons = []
    icons = connection.execute(f"SELECT * FROM Icon").fetchall()
    for i in icons:
        list_icons.append({'id': i[0],'icon_name': i[2], 'name': i[1]})
    close_connection(connection)
    return list_icons

def get_username(author_id):
    connection = get_connection()
    users =  connection.execute(f"SELECT * FROM UserBot where id_discord={author_id}").fetchone()
    close_connection(connection)
    return {'id': users[0],'name': users[1]}

#LIST
def get_list_user(author_id):
    connection = get_connection()
    users =  connection.execute(f"SELECT id FROM UserBot where id_discord={author_id}")
    user_id = users.fetchone()[0]
    list_format = []
    if user_id:
        lists_users = connection.execute(f"SELECT * FROM List where owner_id={user_id}").fetchall()
        for l in lists_users:
            list_format.append({'id': l[0],'name': l[1], 'note_list': l[2]})
        close_connection(connection)
        return list_format
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
    return False

def delete_task_list_user(list_id, author_id, task_id):
    connection = get_connection()
    users =  connection.execute(f"SELECT id FROM UserBot where id_discord={author_id}")
    user_id = users.fetchone()[0]
    lists_users = connection.execute(f"SELECT * FROM List where id={int(list_id)} AND owner_id={user_id}")
    if lists_users.fetchone() and user_id:
        connection.execute(f"DELETE FROM Task where list_id={int(list_id)} AND id={int(task_id)}");  
        close_connection(connection)
        return True
    else:
        return False   

def all_task_list_user(list_id, author_id):
    connection = get_connection()
    users =  connection.execute(f"SELECT id FROM UserBot where id_discord={author_id}")
    user_id = users.fetchone()[0]
    lists_users = connection.execute(f"SELECT * FROM List where id={int(list_id)} AND owner_id={user_id}").fetchone()
    if lists_users and user_id:
        all_tasks_list = connection.execute(f"SELECT * FROM Task where list_id={int(list_id)}").fetchall()
        if len(all_tasks_list) > 0:
            close_connection(connection)
            return {'list_name': lists_users[1] ,'tasks_list':all_tasks_list, 'note_content': lists_users[2]}
        else:
            close_connection(connection)
            return False
    close_connection(connection)
    return  False

def task_user_by_id(task_id, author_id):
    connection = get_connection()
    users =  connection.execute(f"SELECT id FROM UserBot where id_discord={author_id}")
    user_id = users.fetchone()[0]
    task_by_id = connection.execute(f"SELECT Task.id, Task.desc, Task.icon_status FROM Task INNER JOIN List on Task.list_id=List.id \
                WHERE Task.id={int(task_id)} and List.owner_id={int(user_id)}").fetchone()
    if task_by_id:
        close_connection(connection)
        return {'task_id': task_by_id[0] ,'tasks_desc':task_by_id[1],'task_status_icon': task_by_id[2]}
    else:
        return False

def all_task_by_user(author_id):
    connection = get_connection()
    users =  connection.execute(f"SELECT id FROM UserBot where id_discord={author_id}")
    user_id = users.fetchone()[0]
    list_task_by_id = connection.execute(f"SELECT List.id, List.name, Task.id, Task.desc, Task.icon_status FROM Task INNER JOIN List on Task.list_id=List.id \
                WHERE List.owner_id={int(user_id)}").fetchall()
    list_format=[]                
    if len(list_task_by_id) > 0:
        for list in list_task_by_id:
            list_format.append({'list_id': list[0],'list_name':list[1],
        'task_id':list[2], 'task_desc':list[3],'task_status_icon':list[4]})
        close_connection(connection)
        return list_format
    else:
        return False

def update_task(task_id, status_id, author_id):
    connection = get_connection()
    users =  connection.execute(f"SELECT id FROM UserBot where id_discord={author_id}")
    user_id = users.fetchone()[0]
    update_task_final=''               
    if isinstance(task_id,numbers.Integral):
        try:
            update_task_final = connection.execute(f"UPDATE Task SET icon_status={int(status_id)}  \
                    WHERE Task.id={int(task_id)}").fetchall()
            close_connection(connection)
            return update_task_final
        except:
            return False
    else:
        return False

def create_or_update_note(list_id, note_content, author_id):
    connection = get_connection()
    users =  connection.execute(f"SELECT id FROM UserBot where id_discord={author_id}")
    user_id = users.fetchone()[0]            
    if isinstance(list_id,numbers.Integral):
        try:
            connection.execute(f"UPDATE List SET note_list='{note_content}' WHERE List.id={int(list_id)}")
            close_connection(connection)
            return True
        except:
            return False
    else:
        return False        
       