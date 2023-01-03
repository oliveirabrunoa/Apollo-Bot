import sqlite3

#database settings
connection = sqlite3.connect("bot_database.db")
connection.execute("PRAGMA foreign_keys = ON")
connection.execute("CREATE TABLE IF NOT EXISTS Icon \
                    (id INTEGER PRIMARY KEY, \
                    name STRING, \
                    icon_name STRING);")
connection.execute("CREATE TABLE IF NOT EXISTS UserBot \
                    (id INTEGER PRIMARY KEY, \
                    name STRING, \
                    id_discord STRING, \
                    user_discord STRING, \
                    email_discord STRING);")                    
connection.execute("CREATE TABLE IF NOT EXISTS List \
                    (id INTEGER PRIMARY KEY, \
                    name STRING, \
                    note_list VARCHAR DEFAULT '', \
                    owner_id INTEGER NOT NULL, \
                    foreign key (owner_id) references UserBot(id));")
connection.execute("CREATE TABLE IF NOT EXISTS Task \
                    (id INTEGER PRIMARY KEY, \
                     desc STRING NOT NULL, \
                     list_id INTEGER NOT NULL, \
                     icon_status INTEGER NOT NULL, \
                     foreign key (icon_status) references Icon(id) \
                     foreign key (list_id) references List(id));")   

connection.commit()                     
connection.close()