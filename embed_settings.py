import discord
import queries

list_icons = queries.get_icons()

def tasks_by_list(tasks_list):
  print('RECEBIDO NO EMBSETT: ', tasks_list)
  
  embed = discord.Embed(
    title = '``{0}``'.format(tasks_list['list_name']),
    color = 0x39ff14
  )
  
  embed.set_footer(text= 'author_embed')
  all_tasks = tasks_list['tasks_list']
  task_format=' '
  for t in all_tasks:
    task_format+= "#{0} | {1} - {2} \n".format(t[0], t[1], t[2]) 
    
  embed.add_field(name='__*Tarefas dessa lista:*__',value='{0}'.format(task_format), inline=False)
  
  return embed