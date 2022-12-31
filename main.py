#from keep_alive import keep_alive
import discord
from discord import app_commands
from discord.ext import commands
import my_config
import queries  
import embed_settings       

#bot settings
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix="+")
bot.remove_command('help')
user_listas=[]

@bot.event
async def on_ready():
  print(f"Estou pronto! Bem-vindo {bot.user}")

@bot.command(name="listas")
async def get_lists(ctx):
 # await ctx.message.delete()
  user_listas = queries.get_list_user(ctx.author.id)
  if not user_listas or len(user_listas) == 0:
    embed = embed_settings.info("``Não existem listas criadas para este usuário``","")
    await ctx.send(embed=embed)
  else:
    embed = embed_settings.lists_by_user(user_listas,ctx.author.id)
    await ctx.send(embed=embed)

@bot.command(name="add")
async def add_list(ctx):
  if ctx.message.author == bot.user:
    return

  if 'lista' in ctx.message.content:
    await ctx.send("Qual será o nome da nova lista?")
    message = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
    queries.create_list_user(message.content,ctx.author.id)
    embed = embed_settings.successful(f"```Lista {message.content} foi CRIADA com sucesso!```")
    await ctx.send(embed=embed)
    
  if 'tarefa' in ctx.message.content:
    await ctx.send("Digite o #ID da lista para a qual deseja adicionar a tarefa.")
    user_listas = queries.get_list_user(ctx.author.id)
    await ctx.send(user_listas)
    message = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
    await ctx.send("Digite a(s) tarefa(s) que deseja adicionar separadas por (;) ponto e virgula.")
    tasks_user = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
    tasks = split_tasks(tasks_user.content)
    result = queries.add_task_list_user(message.content,ctx.author.id, tasks)
    if result is True:
      embed = embed_settings.successful(f"``Tarefa criada com sucesso!``")
      await ctx.send(embed=embed)
    if result is False:
      embed = embed_settings.failure(f"``Não foi possível criar a Tarefa!``", "Algumas causas possíveis: \n - Não existe lista com o #ID informado \n - A lista informada não pertence ao usuário")
      await ctx.send(embed=embed)
 
@bot.command(name="delete")
async def delete_list(ctx):
  if ctx.message.author == bot.user:
    return

  if 'lista' in ctx.message.content:
    await ctx.send("Digite o #ID da lista que deseja deletar. \n **ATENÇÃO:** esta ação não poderá ser desfeita!")
    user_listas = queries.get_list_user(ctx.author.id)
    await ctx.send(user_listas)
    message = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
    result = queries.delete_list_user(message.content,ctx.author.id)
    if result is True:
      await ctx.send(embed=embed_settings.successful(f"```Lista {message.content} foi deletada com sucesso!```"))
    if result is False:
      await ctx.send(embed=embed_settings.successful(f"```Não foi possível deletar a lista informada!```","Algumas causas possíveis: \n - Não existe lista com o #ID informado \n - A lista informada não pertence ao usuário e não pode ser deletada por outro(s)"))


  if 'tarefa'in ctx.message.content:
    await ctx.send("Digite o #ID da lista que contém a tarefa que deseja deletar. \n **ATENÇÃO:** esta ação não poderá ser desfeita!")
    user_listas = queries.get_list_user(ctx.author.id)
    await ctx.send(user_listas)

    message = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
    list_id = message.content

    await ctx.send("Digite o #ID da tarefa que deseja deletar. \n **ATENÇÃO:** esta ação não poderá ser desfeita!")
    message = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
    result = queries.delete_task_list_user(list_id, ctx.author.id, message.content)
    if result is True:
      await ctx.send(embed=embed_settings.successful(f"```Tarefa deletada com sucesso!```"))
    if result is False:
      await ctx.send(embed=embed_settings.failure(f"```Não foi possível deletar a tarefa informada!```","Algumas causas possíveis: \n - Não existe lista com o #ID informado \n - A lista informada não pertence ao usuário e não pode ser deletada por outro(s)"))
    if result is None: await ctx.send(embed=embed_settings.failure(f"```Não foi possível deletar a tarefa informada!```","Algumas causas possíveis: \n - Não existe lista com o #ID informado \n - A lista informada não pertence ao usuário e não pode ser deletada por outro(s) \n - Indisponibilidade de Serviço. Fale com o administrador"))
 
def split_tasks(tasks_list):
  tasks=[]
  for task in tasks_list.split(';'):
    tasks.append(task)
  return tasks

@bot.command(name="tarefas")
async def get_tasks_by_list_id(ctx):
  await ctx.send("Digite o #ID da lista para consultar as tarefas:")
  message = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
  tasks_list = queries.all_task_list_user(message.content, ctx.author.id)
  if not tasks_list or len(tasks_list) == 0:
    embed = embed_settings.failure("``Não foi possível consultar as Tarefas para o #ID informado!``", "Algumas causas possíveis: \n - Não existe lista com o #ID informado \n - A lista está sem tarefas criadas \n - A lista informada não pertence ao usuário")
    await ctx.send(embed=embed)
  else:
    await ctx.send(embed=embed_settings.tasks_by_list(tasks_list)) 


@bot.command(name="update")
async def update_tasks(ctx):
  await ctx.send("Digite o #ID da tarefa que deseja atualizar:")
  message = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
  update_task = queries.task_user_by_id(int(message.content), ctx.author.id)
  if not update_task or len(update_task) <= 0:
    embed = embed_settings.failure("``Não foi localizar a tarefa informada!``", "Verifique o ID e tente novamente")
    await ctx.send(embed=embed)
  else:
    await ctx.send('Tarefa localizada!')
    await ctx.send(embed=embed_settings.task_id(update_task))
    await ctx.send('Digite o #ID do Status para o qual deseja atualizar a tarefa selecionada:')
    await ctx.send(embed=embed_settings.get_all_status_task())
    message = await bot.wait_for('message', check=lambda message: message.author == ctx.author)  
    update_task_status = queries.update_task(update_task.get('task_id'),message.content,ctx.author.id)
    if update_task_status is False:
      await ctx.send(embed=embed_settings.failure("Não foi possível atualizar a tarefa informada", "Verifique o status informado e tente novamente."))
    else:
      await ctx.send(embed=embed_settings.successful("Status da tarefa atualizado com sucesso!"))

@bot.command(name="all")
async def all_tasks_by_user(ctx):
  tasks_list = queries.all_task_by_user(ctx.author.id)
  if not tasks_list or len(tasks_list) == 0:
    embed = embed_settings.failure(f"``Não foi possível consultar suas tarefas!``",'Verifique o ID e tente novamente')
    await ctx.send(embed=embed)
  else:
    await ctx.send(embed=embed_settings.my_tasks(tasks_list))  

@bot.command(name="help")
async def help_bot(ctx):
  embed = embed_settings.failure(f"``Não foi possível consultar suas tarefas!``",'Verifique o ID e tente novamente')
  await ctx.send(embed=embed_settings.help_bot())    

#Apollo
#keep_alive()
bot.run(my_config.TOKEN)
