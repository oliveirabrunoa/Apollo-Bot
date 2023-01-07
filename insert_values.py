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
u1_id_discord=os.getenv("ID_DISCORD_USER1")
u2_id_discord=os.getenv("ID_DISCORD_USER2")
u3_id_discord=os.getenv("ID_DISCORD_USER3")

#USERBOT INSERT
connection.execute(f"INSERT INTO UserBot (id_discord) VALUES ('{u1_id_discord}')");
connection.execute(f"INSERT INTO UserBot (id_discord) VALUES ('{u2_id_discord}')");
connection.execute(f"INSERT INTO UserBot (id_discord) VALUES ('{u3_id_discord}')");

connection.commit()                     
connection.close()