import discord
import queries

list_icons = queries.get_icons()

def tasks_by_list(tasks_list): 
  embed = discord.Embed(
    title = '``Lista: {0}``'.format(tasks_list['list_name']),
    color = 0xffffff)
  
  all_tasks = tasks_list['tasks_list']
  task_format=' '
  for t in all_tasks:    
    task_format+= '{0} | **#ID: {1}** |  {2} \n'.format(get_icon_by_id(t[3]),t[0],t[1]) 
        
  embed.add_field(name='Tarefas:',value='{0}'.format(task_format), inline=False)
  embed.add_field(name='Nota da Lista:',value='{0}'.format(tasks_list['note_content']), inline=False)
  return embed

def get_icon_by_id(icon_id):
    for icon in list_icons:
        if int(icon.get('id')) == int(icon_id):            
            return icon.get('icon_name')

def lists_by_user(lists, author_id):
    username= queries.get_username(author_id)
    embed = discord.Embed(
    title = '**Olá {0},**'.format(username.get("name")),
    color = 0x521987)
  
    list_format=' '
    for l in lists:
        list_format+= ':small_orange_diamond: **#ID: {0}**: {1} \n'.format(l.get('id'), l.get('name'))

    embed.add_field(name='Essas são as suas listas:',value='{0}'.format(list_format), inline=False) 
    return embed

def successful(message_embed):    
    embed = discord.Embed(
    title = '{0}'.format(message_embed),
    color = 0x00ff00)
    return embed

def failure(message_embed, description):    
    embed = discord.Embed(
    title = '{0}'.format(message_embed),
    description= '{0}'.format(description),
    color = 0xe32b2b)
    return embed

def info(message_embed, description):    
    embed = discord.Embed(
    title = '{0}'.format(message_embed),
    description= '{0}'.format(description),
    color = 0x3b81f1)
    return embed    

def get_all_status_task(): 
    icons_format = queries.get_icons()
    temp=' '
    for icon in icons_format:
      temp+= '{0} | **#ID**: {1} | {2} \n'.format(icon.get('icon_name'),icon.get('id'),icon.get('name')) 

    embed = discord.Embed(
    title = '{0}'.format("Status Disponíveis:"),
    description= '{0}'.format(temp),
    color = 0x00FFFF)  
    return embed        

def my_tasks(tasks_list): 
  embed = discord.Embed(
    title = '``Suas Tarefas (todas as listas):``',
    color = 0xFFFF00)
  
  all_task_format=' '
  for t in tasks_list:
    if get_icon_by_id(int(t.get('task_status_icon'))) == ':white_check_mark:':
      all_task_format+= '{2} | **{0}** | ~~{1}~~ >> {3} \n'.format(t.get('task_id'), t.get('task_desc'),
      get_icon_by_id(int(t.get('task_status_icon'))), t.get('list_name'))  
    else: 
      all_task_format+= '{2} | **{0}** | _{1}_ >> {3} \n'.format(t.get('task_id'), t.get('task_desc'),
      get_icon_by_id(int(t.get('task_status_icon'))), t.get('list_name')) 
        
  embed.add_field(name='Tarefas:',value='{0}'.format(all_task_format), inline=False)
  return embed

def task_id(update_task): 
  embed = discord.Embed(
      color = 0xFFFF00)  
  all_task_format= '**#ID**: {0} | **Tarefa**: {1} | **Status**: {2}'.format(update_task.get('task_id'),update_task.get('tasks_desc'),update_task.get('task_status_icon'))
  embed.add_field(name='Tarefa:',value='{0}'.format(all_task_format), inline=False)
  return embed

def help_bot():  
  embed = discord.Embed(
  title = '{0}'.format("Help"),
  description= '{0}'.format("Confira as ações disponíveis na versão 1.0"),
  color = 0xdaa520)

  embed.add_field(name=':small_blue_diamond: Consultar todas as listas:',value='{0}'.format("+listas"), inline=False)
  embed.add_field(name=':small_blue_diamond: Criar nova lista:',value='{0}'.format("+add lista"), inline=False)
  embed.add_field(name=':small_blue_diamond: Deletar uma lista:',value='{0}'.format("+del lista"), inline=False)

  embed.add_field(name=':small_blue_diamond: Consultar todas as tarefas de uma lista:',value='{0}'.format("+tarefas"), inline=False)
  embed.add_field(name=':small_blue_diamond: Criar uma nova tarefa:',value='{0}'.format("+add tarefa"), inline=False)
  embed.add_field(name=':small_blue_diamond: Deletar uma tarefa:',value='{0}'.format("+del tarefa"), inline=False)
  embed.add_field(name=':small_blue_diamond: Atualizar status de uma tarefa:',value='{0}'.format("+update"), inline=False)
  embed.add_field(name=':small_blue_diamond: Visualizar as tarefas de todas as listas:',value='{0}'.format("+all"), inline=False)

  return embed 
