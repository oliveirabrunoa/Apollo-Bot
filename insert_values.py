import sqlite3

#database settings
connection = sqlite3.connect("bot_database.db")
connection.execute("PRAGMA foreign_keys = ON")              

#ICONS INSERT
connection.execute("INSERT INTO ICON (NAME, ICON_NAME) VALUES ('NEW',':new:')");
connection.execute("INSERT INTO ICON (NAME, ICON_NAME) VALUES ('DONE',':white_check_mark:')");
connection.execute("INSERT INTO ICON (NAME, ICON_NAME) VALUES ('REVIEW',':arrows_counterclockwise:')");
connection.execute("INSERT INTO ICON (NAME, ICON_NAME) VALUES ('REJECT',':sos:')");

#USERBOT INSERT
connection.execute("INSERT INTO UserBot (NAME, id_discord, USER_DISCORD, EMAIL_DISCORD) VALUES ('Bruno Oliveira','1050592371584290836','Bruno Oliveira#5347','unasolucoesdigitais@gmail.com')");
connection.execute("INSERT INTO UserBot (NAME, id_discord, USER_DISCORD, EMAIL_DISCORD) VALUES ('André Nery','1052993072289550399','André Nery#9696','andrenerytreinamentos@gmail.com')");
connection.execute("INSERT INTO UserBot (NAME, id_discord, USER_DISCORD, EMAIL_DISCORD) VALUES ('Danilo Bacellar','1053818277530452051','Danilo Bacellar#8607','danilo@unasolucoesdigitais.com.br')");
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