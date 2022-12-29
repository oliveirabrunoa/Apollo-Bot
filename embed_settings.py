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
    task_format+= '{0} | #{1} - {2} \n'.format(get_icon_by_id(t[3]),t[0],t[1]) 
        
  embed.add_field(name='Tarefas:',value='{0}'.format(task_format), inline=False)
  return embed

def get_icon_by_id(icon_id):
    for icon in list_icons:
        if int(icon.get('id')) == int(icon_id):            
            return icon.get('icon_name')