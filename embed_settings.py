import discord
import queries

list_icons = queries.get_icons()

def tasks_by_list(tasks_list): 
  embed = discord.Embed(
    title = '``Lista: {0}``'.format(tasks_list['list_name']),
    color = 0xfa5537)
  
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