import sqlite3
import os

#database settings
connection = sqlite3.connect("bot_database.db")
connection.execute("PRAGMA foreign_keys = ON")              

#ICONS INSERT :warning:
connection.execute("INSERT INTO ICON (NAME, ICON_NAME) VALUES ('NEW',':new:')");
connection.execute("INSERT INTO ICON (NAME, ICON_NAME) VALUES ('DOING',':pushpin:')");
connection.execute("INSERT INTO ICON (NAME, ICON_NAME) VALUES ('DONE',':white_check_mark:')");
connection.execute("INSERT INTO ICON (NAME, ICON_NAME) VALUES ('REVIEW',':warning:')");
connection.execute("INSERT INTO ICON (NAME, ICON_NAME) VALUES ('PROBLEM',':sos:')");

#User Settings
u1_name=os.getenv("NAME_USER1")
u2_name=os.getenv("NAME_USER2")
u3_name=os.getenv("NAME_USER3")
u1_id_discord=os.getenv("ID_DISCORD_USER1")
u2_id_discord=os.getenv("ID_DISCORD_USER2")
u3_id_discord=os.getenv("ID_DISCORD_USER3")
u1_discord=os.getenv("USER_DISCORD_USER1")
u2_discord=os.getenv("USER_DISCORD_USER2")
u3_discord=os.getenv("USER_DISCORD_USER3")
u1_email=os.getenv("EMAIL_DISCORD_USER1")
u2_email=os.getenv("EMAIL_DISCORD_USER2")
u3_email=os.getenv("EMAIL_DISCORD_USER3")

#USERBOT INSERT
connection.execute(f"INSERT INTO UserBot (NAME, id_discord, USER_DISCORD, EMAIL_DISCORD) VALUES ('{u1_name}','{u1_id_discord}','{u1_discord}','{u1_email}')");
connection.execute(f"INSERT INTO UserBot (NAME, id_discord, USER_DISCORD, EMAIL_DISCORD) VALUES ('{u2_name}','{u2_id_discord}','{u2_discord}','{u2_email}')");
connection.execute(f"INSERT INTO UserBot (NAME, id_discord, USER_DISCORD, EMAIL_DISCORD) VALUES ('{u3_name}','{u3_id_discord}','{u3_discord}','{u3_email}')");
'''
#LIST INSERT
connection.execute("INSERT INTO List (NAME, owner_id ) VALUES ('TODO',1)");
connection.execute("INSERT INTO List (NAME, owner_id ) VALUES ('TODO2',1)");
connection.execute("INSERT INTO List (NAME, owner_id ) VALUES ('TODO3',1)");
connection.execute("INSERT INTO List (NAME, owner_id ) VALUES ('TODO',2)");
connection.execute("INSERT INTO List (NAME, owner_id ) VALUES ('TODO',3)");

#TASK INSERT
connection.execute("INSERT INTO Task (desc, list_id, icon_status ) VALUES ('exemplo tarefa',1,1)");
'''
connection.commit()                     
connection.close()