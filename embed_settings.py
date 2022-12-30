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
    task_format+= '{0} | **#ID: {1}**:  {2} \n'.format(get_icon_by_id(t[3]),t[0],t[1]) 
        
  embed.add_field(name='Tarefas:',value='{0}'.format(task_format), inline=False)
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

def my_tasks(tasks_list): 
  embed = discord.Embed(
    title = '``Suas Tarefas (todas as listas):``',
    color = 0xFFFF00)
  
  all_task_format=' '
  for t in tasks_list:    
    all_task_format+= '**#ID: {0}**:  {1} | **Status**: {2} | **Lista**: {3} \n'.format(t.get('task_id'), t.get('task_desc'),
    get_icon_by_id(int(t.get('task_status_icon'))), t.get('list_name')) 
        
  embed.add_field(name='Tarefas:',value='{0}'.format(all_task_format), inline=False)
  return embed

def task_id(update_task): 
  embed = discord.Embed(
      color = 0xFFFF00)  
  all_task_format= '**#ID**: {0} | Tarefa: {1} | Status: {2}'.format(update_task.get('task_id'),update_task.get('tasks_desc'),update_task.get('task_status_icon'))
  embed.add_field(name='Tarefa:',value='{0}'.format(all_task_format), inline=False)
  return embed
